#!/bin/bash

set -x
source /home/nkannielai/.bash_profile
. /home/nkannielai/webapps/django/env/bin/activate
/home/nkannielai/webapps/django/panda/panda/manage.py dbbackup
/home/nkannielai/webapps/django/panda/panda/manage.py mediabackup

date >> /home/nkannielai/webapps/django/backup_time.log

