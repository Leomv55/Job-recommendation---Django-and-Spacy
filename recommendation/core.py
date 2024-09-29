from sklearn.metrics.pairwise import cosine_similarity 

from .utils import (
    get_vector_cache,
    get_model
)


class RecommendationEngine:

    def __init__(self, model) -> None:
        self.model = model

    def similarity_search(self, query, filter_func=None, max_result=10):
        nlp = get_model(self.model)
        df = get_vector_cache()

        query_vector = nlp.get_vector(query)
        df['similarity'] = df['embedding'].apply(lambda x: cosine_similarity([query_vector], [x]).flatten()[0])

        ranked_jobs = df.sort_values(by='similarity', ascending=False)
        if filter_func:
            filter_func(ranked_jobs)

        top_results = ranked_jobs.head(max_result)
        return top_results.to_dict(orient="records")
