from rest_framework import viewsets, mixins
from core.models import Candidate
from candidate import serializers
import requests

# from drf_spectacular.utils import extend_schema_view, extend_schema


class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CandidateSerializer
    queryset = Candidate.objects.all()

    def get_queryset(self):
        queryset = self.queryset

        items = queryset.filter().order_by("id").distinct()
        # save db from github
        if len(items) == 0:
            try:
                r = requests.get(
                    "https://api.github.com/search/users?q=location:Turkey"
                )
                data = r.json()

                for user in data["items"]:
                    url = "https://api.github.com/users/" + user["login"]
                    res = requests.get(url)

                    user_data = res.json()
                    name = user_data["name"]
                    website = user_data["blog"]
                    location = user_data["location"]
                    email = user_data["email"]
                    bio = user_data["bio"]
                    join_date = user_data["created_at"]
                    hireable = user_data["hireable"]
                    company = user_data["company"]

                    b = {
                        "name": name,
                        "username": user["login"],
                        "avatar_url": user["avatar_url"],
                        "github_url": user["html_url"],
                        "website": website,
                        "location": location,
                        "email": email,
                        "bio": bio,
                        "join_date": join_date,
                        "company": company,
                        "hireable": hireable,
                    }

                    serializer = serializers.CandidateSerializer(data=b)
                    serializer.is_valid(raise_exception=True)
                    self.perform_create(serializer)
                items = queryset.filter().order_by("id").distinct()
            except Exception as e:
                print(e)

        role = self.request.query_params.get("role")

        if role:
            items = queryset.filter(bio__icontains=role)

        return items

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.CandidateSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save()


class BaseCandidateViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
):
    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter().order_by("-name").distinct()

    def perform_create(self, serializer):
        serializer.save()


class Candidate(BaseCandidateViewSet):
    queryset = Candidate.objects.all()
    serializer_class = serializers.CandidateSerializer
