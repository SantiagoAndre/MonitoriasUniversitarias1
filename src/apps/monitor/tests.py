from django.test import TestCase
from .models import Monitor
from apps.learning_graph.models import Subject
from .errors import ValidationError
# Create your tests here.


class MonitorTest(TestCase):
    def setUp(self):
        self.name1 = "Test                                                  "
        self.name2 = "Test............................................................"
        self.name3 = "test test test test< test test test test test test test test test test test"
        self.email = "email@domain.com"
        self.career = "Ing Sistemas"
        self.college = "unicauca"
        self.residence = "popayan"
        self.level_education = "universitario"
        self.username = self.email

    def test_name(self):
        with self.assertRaises(ValidationError):
            m = Monitor(username=self.username,
                        first_name="self.name1", college=None, email=self.name1,
                        residence=self.name3, level_education=self.level_education,
                        college_career=self.career,last_name="TestName"
                        )
            m.save()

