import os

# python manage.py dumpdata --format=json --indent=2 --exclude=sessions > inserts.json
# python manage.py shell -c "exec(open('teste.py').read())"

os.system('pip install -r start/requirements.txt')
os.system('python manage.py makemigrations JogoDoBicho')
os.system('python manage.py migrate')
#os.system('python manage.py createsuperuser')
#os.system('python manage.py shell -c "exec(open('"'start/config.py'"').read())"')
os.system('python manage.py loaddata inserts.json')
os.system('python manage.py runserver 0.0.0.0:80')