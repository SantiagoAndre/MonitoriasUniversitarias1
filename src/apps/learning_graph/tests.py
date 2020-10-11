from django.test import TestCase

from .models import  Subject
from .errors import NameAlreadyUsedException,ParentSubjectNotFoundException,SubjectCircularRealtionException,MaxDeepSubjectException
from core.settings import MAX_DEEP_SUBJECT
'''
class LearningLineTest(TestCase):

    def setUp(self):
        self.same_name1 = "same  name"
        self.same_name2 = "    same name "
        obj_test_one = LearningLine.objects.create(name=self.same_name1, description="Descripcion para la linea de aprendizaje ")    
        
    def test_name_unique(self):
        with self.assertRaises(NameAlreadyUsedException):
            LearningLine.objects.create(name=self.same_name2, description="Descripcion para la linea de aprendizaje  (case two)")
'''            
class SubjectTest(TestCase):
    def setUp(self):
        self.same_name1 = "same  name"
        self.same_name2 = "    same name "
        #self.learningline1 = LearningLine.objects.create(name=" Pruebas de software ", description="Descripcion para la linea de aprendizaje ")
        
        self.subjectparent = Subject.objects.create(name=self.same_name1, description="Descripcion para la linea de aprendizaje s (case two)")
        self.subjectchild = Subject.objects.create(name="     Pruebas de software  2  ", description="Descripcion para la linea de aprendiza  (case two)",parent_id=self.subjectparent.id)
    def test_name_unique(self):
        self.subjectchild.description = "adasd as a ssas"
        self.subjectchild.save()
        with self.assertRaises(NameAlreadyUsedException):
            Subject.objects.create(name=self.same_name2, description="Descripcion para la linea de aprendizaje case two)")

    def test_auto_parent(self):
        with self.assertRaises(SubjectCircularRealtionException):
            self.subjectparent.parent_id=self.subjectchild.id
            self.subjectparent.save()
    def test_max_deep(self):
        parent = self.subjectchild
        for i in range(MAX_DEEP_SUBJECT-1):
            new_subject = Subject.objects.create(name="     Pruebas de software s   %d"%i, description="Descripcion para la linea de aprendizaje  (case two)",parent_id=parent.id)
            parent = new_subject
            
        with self.assertRaises(MaxDeepSubjectException):
            new_subject = Subject.objects.create(name="    sdf Pruebas de software    c", description="Descripcion para la linea de aprendizaje  (case two)",parent_id=parent.id)
# * comando python manage.py test apps.learning_graph.tests
