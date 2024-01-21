from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from theatre.models import Play, Genre, Actor
from theatre.serializers import PlayListSerializer, PlayDetailSerializer

PLAY_URL = reverse("theatre:play-list")


def detail_url(play_id: int):
    return reverse("theatre:play-detail", args=[play_id])


def sample_play(**params):
    defaults = {
        "title": "Test Play",
        "description": "Test Description"
    }
    defaults.update(params)
    return Play.objects.create(**defaults)


def sample_genre(**params):
    defaults = {
        "name": "Test Genre",
    }
    defaults.update(params)
    return Genre.objects.create(**defaults)


def sample_actor(**params):
    defaults = {
        "first_name": "test first_name",
        "last_name": "test last_name"
    }
    defaults.update(params)
    return Actor.objects.create(**defaults)


class UnauthenticatedPlayApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(PLAY_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedPlayApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="testfortest@test.com",
            password="Test122345"
        )
        self.client.force_authenticate(self.user)

    def test_list_plays(self):
        sample_play()
        sample_play()
        play_with_actors = sample_play()
        play_with_genre = sample_play()

        actor1 = sample_actor()
        actor2 = sample_actor()

        play_with_actors.actors.add(actor1, actor2)

        genre = sample_genre()

        play_with_genre.genres.add(genre)

        res = self.client.get(PLAY_URL)

        plays = Play.objects.all()
        serializer = PlayListSerializer(plays, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["results"], serializer.data)

    def test_filter_play_by_title(self):
        play0 = sample_play()
        play1 = sample_play(title="Other")
        play2 = sample_play(title="New")

        response = self.client.get(PLAY_URL, {"title": f"{play1.title}"})

        serializer1 = PlayListSerializer(play0)
        serializer2 = PlayListSerializer(play1)
        serializer3 = PlayListSerializer(play2)

        self.assertNotIn(serializer1.data, response.data["results"])
        self.assertIn(serializer2.data, response.data["results"])
        self.assertNotIn(serializer3.data, response.data["results"])

    def test_filter_play_by_genres(self):
        play0 = sample_play()
        play1 = sample_play(title="Other")
        play2 = sample_play(title="New")

        genre1 = sample_genre()
        genre2 = sample_genre(name="Comedy")

        play1.genres.add(genre1)
        play2.genres.add(genre2)

        response = self.client.get(PLAY_URL, {"genres": f"{genre1.id},{genre2.id}"})

        serializer1 = PlayListSerializer(play0)
        serializer2 = PlayListSerializer(play1)
        serializer3 = PlayListSerializer(play2)

        self.assertNotIn(serializer1.data, response.data["results"])
        self.assertIn(serializer2.data, response.data["results"])
        self.assertIn(serializer3.data, response.data["results"])

    def test_filter_play_by_actor(self):
        play1 = sample_play(title="Other")
        play2 = sample_play(title="New")

        actor = sample_actor()

        play1.actors.add(actor)

        response = self.client.get(PLAY_URL, {"actors": f"{actor.id}"})

        serializer1 = PlayListSerializer(play1)
        serializer2 = PlayListSerializer(play2)

        self.assertIn(serializer1.data, response.data["results"])
        self.assertNotIn(serializer2.data, response.data["results"])

    def test_retrieve_play_detail(self):
        play = sample_play()
        actor = sample_actor()
        genre = sample_genre()

        play.actors.add(actor)
        play.genres.add(genre)

        url = detail_url(play.id)
        res = self.client.get(url)

        serializer = PlayDetailSerializer(play)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        print(res.data)
        self.assertEqual(res.data, serializer.data)

    def test_create_play_forbidden(self):
        payload = {
            "title": "Test Play",
            "description": "Test Description"
        }

        res = self.client.post(PLAY_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminPlayApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="testfortest@test.com",
            password="Test122345",
            is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_play(self):
        genre = sample_genre()

        actor = sample_actor()

        payload = {
            "title": "Test Play",
            "description": "Test Description",
            "genres": [genre.id],
            "actors": [actor.id]
        }

        res = self.client.post(PLAY_URL, payload)
        play = Play.objects.get(id=res.data["id"])
        genres = play.genres.all()
        actors = play.actors.all()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(genres.count(), 1)
        self.assertEqual(actors.count(), 1)
        self.assertIn(genre, genres)
        self.assertIn(actor, actors)

    def test_delete_play_not_allowed(self):
        play = sample_play()

        url = detail_url(play.id)

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
