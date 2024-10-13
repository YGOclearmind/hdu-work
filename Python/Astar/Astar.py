# 导入所需的库
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# 定义Node类，每个节点代表地图上的一个位置
class Node:
    def __init__(self, position, parent=None):  # 初始化节点，包括位置、父节点及初始费用
        self.position = position  # 当前节点的位置坐标
        self.parent = parent      # 父节点，用于构建最终路径
        self.g = 0               # 到达当前节点的实际成本
        self.h = 0               # 估计到目标的成本，即启发式函数值
        self.f = 0               # 总成本 = g + h
    
    def __eq__(self, other):     # 判断两个节点位置是否相等
        return self.position == other.position

# 定义启发式函数，使用曼哈顿距离
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # 计算两点之间的直线距离

# A*算法的主要执行函数
def astar(grid, start, end):
    open_list = []          # 开放列表，存储待评估的节点
    closed_list = []        # 封闭列表，存储已评估的节点

    start_node = Node(start)   # 创建起始节点
    end_node = Node(end)       # 创建目标节点

    # 将起始节点加入开放列表
    open_list.append(start_node)

    while open_list:          # 循环直到找到路径或者开放列表为空
        # 找出当前开放列表中f值最小的节点（即当前最佳选择）
        current_node = min(open_list, key=lambda node: node.f)

        if current_node == end_node:  # 如果到达目标，则构建并返回路径
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # 反转路径使得它从起点到终点

        # 移动当前节点到封闭列表
        open_list.remove(current_node)
        closed_list.append(current_node)

        # 检查所有邻居节点
        for move in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_position = (current_node.position[0] + move[0], current_node.position[1] + move[1])
            
            # 检查新位置是否合法（在地图内且无障碍）
            if not(0 <= new_position[0] < len(grid)) or not(0 <= new_position[1] < len(grid[0])) or grid[new_position[0]][new_position[1]]:
                continue
            
            new_node = Node(new_position, current_node)  # 创建邻居节点

            # 若邻居节点已在封闭列表，则跳过
            if new_node in closed_list:
                continue
            
            # 更新邻居节点的g、h、f值
            new_node.g = current_node.g + 1
            new_node.h = heuristic(new_node.position, end_node.position)
            new_node.f = new_node.g + new_node.h
            
            # 检查是否应该替换开放列表中的现有节点
            if add_to_open(open_list, new_node):
                open_list.append(new_node)

    # 未找到路径
    return None

def add_to_open(open_list, node):
    """确保新节点比开放列表中的旧节点更好"""
    for existing_node in open_list:
        if node == existing_node and node.g > existing_node.g:
            return False  # 不添加，因为已有更优解
    return True  # 添加到列表

# 绘制路径和地图的函数
def plot_path(grid, path):
    plt.imshow(grid, cmap='binary')  # 显示网格地图
    path_x, path_y = zip(*path)  # 提取路径的x和y坐标
    plt.plot(path_x, path_y, 'r-', linewidth=2)  # 绘制路径
    plt.plot(path[0][0], path[0][1], 'go')  # 起点绿色标记
    plt.plot(path[-1][0], path[-1][1], 'bo')  # 终点蓝色标记
    plt.show()  # 展示图形



# 运行A*算法
grid = np.zeros((20, 20))  # 10x10的空白地图
grid[5:7,5:7]=1
grid[11:14,11:14]=1



start = (0, 0)  # 起点坐标
end = (15, 12)   # 终点坐标
print(grid)
path = astar(grid, start, end)

# 根据结果绘制地图和路径
if path:
    plot_path(grid, path)
else:
    print("No path found")  # 输出无路径信息
