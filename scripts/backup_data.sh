#!/bin/bash

set -x
source /home/nkannielai/.bash_profile
. /home/nkannielai/webapps/django/env/bin/activate

# For dbbackup's binary copy mode, need to cd to db.sqlite path
cd /home/nkannielai/webapps/django/panda/panda/

# Actual ./manage.py is also ok....
/home/nkannielai/webapps/django/panda/panda/manage.py dbbackup -s wb
/home/nkannielai/webapps/django/panda/panda/manage.py mediabackup -s wb

date >> /home/nkannielai/webapps/django/backup_time.log

