from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch("core.management.commands.wait_db.Command.check")
class CommandTests(SimpleTestCase):
    def test_wait_db_ready(self, patched_check):
        patched_check.return_value = True

        call_command("wait_db")
        patched_check.assert_called_once_with(databases=["default"])

    @patch("time.sleep")
    def test_wait_db_delay(self, patched_sleep, pathced_check):
        effect = [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]
        pathced_check.side_effect = effect

        call_command("wait_db")
        self.assertEqual(pathced_check.call_count, 6)
        pathced_check.assert_called_with(databases=["default"])
