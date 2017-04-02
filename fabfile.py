from fabric.api import *

env.hosts = [
    '117.239.246.58',
]
env.user = "root"

def hack_db():
    with prefix('source /home/ubuntu/hackathon/hack_env/bin/activate'):
        with cd('/home/ubuntu/hackathon/hackathon_backend'):
            run('git pull')
            run('pip install -r requirements.txt')
            run('python3 manage.py collectstatic')
            run('python3 manage.py makemigrations')
            run('service apache2 restart')