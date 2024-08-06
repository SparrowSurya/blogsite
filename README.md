# Blogsite

# Setup (for me)
1. Clone the repository
```sh
git clone https://github.com/sparrowsurya/blogsite.git
```

2. Move into project folder
```sh
cd blogsite
```

3. Create virtual environment (virtualenv)
```sh
virtualenv venv
```

4. Activate virtual environment (linux)
```sh
source ./venv/bin/activate
```

5. Install project dependencies
```sh
python3 -m pip install -r requirements.txt
```

6. Create database and schemas
```sh
python3 manage.py migrate
```

7. Load fixtures (populate database table entries)
```sh
python3 manage.py loaddata fixtures/users.json
python3 manage.py loaddata fixtures/posts.json
python3 manage.py loaddata fixtures/comments.json
```

8. Run server
```sh
python3 manage.py runserver
```
