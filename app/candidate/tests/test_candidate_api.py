from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Candidate
from candidate.serializers import CandidateSerializer

CANDIDATE_URL = reverse("candidate:candidate-list")


def create_candidate(**params):
    defaults = {
        "name": "Halis",
        "username": "mehmethalis",
        "avatar_url": "https://avatars.githubusercontent.com/u/69078217?v=4",
        "github_url": "https://github.com/mehmethalis",
        "website": "https://haliscicek.com",
        "location": "Turkey",
        "email": "",
        "bio": "Software Engineer",
        "join_date": "2020-08-01T12:03:49Z",
        "hireable": True,
        "company": "",
    }
    defaults.update(params)
    candidate = Candidate.objects.create(**defaults)
    return candidate


class CandidateAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_candidates(self):
        create_candidate()

        res = self.client.get(CANDIDATE_URL)
        candidates = Candidate.objects.all().order_by("-id")
        serializer = CandidateSerializer(candidates, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_candidate(self):
        payload = {
            "name": "Halis",
            "username": "mehmethalis",
            "avatar_url": "https://avatars.githubusercontent.com/u/69078217?v=4",
            "github_url": "https://github.com/mehmethalis",
            "website": "https://haliscicek.com",
            "location": "Turkey",
            "email": "",
            "bio": "Software Engineer",
            "join_date": "2020-08-01T12:03:49Z",
            "hireable": True,
            "company": "",
        }
        res = self.client.post(CANDIDATE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        candidate = Candidate.objects.get(id=res.data["id"])
        for k, v in payload.items():
            self.assertEqual(getattr(candidate, k), v)
