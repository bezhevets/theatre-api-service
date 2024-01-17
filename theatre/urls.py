from rest_framework import routers

from theatre.views import TheatreHallViewSet, GenreViewSet, ActorViewSet, PlayViewSet, PerformanceViewSet

router = routers.DefaultRouter()
router.register("theatre_halls", TheatreHallViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("plays", PlayViewSet)
router.register("performance", PerformanceViewSet)

urlpatterns = router.urls

app_name = "theatre"
