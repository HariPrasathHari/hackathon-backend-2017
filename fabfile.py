from fabric.api import *

def production():
    with prefix('source /home/ubuntu/hackathon/hack_env/bin/activate'):
        with cd('/home/ubuntu/hackathon/hackathon_backend'):
            run('git pull')
            run('pip install -r requirements.txt')
            run('python3 manage.py collectstatic')
            run('python3 manage.py makemigrations')
            run('service apache2 restart')