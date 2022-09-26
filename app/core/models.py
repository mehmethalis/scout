from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    avatar_url = models.CharField(max_length=100, blank=True)
    github_url = models.CharField(max_length=100)
    website = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True)
    bio = models.CharField(max_length=100)
    join_date = models.CharField(max_length=100)
    hireable = models.BooleanField(blank=True)
    company = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username
