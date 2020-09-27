from django.test import TestCase

from .models import LearningLine, Subject

class LearningGraphTest(TestCase):

    def setUp(self):
        obj_test_one = LearningLine.objects.create(name="Pruebas de software", description="Descripcion para la linea de aprendizaje 'Pruebas de software'")
        obj_test_two = LearningLine.objects.create(name="Pruebas de software", description="Descripcion para la linea de aprendizaje 'Pruebas de software' (case two)")

        obj_test_three = Subject.objects.create(name="Tema 1", description="Descripción para tema 1", parent=None)
        obj_test_four = Subject.objects.create(name="Subtema 1 de Tema 1", description="Descripción para Subtema 1 de Tema 1", parent=obj_test_three)
        obj_test_five = Subject(name="Tema 2", description="Descripción para Tema 2", parent=None)
        obj_test_five.parent = obj_test_five
        obj_test_five.save()
    
    def test_name_unique(self):
        objects = LearningLine.objects.filter(name="Pruebas de software")
        self.assertEqual(len(objects), 1)
    
    def test_auto_parent(self):
        subjects = Subject.objects.all()
        bad_records = []
        for subject in subjects:
            if subject.id == subject.parent.id:
                bad_records.append(subject)
        self.assertEquals(len(bad_records), 0)


# * comando python manage.py test apps.learning_graph.tests

