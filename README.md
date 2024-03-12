# Protos
```
python -m grpc_tools.protoc -Iprotos --python_out=./pb2py --pyi_out=./pb2py --grpc_python_out=./pb2py protos/clientes.proto
```

# Ejecutar pulsar
```
docker-compose --profile pulsar up
```

# Ejecutar db
```
docker-compose --profile db up
```

# Ejecutar Cliente
```
python -m pip install PyMySQL
flask --app src/clientes/api run --port=5001
```

# Crear un cliente
```
curl --location 'http://127.0.0.1:5001/clientes/clientes' \
--header 'Content-Type: application/json' \

--data-raw '{
    "nombres" : "CESAR", 
    "apellidos" : "GARCIA",  
    "identificacion" : "13514130", 
    "fecha_nacimiento" : "1978-03-15",  
    "genero" : "MASCULINO",  
    "direccion" : "CLL",  
    "telefono" : "310",  
    "correo" : "cesa96@gmail.com", 
    "tipoCliente" : "NATURAL", 
    "sitioWeb" : "www.cesar.com"
}'
```

# Consultar un cliente
```
curl --location --request GET 'http://127.0.0.1:5001/clientes/clientes/cecec011-4920-46a5-b3a9-663d0d960039' \
--header 'Content-Type: application/json' \
```

# Ejecutar Sidecar
```
python src/sidecar/main.py
```

# Pruebas Sidecar
```
python src/sidecar/cliente.py
```

# Ejecutar inquilinos
```
flask --app src/inquilinos/api run --port=5002
```

# Crear inquilino

```
curl --location 'http://127.0.0.1:5002/inquilinos/inquilinos' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nombres" : "CESAR", 
    "apellidos" : "GARCIA",  
    "identificacion" : "13514130", 
    "fecha_nacimiento" : "1978-03-15",  
    "genero" : "MASCULINO",  
    "direccion" : "CLL",  
    "telefono" : "310",  
    "correo" : "cesa96@gmail.com", 
    "sitioWeb" : "www.cesar.com"
}'
```

# Consultar inquilino
```
curl --location --request GET 'http://127.0.0.1:5002/inquilinos/inquilinos/b4cc1a49-ee4d-4f09-828b-97e0412c03c1' \
--header 'Content-Type: application/json' \
```

# Asociar Propiedades
```
curl --location --request PUT 'http://127.0.0.1:5002/inquilinos/inquilinos/32fe678b-9212-440a-a35f-740b570f7131/asociar_propiedad/b4cc1a79-ee4d-4f09-828b-97e0412c0555' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nombres" : "CESAR", 
    "apellidos" : "GARCIA",  
    "identificacion" : "13514130", 
    "fecha_nacimiento" : "1978-03-15",  
    "genero" : "MASCULINO",  
    "direccion" : "CLL",  
    "telefono" : "310",  
    "correo" : "cesa96@gmail.com", 
    "tipoCliente" : "NATURAL", 
    "sitioWeb" : "www.cesar.com"
}'
```

# Ejecutar Sidecar
```
python src/sidecarInquilinos/main.py
```

# Pruebas Sidecar
```
python src/sidecarInquilinos/cliente.py
```

# Ejecutar Propiedades
```
flask --app src/propiedades/api run --port=5003
```

# Crear Propieadd

```
curl --location 'http://127.0.0.1:5003/propiedades/propiedades' \
--header 'Content-Type: application/json' \
--data '{
    "nombre" : "CESAR", 
    "descripcion" : "GARCIA",  
    "num_habitaciones" : 3, 
    "num_banos" : 2, 
    "fecha_construccion" : "1978-03-15",  
    "fecha_modernizacion" : "1978-03-15",  
    "disponible" : false,  
    "direccion" : "CLL",  
    "precio" : 310,  
    "metros_cuadrados" : 150, 
    "tipoPropiedad" : "CASA", 
    "servicios" : "muchos"
}'
```

# Consultar propiedad
```
curl --location --request GET 'http://127.0.0.1:5003/propiedades/propiedades/b77544d4-a1d3-4240-8ab2-22e83ea2fa98' \
--header 'Content-Type: application/json' \
```

# Sidecar propiedad
```
python src/sidecarPropiedades/main.py
```

# Pruebas Sidecar
```
python src/sidecarPropiedades/cliente.py
```

# Ejecutar Saga

```
flask --app src/sagas/api run --port=5004
```

# Colección con el llamado a las sagas

[EntregaFinal.json](https://github.com/cesa96/no-monoliticas-entrega-4-5/blob/main/colecciones/EntregaFinal.postman_collection.json)

# Entrega 4
Para esta entrega se desarrollaron tres experimentos, que nos permitieron validar los siguientes escenarios de calidad:

Escenario de calidad 1: Modificabilidad:
Descripción: Se agrega un nuevo módulo al sistema que interactúa y consume información de microservicios existentes.

Escenario de calidad 2: Escalabilidad:
Descripción: Aumento de la concurrencia de usuarios, debido a la inauguración de una nueva sucursal en otro país.

Escenario de calidad 3: Flexibilidad
Descripción: Mostrar datos uniformes a los usuarios, que cumplan con las necesidades e intereses de los mismos.

--------------

Durante la fase de desarrollo de nuestros experimentos, llevamos a cabo el diseño e implementación de diversos microservicios clave, entre ellos: clientes, inquilinos, y propiedades. Para facilitar la comunicación entre estos servicios, optamos por emplear comandos y eventos, siguiendo una arquitectura orientada a eventos, en la cual Apache Pulsar actúa como broker.

Con el objetivo de garantizar la escalabilidad del sistema, hemos incorporado conceptos como Seedworks y agregaciones en cada uno de los microservicios, aplicando inversiones de dependencias. Además, hemos aprovechado los Objetos valor para los atributos del microservicio de Clientes, los cuales serán utilizados en la agregación raíz del Cliente, contribuyendo así a la cohesión del diseño.

Para asegurar una correcta manipulación y transformación de los datos en el dominio, hemos introducido el concepto de Mapeadores. Estos permiten preparar los datos para su posterior compartición entre los distintos servicios.

En un nivel técnico más específico, hemos implementado el patrón Sidecar para cada uno de nuestros servicios. Este patrón, mediante el uso de protos, facilita la realización de mapeos, conexiones y esquemas de manera independiente a la aplicación principal. Asimismo, esta arquitectura nos brinda la flexibilidad necesaria para extender la funcionalidad de cada servicio sin generar acoplamiento entre ellos. Durante el despliegue, tanto la aplicación principal como el sidecar se integrarán dentro del mismo pod, simplificando así el proceso de gestión y mantenimiento.

Es importante destacar que hemos establecido un sistema de versionamiento para los esquemas, comandos y eventos, comenzando con la versión v1 en este caso específico. Esto nos permitirá gestionar de manera efectiva cualquier actualización o cambio futuro en nuestra arquitectura.

## Desiciones de diseño
### Tipos de eventos utilizados:
Durante el proceso de desarrollo de nuestros experimentos, hemos empleado una combinación de eventos de dominio y eventos de integración, así como la tecnología protobuf para facilitar la comunicación entre los distintos componentes del sistema.
Es importante mencionar que, a diferencia del enfoque de Event Sourcing, hemos optado por implementar un sistema CRUD (Crear, Leer, Actualizar y Eliminar). En este sistema, hemos modelado nuestras entidades utilizando tablas y atributos convencionales, lo que nos ha permitido gestionar los datos de manera más tradicional.

### Topologías de administración de datos
Se empleó una topología descentralizada, en la cual cada microservicio dispone de una base de datos dedicada, lo que posibilita la escalabilidad individual de cada uno. Esta configuración minimiza los riesgos asociados a la introducción de cambios, ya que cada equipo es responsable de su propia infraestructura.
Además, se adoptó el patrón CQRS (Command Query Responsibility Segregation), mediante el cual se segregan los comandos de las consultas. Esta estrategia no solo facilita la escalabilidad independiente, sino que también optimiza el rendimiento del sistema.

### Video demostración

[Video](https://uniandes-my.sharepoint.com/:v:/g/personal/aa_pereza1_uniandes_edu_co/Eb9CDIwlqEBBvFtIAsbVRyoB01ae3A7NulzdesiQry7C3Q?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=k2Sm8a)

### Actividades desarrolladas

| Actividades | Integrantes |
|--------------|--------------|
| Diseño de los experimentos | Jorge Cardona, Andrés Pérez |
| Desarrollo de los microservicios | Cesar García, Andrés Pérez |
| Desarrollo de experimentos | César García, Jorge Cardona |
| Análisis de resultados | Jorge Cardona, Andrés Pérez, César García |

# Entrega 5

En esta entrega se realizó la implementación de sagas para la orquestación de transacciones largas en un sistema compuesto por 4 microservicios, sin embargo al implementar la saga, solamente se tuvo en cuenta a Propiedades e Inquilinos. La arquitectura se basa en eventos y utiliza el patrón Saga para garantizar la consistencia en caso de fallos.

Se implementó un servicio de Sagas que actúa como BFF (Backend for Frontend) y coordina las sagas mediante Pulsar.

Se han implementado varios comandos, como la Creación y Eliminación de Propiedades, este último sirve como comando de Compensación en caso de errores. Se aplica el mismo funcionamiento en los Inquilinos. También se agregó un comando de asociación de propiedades a inquilinos, en este caso, no se requirió un evento de compensación separado, ya que en la base de datos la relación es en cascada, por lo que eliminar la propiedad, elimina automáticamente la asociación con el inquilino.
Esto se logró mediante atributos clave como ```id_cor``` en la tabla de Inquilinos, que identifica la saga, y en la tabla de Sagas, el id del inquilino y de la propiedad, con esto, se garantiza la actualización correcta de todas las tablas, ya sea en la ejecución correcta del proceso o en un evento de compensación.

### Conclusiones
Tras los experimentos realizados, se ha observado que la arquitectura basada en microservicios del sistema ha demostrado ser altamente modificable. La adición de un nuevo módulo que interactúa y consume información de los microservicios existentes se logró de manera eficiente y sin interrupciones significativas en el funcionamiento del sistema. Esto sugiere que la arquitectura está diseñada de manera modular y desacoplada, lo que facilita la incorporación de nuevos componentes sin afectar la integridad del sistema.
Se ha constatado que el sistema ha demostrado una capacidad adecuada para manejar el aumento de la concurrencia de usuarios. A pesar del incremento significativo en la carga de usuarios, el sistema pudo responder debido a la arquitectura basada en eventos, y el uso de CQRS para segregar las operaciones de lectura y escritura en la base de datos, así como el escalamiento individual del servicio al tener una base de datos dedicada para cada servicio. Esto indica que la arquitectura del sistema es escalable y puede adaptarse fácilmente a cambios en el volumen de usuarios sin comprometer el rendimiento. También se ha comprobado que el sistema puede proporcionar datos uniformes a los usuarios, adaptándose a sus necesidades e intereses de manera eficiente. La implementación de patrones como sidecar, la utilización de seedworks y de objetos DTO, ha permitido que el sistema se ajuste dinámicamente a las preferencias individuales de los usuarios. Esto sugiere que el sistema es flexible y puede adaptarse a diversas situaciones y requisitos cambiantes con facilidad.

### Video demostración

[Video](https://uniandes-my.sharepoint.com/:v:/g/personal/aa_pereza1_uniandes_edu_co/EXl7lmnuYtBJqL9DNNRs8EQBokXAH2o5FKqZzk90lH4LUg?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=ldxgYj)


**Nota:** *Debido a restricciones temporales y de recursos, hemos llevado a cabo este ejercicio en una sesión sincrónica de Pair Programming. Dada la considerable cantidad de contenido que requería revisión, se aprovecharon los conocimientos individuales de cada participante para maximizar la eficiencia y la calidad del trabajo realizado*


