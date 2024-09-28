import spacy

from .utils import (
    get_vector_cache,
    get_model
)
from sklearn.metrics.pairwise import cosine_similarity 


class RecommendationEngine:

    def __init__(self, model) -> None:
        self.model = model


    def similarity_search(self, query, filter_func=None, columns_to_drop=[], max_result=10):
        nlp = get_model(self.model)
        df = get_vector_cache()

        query_vector = nlp(query).vector
        df['similarity'] = df['embedding'].apply(lambda x: cosine_similarity([query_vector], [x]).flatten()[0])

        ranked_jobs = df.sort_values(by='similarity', ascending=False)
        if filter_func:
            filter_func(ranked_jobs)

        top_results = ranked_jobs.head(max_result)
        return top_results.to_dict(orient="records")


class SpacyModel:

    @classmethod
    def get_instance(cls):
        if hasattr(cls, "_model"):
            return cls._model

        cls._model = cls._load_spacy()
        return cls._model

    @classmethod
    def _load_spacy(cls):
        try:
            nlp = spacy.load("en_core_web_md")
            return nlp
        except Exception as e:
            raise RuntimeError("Failed to load spaCy model") from e         