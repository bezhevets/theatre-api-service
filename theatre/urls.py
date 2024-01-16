from rest_framework import routers

from theatre.views import TheatreHallViewSet, GenreViewSet, ActorViewSet

router = routers.DefaultRouter()
router.register("theatre_halls", TheatreHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)

urlpatterns = router.urls

app_name = "theatre"
