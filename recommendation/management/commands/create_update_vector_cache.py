from django.core.management.base import BaseCommand
from django.core.paginator import Paginator

from recommendation.models import JobPost
from recommendation.utils import (
    convert_job_posts_to_df,
    add_embedding_for_job_posts_df,
    update_vector_cache,
)


class Command(BaseCommand):
    help = "Create vector cache"

    def handle(self, *args, **kwargs):
        queryset = JobPost.objects.all().order_by("id")
        paginator = Paginator(queryset, 10)

        for page_number in paginator.page_range:
            job_post_list = paginator.get_page(page_number).object_list
            df = convert_job_posts_to_df(job_post_list)
            df = add_embedding_for_job_posts_df(df)
            update_vector_cache(df)

        print("Completed updating vector Cache .....")
