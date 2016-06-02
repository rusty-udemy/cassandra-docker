#!/bin/bash

docker-compose run web ./manage.py sync_cassandra
docker-compose run web ./manage.py my_trial
