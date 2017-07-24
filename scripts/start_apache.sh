#!/bin/bash

set -x
source ~/.bash_profile
env >~/webapps/django/env.txt
~/webapps/django/apache2/bin/start


