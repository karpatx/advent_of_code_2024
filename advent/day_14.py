from typing import List
from copy import deepcopy
from utils import read_data_file
from unicurses import *
from time import sleep

if __name__ == '__main__':

    #width = 11
    #height = 7
    width = 101
    height = 103

    list_of_robots = []
    original_file = read_data_file('../data/day_14/sample_data.txt')
    for line in original_file:
        splited = line.split('=')
        coords = splited[1].replace(' v', '').split(',')
        velocities = splited[2].split(',')
        list_of_robots.append({
            'p-x': int(coords[0]),
            'p-y': int(coords[1]),
            'v-x': int(velocities[0]),
            'v-y': int(velocities[1])
        })

    original_robots = deepcopy(list_of_robots)

    for steps in range(0, 100):
        for robot in list_of_robots:
            robot['p-x'] += robot['v-x']
            robot['p-y'] += robot['v-y']
            robot['p-x'] = robot['p-x'] % width
            robot['p-y'] = robot['p-y'] % height

    print(list_of_robots)

    all = 1
    for area in [(0,0,height//2,width//2), (0,width//2+1,height//2,width), (height//2+1,0,height,width//2), (height//2+1,width//2+1,height,width)]:
        print(area)
        counter = 0
        for robot in list_of_robots:
            print(robot['p-y'], robot['p-x'])
            if robot['p-y'] >= area[0] and robot['p-y'] < area[2] and robot['p-x'] >= area[1] and robot['p-x'] < area[3]:
                counter += 1
        print(counter)
        if counter != 0:
            all *= counter
    
    print(all)

    steps = 0
    while True:
        for robot in original_robots:
            robot['p-x'] += robot['v-x']
            robot['p-y'] += robot['v-y']
            robot['p-x'] = robot['p-x'] % width
            robot['p-y'] = robot['p-y'] % height
        sorted_robots = sorted(original_robots, key=lambda x: (x['p-y'], x['p-x']))
        counter = 0
        for r in range(0, len(sorted_robots) - 1):
            if sorted_robots[r]['p-y'] == sorted_robots[r+1]['p-y'] and abs(sorted_robots[r+1]['p-x']-sorted_robots[r]['p-x']) == 1:
                counter += 1
                if counter > 9:
                    initscr()
                    clear()
                    mvaddstr(0, 0, str(steps))
                    for robot in original_robots:
                        mvaddstr(robot['p-y']+1, robot['p-x'], '#')
                    refresh()
                    sleep(10.0)
                    endwin()        
            else:
                counter = 0
        steps += 1
        print(steps, end='\r')