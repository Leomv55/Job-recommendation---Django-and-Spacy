from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Playground"

    def handle(self, *args: Any, **options: Any):
        from recommendation.utils import get_vector_cache
        df = get_vector_cache()
        print(df["skills"])