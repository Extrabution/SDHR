#! /usr/bin/bash
docker-compose build  &&
cd ./services/manipulator &&
docker build -t manipulator:img .&&
cd ../sensor &&
docker build -t sensor:img .