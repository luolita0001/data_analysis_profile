from collections import deque
from collections import namedtuple

ql = 1  # 晴朗
gw = 2  # 高温
sb = 3 #沙暴

def bfs(start_node, end_node, graph,wether,dayx,dayy):
    node = namedtuple('node', ['name', 'from_node'])
    search_stack = deque()  # 这里当作栈使用
    name_search = deque()
    visited = {}

    search_stack.append(node(start_node, None))
    name_search.append(start_node)
    path = []
    path_len = 0
    day = 0
    food = 0
    water = 0
    print('开始搜索...')
    while search_stack:
     print('待遍历节点: ', name_search)
     if weather[day] == 3:              #如果遇到沙暴天气则不能移动
           food += dayx[day]  # 当一个节点出来，遍历下一个节点的时候日期发生变化
           water += dayy[day]  # 消耗的水和食物总量都增加
           day += 1
           path.append('sb')
     else:
      current_node = search_stack.pop()
      name_search.pop()
                 #当一个节点出来，遍历下一个节点的时候日期发生变化
      food += dayx[day]
      water += dayy[day]         #消耗的水和食物总量都增加
      day += 1
     if current_node.name not in visited:
        print('当前节点: ', current_node.name, end=' | ')
        if current_node.name == end_node:
           pre_node = current_node
           while True:
                if pre_node.name == start_node:
                    path.append(start_node)
                    break
                else:
                    path.append(pre_node.name)
                    pre_node = visited[pre_node.from_node]
                path_len = len(path) - 1
           break
        else:
            visited[current_node.name] = current_node
            for node_name in graph[current_node.name]:
                if node_name not in name_search:
                    search_stack.append(node(node_name, current_node.name))
                    name_search.append(node_name)
    print('搜索完毕,路径为:', path[::-1], "长度为:", path_len,'消耗食物为:',food,'消耗水为:',water)  # 这里不再是最短路径，深度优先搜索无法一次给出最短路径


if __name__ == "__main__":

    graph = dict()    #使用字典表示有向图
    graph[1] = [2, 4, 5] 
    graph[2] = [3, 4]
    graph[3] = [4, 8, 9]
    graph[4] = [3, 6, 7]
    graph[5] = [4, 6]
    graph[6] = [7, 12, 13]
    graph[7] = [11, 12, 6]
    graph[8] = [9]
    graph[9] = [10, 11]
    graph[10] = [11, 13]
    graph[11] = [13]
    graph[12] = [11, 6]
    graph[13] = []
    dayx=[6, 18, 6, 6, 18, 6, 6, 18, 18, 18, 20, 20, 6, 6, 6, 18, 18, 18, 20, 18, 20, 6, 6, 18, 6, 20, 6, 18, 20, 18]
    dayy=[8, 18, 8, 8, 18, 8, 8, 18, 18, 18, 20, 20, 8, 8, 8, 18, 18, 18, 20, 18, 20, 8, 8, 18, 8, 20, 8, 18, 20, 18]
    weather = [3, 3, 1, 1, 1, 2, 2, 2, 3, 2, 3, 1, 1, 2, 1, 3, 1, 2, 3, 2, 3]

    bfs(1, 13, graph,weather[20],dayx[20],dayy[20]) 