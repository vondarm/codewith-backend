from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkspaceMemberViewSet


router = DefaultRouter()
router.register("", WorkspaceMemberViewSet, basename="workspace-member")

urlpatterns = router.urls
