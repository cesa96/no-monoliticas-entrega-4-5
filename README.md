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

### Conclusiones

### Actividades desarrolladas

| Actividades | Integrantes |
|--------------|--------------|
| Diseño de los experimentos | Jorge Cardona, Andrés Pérez |
| Desarrollo de los microservicios | Cesar García, Andrés Pérez |
| Desarrollo de experimentos | César García, Jorge Cardona |
| Análisis de resultados | Jorge Cardona, Andrés Pérez, César García |

**Nota:** *Debido a restricciones temporales y de recursos, hemos llevado a cabo este ejercicio en una sesión sincrónica de Pair Programming. Dada la considerable cantidad de contenido que requería revisión, se aprovecharon los conocimientos individuales de cada participante para maximizar la eficiencia y la calidad del trabajo realizado*
