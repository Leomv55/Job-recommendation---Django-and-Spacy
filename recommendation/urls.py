from django.urls import path

from .views import JobPostAPIView, JobPostRecommendation

urlpatterns = [
    path("jobs/", JobPostAPIView.as_view(), name="job_post_api_view"),
    path("recommend-jobs/", JobPostRecommendation.as_view(), name="job_Recommendation_api_view"),
]