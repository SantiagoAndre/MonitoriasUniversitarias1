from django.test import TestCase

from apps.learning_graph.models import Subject
from apps.learning_graph.errors import NameAlreadyUsedException, ParentSubjectNotFoundException, SubjectCircularRealtionException, MaxDeepSubjectException
from .schema import ROOT_SCHEMA
from .errors import CustomGraphQLView as GraphQLView
from core.settings import MAX_DEEP_SUBJECT


class SubjectTest(TestCase):
    def setUp(self):
        self.create_parent = """ 
        mutation createSubject{
              createSubject(input:{ name:" {name}",description:"U3ViamVjdE5vZGU6MTY"}){
                subject{
                id
                }
              } 
        }
        """
        self.create_child = """ 
        mutation createSubjectChild{
              createSubject(input:{ name:" {name}",description:"U3ViamVjdE5vZGU6MTY",parentId:"{parentId}"}){
                subject{
                id
                name
                 parent{
                    id
                    name
                }
                }
              } 
        }
        """
        self.edit_parent_subject = """
        mutation editSubject{
              editSubject(input:{id:"{id}", parentId:"{parentId}"}){
                subject{
                id
                }
              } 
        }
        """
        self.status_mutation = """
        mutation U{
            updateMonitor(input:{id:"TW9uaXRvck5vZGU6Mg==",status:"DISCARDED"}){
              monitor{
                id
                status
                lastName
              }
            }
          }
        """
        self.create_monitor = """
        mutation M2{
          createMonitor(input: {subject: ["U3ViamVjdE5vZGU6MQ=="]
            , collegeCareer: "dsfsdf",
            experience: "sss", firstName: "pipe",
            college: "Unicauca", email: "saramirez@unicauca.edu.co",
            residence: "dasdasd", levelEducation: "adasd",
            careerAverage: 0.3, lastName: "asdasd",
            telephone: "2323", shortJob: false,
            informaticTool: "Si",
            workHour: 2,
            serviceType:["Asesoria","Clases"]}) {
            user {
              status
              id
              firstName
            }
          }
        }
        """

    def test_name_unique(self):
        mutation = self.create_parent.replace("{name}", "nameee")
        ROOT_SCHEMA.execute(mutation)  # create first subject with name "namee"
        # create second subject with name "namee"
        result = ROOT_SCHEMA.execute(mutation)
        #print(dir(self))
        self.assertTrue(len(result.errors) != 0)

    def test_auto_parent(self):
        # 1 create parent
        create_parent = self.create_parent.replace("{name}", "nameee parent")
        result = ROOT_SCHEMA.execute(create_parent)
        parent = result.data['createSubject']['subject']
        # create child
        create_child = self.create_child.replace("{name}", "nameee child")
        create_child = create_child.replace("{parentId}", parent['id'])
        result = ROOT_SCHEMA.execute(create_child)
        # mutate parent
        child = result.data['createSubject']['subject']
        edit_parent_subject = self.edit_parent_subject.replace(
            "{id}", parent['id'])
        edit_parent_subject = edit_parent_subject.replace(
            "{parentId}", child['id'])
        result = ROOT_SCHEMA.execute(edit_parent_subject)
        # verify
        self.assertTrue(len(result.errors) != 0)

    def test_max_deep(self):
        # 1 create parent
        create_parent = self.create_parent.replace("{name}", "nameee parent")
        result = ROOT_SCHEMA.execute(create_parent)
        parent = result.data['createSubject']['subject']
        for i in range(MAX_DEEP_SUBJECT):
            create_child = self.create_child.replace(
                "{name}", "nameee child %d" % i)
            create_child = create_child.replace("{parentId}", parent['id'])
            result = ROOT_SCHEMA.execute(create_child)
            print(result)
            parent = result.data['createSubject']['subject']
        create_child = self.create_child.replace(
            "{name}", "nameee child %d" % (i+1))
        create_child = create_child.replace("{parentId}", parent['id'])
        result = ROOT_SCHEMA.execute(create_child)
        print(result)
        self.assertTrue(len(result.errors) != 0)
       # new_subject = Subject.objects.create(name="    sdf Pruebas de software    c", description="Descripcion para la linea de aprendizaje  (case two)",parent_id=parent.id)

    def test_create_monitor(self):
        result = ROOT_SCHEMA.execute(self.create_monitor)
        self.assertTrue(len(result.errors) != 0)

    def test_status_mutation(self):
        result = ROOT_SCHEMA.execute(self.create_monitor)
        self.assertTrue(len(result.errors) != 0)
