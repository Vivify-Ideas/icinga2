#!/bin/sh
docker exec -it $(docker ps -aqf "name=icinga2_icinga2") bash -c "icinga2 object list | grep salt | grep -oP '\".*\"' | cut -c 2-33"

