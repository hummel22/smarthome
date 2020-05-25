#!/bin/bash

source ./.env

docker-compose -H tcp://server:2375 -f ./docker-compose-server.yml up -d