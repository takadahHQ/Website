#!/bin/sh   
git pull origin master
source ~/env/bin/activate
pip install -r requirements.txt
# python3 remote.py makemigrations
# python3 remote.py migrate
# python3 remote.py collectstatic
sudo systemctl restart nginx
sudo systemctl restart gunicorn