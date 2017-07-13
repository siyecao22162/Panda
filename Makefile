# These targets are not files
.PHONY: install panda docs coverage lint messages compiledmessages css clean panda_image

install:
	pip install -r requirements.txt
	pip install panda/libs/django-oscar-paypal-0.9.7.tar.gz
	pip install -e .[test]

build_panda:
	# Remove media
	-rm -rf panda/public/media/images
	-rm -rf panda/public/media/cache
	-rm -rf panda/public/static
	-rm -f panda/db.sqlite
	# Create database
	panda/manage.py migrate
	# Import some fixtures. Order is important as JSON fixtures include primary keys
	panda/manage.py loaddata panda/fixtures/child_products.json panda/fixtures/partners.json
	#panda/manage.py oscar_import_catalogue panda/fixtures/*.csv
	panda/manage.py oscar_import_catalogue_images panda/fixtures/images1.tar.gz
	panda/manage.py oscar_import_catalogue_images panda/fixtures/images2.tar.gz
	panda/manage.py oscar_populate_countries --initial-only
	panda/manage.py loaddata panda/fixtures/pages.json panda/fixtures/auth.json panda/fixtures/vouchers.json panda/fixtures/offers.json
	panda/manage.py loaddata panda/fixtures/promotions.json
	#panda/manage.py loaddata panda/fixtures/orders.json
	panda/manage.py clear_index --noinput
	panda/manage.py update_index catalogue
	panda/manage.py thumbnail cleanup
	panda/manage.py collectstatic --noinput

panda: install build_panda

panda_image:
	docker build -t django-oscar-panda:latest .

docs:
	cd docs && make html

test:
	py.test 

coverage:
	py.test --cov=oscar --cov-report=term-missing

lint:
	flake8 src/oscar/
	isort -q --recursive --diff src/

testmigrations:
	pip install -r requirements_migrations.txt
	cd panda && ./test_migrations.sh

messages:
	# Create the .po files used for i18n
	cd src/oscar; django-admin.py makemessages -a

compiledmessages:
	# Compile the gettext files
	cd src/oscar; django-admin.py compilemessages

css:
	npm install
	npm run build

clean:
	# Remove files not in source control
	find . -type f -name "*.pyc" -delete
	find . -type f -name "__pycache__" -delete
	rm -rf nosetests.xml coverage.xml htmlcov *.egg-info *.pdf dist violations.txt

todo:
	# Look for areas of the code that need updating when some event has taken place (like 
	# Oscar dropping support for a Django version)
	-grep -rnH TODO *.txt
	-grep -rnH TODO src/oscar/apps/
	-grep -rnH "django.VERSION" src/oscar/apps


release: clean
	pip install twine wheel
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload -s dist/*
