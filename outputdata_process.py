import pandas as pd
import os, sys
import traci;

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

outputDataPath = "/home/jasmine/PycharmProjects/SumoDataGenerator/OutputData/data"
inputDataPath = "/home/jasmine/PycharmProjects/SumoDataGenerator/InputData/data"
sumoBinary = "/usr/share/sumo/bin/sumo-gui"


def output_complete_trajectories(step):
    position_data = pd.DataFrame(
        columns=['simu_time', 'car_num', 'x_position', 'y_position',
                 'speed(m/s)',  'roadID', 'LaneID', 'Lane_index', 'lane_position'], dtype=float)

    # 获取车辆ID
    all_vehicle_id = traci.vehicle.getIDList()
    # print(type(all_vehicle_id))
    n = 0
    # 获取车辆位置
    for i in all_vehicle_id:
        all_vehicle_position = traci.vehicle.getPosition(i)

        get_speed = traci.vehicle.getSpeed(i)

        get_roadID = traci.vehicle.getRoadID(i)
        get_laneID = traci.vehicle.getLaneID(i)

        get_lane_index = traci.vehicle.getLaneIndex(i)
        get_lane_position = traci.vehicle.getLanePosition(i)

        # print(i)
        # print(all_vehicle_id[n])
        position_data.loc[n] = [step, all_vehicle_id[n], all_vehicle_position[0], all_vehicle_position[1],
                                get_speed, get_roadID, get_laneID, get_lane_index, get_lane_position]
        n += 1
    return position_data

def output_car_neighbors(step):
    position_data = pd.DataFrame(
        columns=['simu_time', 'car_num', 'x_position', 'y_position',
                 'neighbors_id'], dtype=float)

    # 获取车辆ID
    all_vehicle_id = traci.vehicle.getIDList()
    # print(type(all_vehicle_id))
    n = 0
    max_neighbors_distance = 30
    # 获取车辆位置
    for i in all_vehicle_id:
        #计算当前车辆位置
        cur_vehicle_position = traci.vehicle.getPosition(i)

        #计算近邻车辆j
        cur_vehicle_neighbors = []
        for j in all_vehicle_id:
            if j != i:
                another_vehicle_position = traci.vehicle.getPosition(j)
                max_distance = max(abs(cur_vehicle_position[0] - another_vehicle_position[0]),
                                   abs(cur_vehicle_position[1] - another_vehicle_position[1]))
                if max_distance <= max_neighbors_distance:
                    cur_vehicle_neighbors.append(j)

        length = len(cur_vehicle_neighbors)
        if length != 0:
            print(cur_vehicle_neighbors)
            for m in range(0,length):
                print(cur_vehicle_neighbors[m])
                position_data.loc[n] = [step, i, cur_vehicle_position[0], cur_vehicle_position[1],
                                        cur_vehicle_neighbors[m]]
                n += 1
    return position_data

def traci_control_env_update(step_time,sumoCmd):
    # ----开始---

    traci.start(sumoCmd)

    # 仿真延迟

    for step in range(0, step_time):

        # 步长控制
        traci.simulationStep(step + 1)

        if step == 0:
            output_data1 = output_complete_trajectories(step)
            output_data2 = output_car_neighbors(step)

        else:
            output_data1 = pd.concat([output_data1, output_complete_trajectories(step)], axis=0,
                                     ignore_index=True)
            output_data2 = pd.concat([output_data2, output_car_neighbors(step)], axis=0,
                                     ignore_index=True)


    traci.close(wait=True)
    return output_data1,output_data2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    N_STATES = 36000
    data_version = 2
    sumoCmd = [sumoBinary, "-c", inputDataPath + str(data_version) +"/data" + str(data_version) + ".sumocfg"]
    print(sumoCmd)

    print('------------------------------------------------')
    a = traci_control_env_update(N_STATES,sumoCmd)
    try:
        a[0].to_csv(outputDataPath + str(data_version) + "/trajectory" + ".csv")
    except:
        os.makedirs(outputDataPath + str(data_version))
        a[0].to_csv(outputDataPath + str(data_version) + "/trajectory" + ".csv")

    try:
        a[1].to_csv(outputDataPath + str(data_version) + "/neighbors" + ".csv")
    except:
        os.makedirs(outputDataPath + str(data_version))
        a[1].to_csv(outputDataPath + str(data_version) + "/neighbors" + ".csv")


    print('--------------------END----------------------------')