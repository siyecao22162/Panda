#!/bin/bash

# set echo
set -x

# pull from git
cd ~/Panda
git reset --hard
git pull

# backup old files and put new files
cd
cp webapps/django/panda/panda/db.sqlite .
mv webapps/django/panda backups/panda.`date +%Y%m%d%H%M%S`
cp -rf Panda webapps/django/panda
cp db.sqlite webapps/django/panda/panda/

# start make
cd webapps/django/panda/
. ../env/bin/activate
make install
panda/manage.py makemigrations
panda/manage.py migrate
panda/manage.py collectstatic --noinput

# restart apache2
/home/nkannielai/webapps/django/apache2/bin/stop
sleep 2
/home/nkannielai/webapps/django/apache2/bin/start

