### Setup 
Install dependencies
```bash
pip install -r requirements.txt`
```
Run migrations
```bash
python manage.py migrate
```
Run server
```bash
python manage.py runserver
```
Access doc at http://127.0.0.1:8000/redoc/

Run tests with
```bash
pytest
```

## Assumptions
1. There's only one pair of closest points for a given set of points
2. Point values are integers