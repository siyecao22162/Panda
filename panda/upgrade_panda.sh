#!/bin/bash

set -x
cd ~/Panda
git reset --hard
git pull
cd
mv webapps/django/panda backups/panda.`date +%Y%m%d%H%M%S`
cp -rf Panda webapps/django/panda
cd webapps/django/panda/
. ../env/bin/activate
make panda

/home/nkannielai/webapps/django/apache2/bin/stop
sleep 2
/home/nkannielai/webapps/django/apache2/bin/start

