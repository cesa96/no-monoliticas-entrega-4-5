# Protos

python -m grpc_tools.protoc -Iprotos --python_out=./pb2py --pyi_out=./pb2py --grpc_python_out=./pb2py protos/clientes.proto

# Ejecutar pulsar
docker-compose --profile pulsar up  

# Ejecutar db
docker-compose --profile db up  

# Ejecutar Cliente
python -m pip install PyMySQL
flask --app src/clientes/api run --port=5001


# Crear un cliente

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

# Consultar un cliente

curl --location --request GET 'http://127.0.0.1:5001/clientes/clientes/cecec011-4920-46a5-b3a9-663d0d960039' \
--header 'Content-Type: application/json' \


# Ejecutar Sidecar

python src/sidecar/main.py 

# Pruebas Sidecar

python src/sidecar/cliente.py 

# Ejecutaar inquilinos

flask --app src/inquilinos/api run --port=5002

# Crear inquilino

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

# Consultar inquilino

curl --location --request GET 'http://127.0.0.1:5002/inquilinos/inquilinos/b4cc1a49-ee4d-4f09-828b-97e0412c03c1' \
--header 'Content-Type: application/json' \


# Asociar Propiedades

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



# Ejecutar Sidecar

python src/sidecarInquilinos/main.py 

# Pruebas Sidecar

python src/sidecarInquilinos/cliente.py 

# Ejecutar Propiedades

flask --app src/propiedades/api run --port=5003

# Crear Propieadd

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

# Cosnultar propiedad

curl --location --request GET 'http://127.0.0.1:5003/propiedades/propiedades/b77544d4-a1d3-4240-8ab2-22e83ea2fa98' \
--header 'Content-Type: application/json' \

# Sidecar propiedad

python src/sidecarPropiedades/main.py 

# Pruebas Sidecar

python src/sidecarPropiedades/cliente.py 


# Ejecutar Saga

flask --app src/sagas/api run --port=5004

# Colección con el llamado a las sagas

EntregaFinal.postman_collection.json


