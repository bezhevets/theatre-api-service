from rest_framework import routers

from theatre.views import TheatreHallViewSet, GenreViewSet

router = routers.DefaultRouter()
router.register("theatre_halls", TheatreHallViewSet)
router.register("genre", GenreViewSet)

urlpatterns = router.urls

app_name = "theatre"
