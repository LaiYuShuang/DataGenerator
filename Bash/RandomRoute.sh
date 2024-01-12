#!/bin/bash
#${1}: net文件的地址和文件名
#
#-e 2000：这个选项指定了生成的行程文件中的车辆数目。在这个例子中，生成了2000辆车的行程。
#
#-l：这个选项用于生成的行程文件中的车辆是否按照车道进行分组。当指定了该选项时，每个车道上的车辆将被分为不同的组。
#
#-L：这个选项用于生成的行程文件中的车辆是否按照车辆类型进行分组。当指定了该选项时，不同类型的车辆将被分为不同的组。
#
#--fringe-factor 10：这个选项指定了在生成的行程文件中车辆在起点和终点之间行驶的最大偏移量。这个值为10表示车辆可以在起点和终点之间的位置上有最多10米的随机偏移。
#
#--allow-fringe：这个选项指示生成的行程文件中的车辆是否允许在起点和终点之间行驶时超出道路网络的边界。

#<vType id="trashCar" color="red" vClass="truck" length="7.0" width="3.0" height="1.7"/>
#<vehicle id="72" type="trashCar" depart="72.00">
#<route edges="232317997#3.787 190236969#2 190236969#4 190236969#5 190236969#7 190236969#8"/>
#<stop lane="190236969#2_0" endPos="50" duration="120"/>
#</vehicle>

#-n data2.net.xml.gz：指定SUMO仿真网络的文件路径，这里的osm.net.xml.gz是网络文件的名称。
#
#--fringe-factor 10：设置边缘系数，用于控制车辆在网络边缘的生成密度。数值越大，边缘区域的车辆生成密度越高。
#
#--insertion-density 30：设置车辆生成的密度，表示在网络中每个时间步生成的车辆数量。
#
#-o osm.passenger.trips.xml：指定生成的车辆行程文件的输出路径和名称，这里的osm.passenger.trips.xml是行程文件的名称。
#
#-r osm.passenger.rou.xml：指定生成的车辆路由文件的输出路径和名称，这里的osm.passenger.rou.xml是路由文件的名称。
#
#-b 0：设置仿真开始的时间，这里的值为0，表示从仿真开始时刻开始生成车辆。
#
#-e 36000：设置仿真结束的时间，这里的值为36000，表示仿真持续10小时。
#
#--validate：在生成行程和路由文件之前，对网络进行验证，确保生成的行程和路由是合法的。
#
#--remove-loops：在生成路由文件时，删除可能存在的环路。
#
#--vehicle-class passenger：设置车辆的类型，这里设定为乘客车辆。
#
#--vclass passenger：设置车辆的类型，与上述的--vehicle-class参数具有相同的作用。
#
#--min-distance 300：设置车辆之间的最小间距，这里的值为300。
#
#--min-distance.fringe 10：设置边缘区域车辆之间的最小间距，这里的值为10。
#
#--allow-fringe.min-length 1000：设置边缘区域车辆的最小路径长度，这里的值为1000。
#
#--lanes：在生成路由文件时，将车辆限制在它们的初始车道上。

echo '-----------------根据net文件生成route文件---------------------'
#python ${SUMO_HOME}/tools/randomTrips.py -n  -r  -o  -e 2000 -l -L --fringe-factor 10 --allow-fringe
python ${SUMO_HOME}/tools/randomTrips.py -n ${1}.net.xml -r ${1}.rou.xml -o ${1}.trips.xml --insertion-density 5 -b 0 -e 36000 --fringe-factor 10 --allow-fringe --validate --remove-loops --vehicle-class passenger --vclass passenger --min-distance 300 --min-distance.fringe 10 --allow-fringe.min-length 1000 --lanes