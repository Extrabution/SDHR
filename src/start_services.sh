#! /usr/bin/bash
docker-compose up -d &&
docker run -d --name man01 manipulator:img &&
docker run -d --name sen01 sensor:img
docker run -d --name sen02 sensor:img
docker run -d --name sen03 sensor:img
docker run -d --name sen04 sensor:img
docker run -d --name sen05 sensor:img
docker run -d --name sen06 sensor:img
docker run -d --name sen07 sensor:img
docker run -d --name sen08 sensor:img