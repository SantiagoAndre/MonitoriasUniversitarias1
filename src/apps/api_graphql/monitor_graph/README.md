# Variables 
- firstName: String
- lastName: String
- email: String
- telephone : String
- residence: String
- levelEducation: String
- college: String
- collegeCareer: String
- experience: String
- serviceType: Boolean
- shortJob: String
- subject: List(Type ID) Es una lista con los ID's de las áreas de conocimiento(Subjects)
- careerAverage: Float
- informaticTool: String

#### Nota
La variable 'subject' es una lista con los ID's de las áreas de conocimiento(Subjects).
por ejemplo:
```js
subject:["U3ViamVjdE5vZGU6MQ==","U3ViamVjdE5vZGU6Mg==","U3ViamVjdE5vZGU6Mw=="]
```

# Input
### Obligatorio
Las siguientes variables son requeridas en la base de datos
- firstName
- lastName
- email
- telephone
- residence
- levelEducation
- college
- collegeCareer
- subject: Es ina lista con los indices de las materias agregadas

### Opcionales
Las siguientes variables son opcionales, pueden o no pueden ir
- experience 
- serviceType: Boolean
- shortJob 
- careerAverage: Float

### Ejemplo
```json
{
  "input": {
    "firstName": "Aquiles",
    "lastName": "Bailo",
    "email": "AquilesBailo@gmail.co",
    "telephone": "1234567890",
    "residence": "Popayan Cauca",
    "levelEducation": "Universitario",
    "college": "Unicauca",
    "collegeCareer": "ing sistemas",
    "subject":["U3ViamVjdE5vZGU6MQ==","U3ViamVjdE5vZGU6Mg==","U3ViamVjdE5vZGU6Mw=="],
    
    //opcionales
    "experience" :"cinco años trabajando como profesor",
    "serviceType": ["Trabajos","tareas"],
    "shortJob": true,
    "careerAverage": 4.3,
    "informaticTool":"si"
  }
}
```

# Mutation
```graphql
mutation create($input: MonitorInput!){
createMonitor(input:$input){
    user{
      firstName
      lastName
      residence
      id
      levelEducation
    }
  }
}
```