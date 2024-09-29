from django.http import JsonResponse
from django.views import View
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import JobPost
from .core import RecommendationEngine

class JobPostAPIView(View):
    queryset = JobPost.objects.all()

    def get(self, request, *args, **kwargs):
        page = self.get_page(request)
        data = {
            "meta": {
                "current_page": page.number,
                "has_next": page.has_next(),
                "has_previous": page.has_previous(),
                "total": page.paginator.count,
            },
            "data": [job_post.to_dict() for job_post in page.object_list]
        }
        return JsonResponse(data)

    def get_page(self, request):
        page_no = request.GET.get("page", 1)
        per_page = request.GET.get("per_page", 10)
        
        paginator = Paginator(self.queryset, per_page)

        try:
            page = paginator.page(page_no)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        
        return page


class JobPostRecommendation(View):
    queryset = JobPost.objects.all()

    def get(self, request, *args, **kwargs):
        query = request.GET.get("query", "")
        if not query:
            return JsonResponse({"error": "No query given"})

        recommendation_engine = RecommendationEngine(settings.RECOMMENDATION_MODEL)
        job_post_details = recommendation_engine.similarity_search(
            query,
            filter_func=lambda df: df.drop(columns=['embedding', 'text', 'skills_str'], inplace=True)

        )
        return JsonResponse(job_post_details, safe=False)
