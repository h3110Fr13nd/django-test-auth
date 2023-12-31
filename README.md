# django-test-auth


### Setup and Installation

##### Prerequisites

- python3.7 or higher

##### Setup

1. Install the requirements
   1. ```
      pip install -r requirements.txt

      ```
2. Make migrations
   1. ```
      python manage.py makemigrations
      python manage.py migrate

      ```
3. Create a SuperUser
   1. ```
      python manage.py createsuperuser

      ```
4. RunServer
   1. ```
      python managepy runserver

      ```
   2. Go to ``http://localhost:8000/admin``
   3. Add some services and Users
5. Use the Following apis to Perform CRUD operations


## Created a Model Name Service

#### CRUD Operations APIs


Create a Service

```

http://localhost:8000/api/services/
Method Post
form data: 
 	- name
	- description
	- time (optional) (default = 2 months)
	- price 
	- discount


```


Get all Services

```

http://localhost:8000/api/services/
Method Get
```


Retrieve A Service

```

http://localhost:8000/api/services/1
Method Get
```


Update a Service

```

http://localhost:8000/api/services/1/
Method Put
form data: 
 	- name
	- description
	- time (optional) (default = 2 months)
	- price 
	- discount


```


Delete a Service

```

http://localhost:8000/api/services/1/
Method Delete
```


Get JWT Token

```
http://localhost:8000/api/token/
GET
```

Refresh The Token

```
http://localhost:8000/api/token/refresh/
POST
form data:
	- refresh : Access Token
```


Example View of authentication 

```
http://localhost:8000/api/user/
Method GET
Headers:
	- Bearer Token : <Access Token>
```
