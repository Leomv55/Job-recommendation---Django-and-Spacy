import pandas as pd

from django.conf import settings

from .nlp_models import (
    SpacyModel,
    SBertModel,
)

def update_vector_cache(df):
    try:
        exising_df = pd.read_pickle(settings.VECTOR_CACHE_PATH)
    except Exception as inst:
        exising_df = pd.DataFrame()

    if exising_df.empty:
        exising_df = df
    else:
        df.set_index("id")
        exising_df.set_index("id")
        exising_df.update(df, overwrite=True)

    exising_df.to_pickle(settings.VECTOR_CACHE_PATH)


def get_vector_cache():
    try:
        return pd.read_pickle(settings.VECTOR_CACHE_PATH)
    except Exception:
        raise Exception("Make sure vector cache is available !!")


def get_model(model):
    if model == "spacy":
        return SpacyModel.get_instance()
    elif model == "sbert":
        return SBertModel.get_instance()

    raise ValueError(f"Unknon model: {model}")


def convert_job_posts_to_df(job_posts):
    job_post_list = []
    for job_post in job_posts:
        job_post_list.append(job_post.to_dict())
    
    return pd.DataFrame(job_post_list)


def add_embedding_for_job_posts_df(df):
    nlp = get_model(settings.RECOMMENDATION_MODEL)

    df['skills_str'] = df['skills'].apply(lambda x: ' '.join(x))
    df['text'] = df['title'] + ' ' + df['description'] + ' ' + df['skills_str']
    df['embedding'] = df['text'].apply(lambda x: nlp.get_vector(x))

    return df
