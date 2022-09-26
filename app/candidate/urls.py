from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from candidate import views


router = DefaultRouter()
router.register("", views.CandidateViewSet)

app_name = "candidate"

urlpatterns = [
    path("", include(router.urls)),
]
