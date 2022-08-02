CRUD API with PSQL
## ENGLISH ###
#Step 1: configure data such as domain name and trusted origins at settings.py

#Step 2: Deploy docker compose

docker-compose up --build -d

#Step 3: Apply migrations

-docker exec -it containerid python manage.py makemigrations 

-docker exec -it containerid python manage.py migrate --run-syncdb 

-docker exec -it containerid python manage.py createsuperuser 

#Step 4: Populate api with data at http://domain:8000.com/admin/



### SPANISH ###
#Paso 1: 
Configurar datos como el dominio en api/settings.py 

#Paso 2: Deploy de red de contenedores a través de docker compose

docker-compose up --build -d

#Paso 3:Aplicar migraciones

-docker exec -it containerid python manage.py makemigrations 

-docker exec -it containerid python manage.py migrate --run-syncdb 

-docker exec -it containerid python manage.py createsuperuser 

#Paso 4: Añadir data al api en http://domain.com/admin/


