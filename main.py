# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import time
from collections import defaultdict

inputPath = "/home/jasmine/PycharmProjects/SumoDataGenerator/OutputData/data"
# 容许误差范围
time_tolerate = 10  # unit : S
position_tolerate = 1  # unit:m

def read_inputdata(file):
    output_data = []
    with open(file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # 跳过头部（列名）行
        for row in reader:
            data = []
            for tup in row:
                data.append(float(tup))
            output_data.append(data)
    return output_data

def gride_index(input_data, start_time, end_time, x, y):
    # 定义网格索引的网格大小（可根据具体需求进行调整）
    GRID_SIZE = 200  # 网格大小为10单位

    # 定义网格索引字典
    grid_index = defaultdict(list)

    for row in input_data:
        x_position = float(row[3])
        y_position = float(row[4])

        # 计算当前位置所在网格的索引
        grid_x = int(x_position // GRID_SIZE)
        grid_y = int(y_position // GRID_SIZE)

        # 将当前行数据添加到对应的网格索引中
        grid_index[(grid_x, grid_y)].append(row)

    # 根据时间和位置范围查找数据
    min_time = start_time - time_tolerate
    max_time = end_time + time_tolerate
    min_x = x - position_tolerate
    max_x = x + position_tolerate
    min_y = y - position_tolerate
    max_y = y + position_tolerate

    # 计算范围所涵盖的网格索引
    min_grid_x = int(min_x // GRID_SIZE)
    max_grid_x = int(max_x // GRID_SIZE)
    min_grid_y = int(min_y // GRID_SIZE)
    max_grid_y = int(max_y // GRID_SIZE)

    # 在范围内的网格中查找符合条件的数据
    target_data = []
    for grid_x in range(min_grid_x, max_grid_x + 1):
        for grid_y in range(min_grid_y, max_grid_y + 1):
            grid_key = (grid_x, grid_y)
            target_data.extend(grid_index[grid_key])

    # 过滤符合时间和位置范围的数据
    output_rows = []
    output_set = set()
    start = time.time()
    for row in input_data:
        if min_time < row[1] < max_time and min_x < row[3] < max_x and min_y < row[4] < max_y:
            output_rows.append(row)
            output_set.add(row[5])
    print((time.time() - start) * 1000)


    # 打印结果
    # for data in output_rows:
    #     print(f"row_id: {data[0]}, simu_time: {data[1]}, x_position: {data[2]}, y_position: {data[3]}")
    print(output_set)


def base_line(input_data, start_time, end_time, x_position, y_position):

    # 根据时间和位置范围查找数据
    min_time = start_time - time_tolerate
    max_time = end_time + time_tolerate
    min_x = x_position - position_tolerate
    max_x = x_position + position_tolerate
    min_y = y_position - position_tolerate
    max_y = y_position + position_tolerate

    output_rows = []
    output_set = set()
    start = time.time()
    for row in input_data:
        if min_time < row[1] < max_time and min_x < row[3] < max_x and min_y < row[4] < max_y:
            output_rows.append(row)
            output_set.add(row[5])
    print((time.time() - start) * 1000)


    # # 打印符合条件的数据行
    # for row in output_rows:
    #     print(row)
    print(output_set)


def ground_truth():
    input_file = inputPath+ str(data_version) +'/groundtruth.csv'

    output_data = []
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # 跳过头部（列名）行
        row = next(reader)
        output_data.append( float(row[1]))  # 提取第2到第4列数据
        output_data.append( float(row[2]))  # 提取第2到第4列数据
        output_data.append( float(row[3]))  # 提取第2到第4列数据
        output_data.append( float(row[4]))  # 提取第2到第4列数据
        print(output_data)
    return output_data

if __name__ == '__main__':
    data_version = 1
    input_file = inputPath + str(data_version) + '/neighbors.csv'
    input_data = read_inputdata(input_file)

    target = ground_truth()
    x_position = target[0]
    y_position = target[1]
    start_time = target[2]
    end_time = target[3]

    base_line(input_data, start_time, end_time,  x_position, y_position)
    gride_index( input_data,start_time , end_time,  x_position, y_position)