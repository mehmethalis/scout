from django.test import TestCase
from core import models


class ModelTests(TestCase):
    # candidate

    def test_create_candidate_successful(self):
        name = "Halis"
        username = "mehmethalis"
        avatar_url = "https://avatars.githubusercontent.com/u/69078217?v=4"
        github_url = "https://github.com/mehmethalis"
        website = "https://haliscicek.com"
        location = "Turkey"
        email = ""
        bio = "Software Engineer"
        join_date = "2020-08-01T12:03:49Z"
        hireable = True
        company = ""

        candidate = models.Candidate.objects.create(
            name=name,
            username=username,
            avatar_url=avatar_url,
            github_url=github_url,
            website=website,
            location=location,
            email=email,
            bio=bio,
            join_date=join_date,
            hireable=hireable,
            company=company,
        )
        self.assertEqual(candidate.name, name)
        self.assertEqual(candidate.username, username)
        self.assertEqual(candidate.avatar_url, avatar_url)
        self.assertEqual(candidate.github_url, github_url)
        self.assertEqual(candidate.website, website)
        self.assertEqual(candidate.location, location)
        self.assertEqual(candidate.email, email)
        self.assertEqual(candidate.bio, bio)
        self.assertEqual(candidate.join_date, join_date)
        self.assertEqual(candidate.company, company)
        self.assertTrue(candidate.hireable)
