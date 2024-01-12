import subprocess

inputDataPath = "/home/jasmine/PycharmProjects/SumoDataGenerator/InputData/data"
bashPath = "/home/jasmine/PycharmProjects/SumoDataGenerator/Bash"

# python调用shell脚本
def call_shell_script(script_path, *args):
    command = ['bash', script_path] + list(args)
    subprocess.call(command)


# 处理input文件，得到数据集net文件
def net_generator(data_version):
    # 调用Shell脚本并传递参数
    call_shell_script(bashPath + '/NetConvert.sh', inputDataPath + str(data_version) + "/data" + str(data_version))


# 处理input文件，得到数据集rou文件
def route_generator(data_version):
    # 调用Shell脚本并传递参数
    call_shell_script(bashPath + '/RandomRoute.sh', inputDataPath + str(data_version) + "/data" + str(data_version))

#生成sumocfg文件
def sumocfg_generator(data_version):
    begin = 0
    end = 36000
    # 调用Shell脚本并传递参数
    call_shell_script(bashPath + '/SumoCfg.sh', inputDataPath + str(data_version) + "/data" + str(data_version), str(begin), str(end))

if __name__ == '__main__':
    data_version = 2;

    # 处理input data
    # net_generator(data_version)
    route_generator(data_version)
    sumocfg_generator(data_version)

    # 处理停止车辆