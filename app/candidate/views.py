from rest_framework import viewsets
from core.models import Candidate
from candidate import serializers


class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CandidateSerializer
    queryset = Candidate.objects.all()

    def get_queryset(self):
        # payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

        # r = requests.get("https://jsonplaceholder.typicode.com/posts")
        # print(r.text)
        return super().get_queryset().filter().order_by("-id")

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.CandidateSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save()
