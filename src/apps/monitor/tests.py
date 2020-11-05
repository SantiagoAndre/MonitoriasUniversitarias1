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
        self.sub = Subject(name="Test", description="test2")

    def test_username_long_length(self):
        try:
            m = Monitor(username=self.name3,
                        first_name="juanito", college=self.college, email=self.name1,
                        residence='self.name3', level_education=self.level_education,
                        college_career=self.career, last_name="TestName", telephone="31122323"
                        )
            m.save()
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_service_null(self):
        try:
            m = Monitor(username='self.name3',
                        first_name="juanito", college=self.college, email=self.email,
                        residence='self.name3', level_education=self.level_education,
                        college_career=self.career, last_name="TestName", telephone="31122323", service_type=None
                        )
            m.save()
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_experience_null(self):
        try:
            m = Monitor(username='self.name3',
                        first_name="juanito", college=self.college, email=self.email,
                        residence='self.name3', level_education=self.level_education,
                        college_career=self.career, last_name="TestName", telephone="31122323", service_type=None, experience=None
                        )
            m.save()
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_experience_blank(self):
        try:
            m = Monitor(username='self.name3',
                        first_name="juanito", college=self.college, email=self.email,
                        residence='self.name3', level_education=self.level_education,
                        college_career=self.career, last_name="TestName", telephone="31122323",
                        service_type=None, experience=""
                        )
            m.save()
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    def test_experience_specials_characters(self):
        try:
            m = Monitor(username='self.name3',
                        first_name="juanito", college=self.college, email=self.email,
                        residence='self.name3', level_education=self.level_education,
                        college_career=self.career, last_name="TestName", telephone="31122323",
                        service_type=None, experience="None <&&&.,qw>"
                        )
            m.save()
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_short_job_specials_characters(self):
        try:
            m = Monitor(username='self.name3',
                        first_name="juanito", college=self.college, email=self.email,
                        residence='self.name3', level_education=self.level_education,
                        college_career=self.career, last_name="TestName", telephone="31122323",
                        service_type=None, short_job="None <&&&.,qw>"
                        )
            m.save()
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_delete_subject(self):
        try:
            m = Monitor(username='self.name3',
                        first_name="juanito", college=self.college, email=self.email,
                        residence='self.name3', level_education=self.level_education,
                        college_career=self.career, last_name="TestName", telephone="31122323",
                        service_type=None, short_job=None
                        )
            m.save()
            s = self.sub.save()
            m.subject.add(s)
            for s in m.subject.all():
                s.delete()
            self.assertTrue(True)
        except:
            self.assertTrue(False)
