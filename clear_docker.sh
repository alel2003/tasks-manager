#!/bin/bash

echo "Удаление всех Docker-контейнеров..."
docker rm --force $(docker ps -aq)

echo "Удаление всех Docker-образов..."
docker rmi $(docker images -q)

echo "Удаление всех Docker-томов..."
docker volume rm $(docker volume ls -q)

echo "Очистка завершена."