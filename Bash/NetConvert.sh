#!/bin/bash
#${1}传入osm文件的地址和文件名
#
#--junctions.join：这个选项指示在转换过程中合并道路交叉口（junctions）。合并交叉口可以简化网络结构并减少节点数。
#
#--remove-edges.by-type railway.tram：这个选项指示通过类型删除具有"railway.tram"标签的边（edges）。这将从转换后的网络中删除轻轨电车轨道。
#
#--remove-edges.by-vclass hov,taxi,bus,delivery,transport,lightrail,cityrail,rail_slow,rail_fast,motorcycle,bicycle,pedestrian：这个选项指示通过车辆类型删除指定的边。在这个例子中，通过指定多个车辆类型，如高速公路车辆（hov）、出租车（taxi）、公交车（bus）等，将这些类型的边从转换后的网络中删除。
#
#--geometry.remove：这个选项指示在转换过程中删除几何信息。几何信息包括边的形状和长度等信息。
#
#--remove-edges.isolated：这个选项指示删除孤立的边。孤立的边是指与网络中其他边没有连接的边。
#
#--tls.join：这个选项指示在转换过程中合并信号灯（traffic light）。
#
#--tls.guess：这个选项指示在转换过程中猜测信号灯的控制方式。
#
#--verbose：这个选项指示在转换过程中显示详细的输出信息
echo '-----------------根据osm文件生成net文件---------------------'
netconvert --osm-files ${1}.osm --junctions.join --remove-edges.by-type railway.tram  --remove-edges.by-vclass hov,taxi,bus,delivery,transport,lightrail,cityrail,rail_slow,rail_fast,motorcycle,bicycle,pedestrian --geometry.remove --remove-edges.isolated --tls.join --tls.guess  --verbose -o ${1}.net.xml
#sumo-gui ${1}.sumocfg
