#!/bin/bash
CURRENT_DIR=$(pwd)
echo ${1}
echo ${1}.osm
echo ${1}.net.xml
echo '-----------------根据net文件生成route文件---------------------'
#python ${SUMO_HOME}/tools/randomTrips.py -n ${1}.net.xml -r ${1}.rou.xml -o ${1}.trips.xml -e 2000 -l -L --fringe-factor 10 --allow-fringe
#
#python ${SUMO_HOME}/tools/randomTrips.py -n ${1}.net.xml -r ${1}test.rou.xml -e 1 --trip-attributes="departPos='random' duration='600'"
sumo-gui /home/jasmine/PycharmProjects/SumoDataGenerator/InputData/data2/data2.sumocfg
#python ${SUMO_HOME}/tools/randomTrips.py -n data2.net.xml.gz -r data.rou.xml -o
# data.trips.xml --insertion-density 30 -e 14400 --fringe-factor 10 --allow-fringe --validate --remove-loops --vehicle-class passenger --vclass passenger --min-distance 300 --min-distance.fringe 10 --allow-fringe.min-length 1000 --lanes