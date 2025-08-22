from rest_framework.routers import DefaultRouter
from .views import WorkspaceMemberViewSet


router = DefaultRouter(trailing_slash=False)
router.register("workspace_member", WorkspaceMemberViewSet, basename="workspace-member")

urlpatterns = router.urls
