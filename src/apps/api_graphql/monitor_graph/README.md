# Variables 
- firstName
- lastName
- email
- telephone 
- residence 
- levelEducation 
- college 
- collegeCareer
- experience 
- serviceType
- shortJob 
- subject 

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
    "subject":["U3ViamVjdE5vZGU6MQ==","U3ViamVjdE5vZGU6Mg==","U3ViamVjdE5vZGU6Mw=="]
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