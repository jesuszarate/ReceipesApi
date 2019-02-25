import os


os.system(
    'docker-compose run web python src/profiles_project/manage.py makemigrations')
os.system('docker-compose run web python src/profiles_project/manage.py migrate')
os.system('docker-compose up')
