#!/bin/bash

set -e
set -u

function create_test_database() {
	local database=$1
	echo "Creating user and database '$database'"
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    	CREATE DATABASE $database;
    	GRANT ALL PRIVILEGES ON DATABASE $database TO $POSTGRES_USER;
	EOSQL
}

if [ -n "$POSTGRES_TEST_DATABASE" ]; then
	echo "Test database creation requested: $POSTGRES_TEST_DATABASE"
  create_test_database $POSTGRES_TEST_DATABASE
	echo "Test database created"
fi
