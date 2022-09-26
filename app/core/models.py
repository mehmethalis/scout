from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    avatar_url = models.CharField(max_length=100, blank=True, null=True)
    github_url = models.CharField(max_length=100)
    website = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True, null=True)
    bio = models.CharField(max_length=250, blank=True, null=True)
    join_date = models.CharField(max_length=100)
    hireable = models.BooleanField(blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
