# Init

## Start docker
Run docker desktop

### PROD

```
docker compose up -d
```

### DEV 
Open docker desktop, stop ONLY django web container, due to port :) 

#### Install packages
```
cd backend
python3 -m venv venv
pip install -r requerements.txt
```

#### run migrations and seed
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py seed_projects
```

#### 4. Open api, use api in app
Open `localhost:8000/api/projects`

