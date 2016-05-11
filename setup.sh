#!/bin/bash

docker-compose run web ./manage.py sync_cassandra
