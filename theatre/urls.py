from rest_framework import routers

from theatre.views import TheatreHallViewSet, GenreViewSet, ActorViewSet, PlayViewSet

router = routers.DefaultRouter()
router.register("theatre_halls", TheatreHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("plays", PlayViewSet)

urlpatterns = router.urls

app_name = "theatre"
