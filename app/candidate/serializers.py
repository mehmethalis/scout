from rest_framework import serializers

from core.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = [
            "id",
            "name",
            "username",
            "avatar_url",
            "github_url",
            "website",
            "location",
            "email",
            "bio",
            "join_date",
            "hireable",
            "company",
        ]
        read_only_fields = ["id"]
