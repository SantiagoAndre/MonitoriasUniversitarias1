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

# Errores

### Caracteres especiales
- "Monitor: first name field contains Special Characters"
- "Monitor: last name field contains Special Characters"    
- "Monitor: telephone field contains Special Characters"
- "Monitor: residence field contains Special Characters"
- "Monitor: level education field contains Special Characters"
- "Monitor: college field contains Special Characters"    
- "Monitor: college career field contains Special Characters"
- "Monitor: experience field contains Special Characters"
- "Monitor: service type field contains Special Characters"

```json 
{
  "errors": [
    {
      "message": "Monitor: first name field contains Special Characters",
      "code": "ValidationError"
    }
  ],
  "data": {
    "createMonitor": null
  }
}
```
### errores del tamaño de las columnas

- "Monitor: telephone length cannot exceed  10" 
- "Monitor: residence length  cannot exceed  50"
- "Monitor: level education length cannot exceed  50"
- "Monitor: college length  cannot exceed  50" 
- "Monitor: college career length cannot exceed  50"
- "Monitor: experience length  cannot exceed  50" 
- "Monitor: service type length cannot exceed  60"

```json
{
  "errors": [
    {
      "message": "Monitor: telephone length cannot exceed  10",
      "code": "ValidationError"
    }
  ],
  "data": {
    "createMonitor": null
  }
}
```
### espacios nulos o en blanco

- "Monitor: telephone cannot be null or blank"
- "Monitor: residence cannot be null or blank"
- "Monitor: level education cannot be null or blank"
- "Monitor: college cannot be null or blank"
- "Monitor: college career cannot be null or blank"
- "Monitor: first_name cannot be null or blank"
- "Monitor: last name cannot be null or blank"
- "Monitor: email cannot be null or blank"
- "Monitor: service type cannot be null or blank"

```json
{
  "errors": [
    {
      "message": "Monitor: first_name cannot be null or blank",
      "code": "ValidationError"
    }
  ],
  "data": {
    "createMonitor": null
  }
}
```

### Query Monitors

```graphql
query {
  allMonitors(firstName:"pipe",email:"correo@dominio.co"){
    edges{
      node{
        firstName
        lastName
        email
        status
      }
    }
  }
}
```