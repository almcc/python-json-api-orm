# Python JSON API ORM

## Library Goal

The goal of this library is to provide and ember-data style ORM for python applications. The plan is to develop it inline with the [rest\_framework\_ember](https://github.com/django-json-api/rest_framework_ember) django plugin.

## Getting Started

### Create Environemt

	virtualenv --no-site-packages python-json-api-orm
	cd python-json-api-orm
	source bin/activate

### Get the Code

	mkdir checkouts
	cd checkouts
	git clone git@github.com:almcc/python-json-api-orm.git
	cd python-json-api-orm

### Install the requirements

	pip install -r requirements.txt

### Deactivate Environemt

 	deactivate

## Create the example server database

	cd examples/server_alpha
	python manage.py syncdb --noinput
	python manage.py loaddata fixtures/*.json

*Note: The default user name and password is admin:admin*
