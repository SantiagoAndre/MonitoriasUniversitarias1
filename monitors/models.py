from django.db import models

# Create your models here.

'''
# sistema para administración de monitores
# @MonitoriasUniversitarias

MONITOR: Hace parte de recursos humanos de la empresa, este se dedica a dar clase y a realizar trabajos
universitarios.
Se quiere almacenar la siguiente información:
    - Nombre
    - Correo
    - Número de teléfono
    - Dirección de residencia
    - Contacto de alguien cercano(Nombre y teléfono)
    - Datos de su Universidad:
        - Nombre
        - Carrera
        - Semestre(Puede ser egresado)
    - Lista de materias de acuerdo a su rama de  aprendizaje(carrera)
        Nota: Estas deben existir en el sistema. Ej: Matemáticas generales, Física de fluidos
        Si esta no existe el monitor debe llenar correspondientes de este tema para que sea revisado.

LÍNEA DE APRENDIZAJE: Equivalente a las lineas de aprendizaje de una carrera universitaria
    Ej: - Programación
        - Física
        - Matemáticas
        - Emprendimiento
    De esta forma se evita redundancia de temas en las líneas de aprendizaje
Se quiere almacenar la siguiente información:
    - Nombre
    - Descripción
    - Lista de Temas(Nombre, Descripción, Lista de Subtemas)
    Nota: La idea es que cada Materia, Tema, Subtema tenga un antecesor y un tema siguiente, en este sentido ningún tema
    queda en el aire, y todos  te llevan a entender temas cada vez más complejos
REGISTRO DE SERVICIOS DE LA EMPRESA: 
    - Clases: Fecha, Monitor, Duracion, Costo(Enlzado a un presupuesto)
    - Trabajos: Fecha, Monitor, Costo(Enlzado a un presupuesto), fecha de asignacion, fecha de entrega
EVALUACION DE SERVICIOS DE LA EMPRESA: 
    - Atencion al cliente
    - Monitor: Basandose en los aspectos importantes de nuestros servicios especificados en las guias.
    - Material
INGRESOS Y EGRESOS:
'''

# 
class College(models.Model):
    name =  models.CharField(max_length=200)
class CollegeCareer(models.Model):
    name =  models.CharField(max_length=200)
    description = models.CharField(max_length=201)
class Monitor(models.Model):
    name =  models.CharField(max_length=200)
    email =  models.CharField(max_length=200)
    phone = models.IntegerField()
    address =  models.CharField(max_length=200)
    family_phone = models.IntegerField()
    college =  models.ForeignKey(College, on_delete=models.CASCADE)
    career = models.ForeignKey(CollegeCareer, on_delete=models.CASCADE)
    semester = models.IntegerField()

class LearningLine(models.Model):
    name =  models.CharField(max_length=200)
    description = models.CharField(max_length=201)
    career = models.ForeignKey(CollegeCareer, on_delete=models.CASCADE)
    
class Topic(models.Model):
    name =  models.CharField(max_length=200)
    description = models.CharField(max_length=201)
    learning_line = models.ForeignKey(LearningLine, on_delete=models.CASCADE)

class Subtopic(models.Model):
    name =  models.CharField(max_length=200)
    description = models.CharField(max_length=201)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


class Service(models.Model):
    name =  models.CharField(max_length=200)
    description = models.CharField(max_length=201)

class Quotation(models.Model):
    '''
        Cotizacion por un servicio de la empresa
        la cotizacion es una lista de Actividades a realizar, o recursos utilizados 
        Al final es tendra un precio que puede ser precio por hora, precio total
        esta cotizacion puede ser aceptada o no por el cliente
        esta puede ser editada por monitores autorizados
    '''
    acepted = models.BooleanField(default=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    pass


class Poll(models.Model):
    '''
        Datos a evaluar de los servicios de la empresa:
        - Monitor
        - Atencion al cliente
        - Material
    '''
    quotation = models.OneToOneField(Quotation, on_delete=models.CASCADE)

    pass

## HACE FALTA LA PARTE DE INGRESOS Y EGRESOS
