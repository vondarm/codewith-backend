from rest_framework.routers import DefaultRouter
from .views import RoomMemberViewSet

router = DefaultRouter(trailing_slash=False)
router.register("room_member", RoomMemberViewSet, basename="room-member")

urlpatterns = router.urls
