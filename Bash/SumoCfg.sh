#!/bin/bash
echo '-----------------根据route文件生成配置文件---------------------'
text="<configuration>
<input>
<net-file value=\"${1}.net.xml\"/>
<route-files value=\"${1}.rou.xml\"/>
</input>
<time>
<begin value=\"${2}\"/>
<end value=\"${3}\"/>
</time>
</configuration>"

echo "$text" > ${1}.sumocfg
echo "Success."
