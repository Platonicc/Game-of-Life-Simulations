"""
Stimulation of 'THE GAME OF LIFE' altered with a single rule (If a cell has 2 active neightbour cells, it becomes active)
Version : 1.0
Author: Aman Kumar Nirala | [Github: amannirala13] ~ [LinkedIn: amannirala13] ~ [Instagram: amannirala13]
"""

#importing libraries
import copy
import os
import time
from termcolor import colored as color

#Declearing env variables
env = [[]]
env_temp = [[]]
clear = lambda: os.system('cls')

#input the dimentions of the environment
env_len = int(input("Enter the length of the environment: "))
env_wid = int(input("Enter the width of the environment: "))

'''
-----------------------------------------------------------------
                     FUNCTIONS                           
-----------------------------------------------------------------
'''

#Init the environment with '0's
def initEnv():
    for i in range (0,env_wid):
        env.append([0])
    for i in range (0,env_wid):
        for j in range (0,env_len):
            env[i].append(0)

#Preparing the environment for the stimulation cycles
def prepareEnv():
    while True:
        print()
        xInput = int(input("[Enter -1 to start stimulation]\nEnter x coordinate: "))
        if xInput >= env_len or xInput < 0:
            break
        yInput = int(input("Enter y coordinate: "))
        if yInput >= env_wid or yInput < 0:
            break
        env[yInput][xInput] = 1
        refreshEnv()

#Calculates activated neighbour cells of the cell at the particular coordinates
def totalActiveNeighbours (x, y):
    activeCells = 0
    if(x == 0):
        xLower = x
    else:
        xLower = x-1
    if(x == env_len-1):
        xUpper = x
    else:
        xUpper = x+1

    if(y == 0):
        yLower = y
    else:
        yLower = y-1
    if(y == env_wid-1):
        yUpper = y
    else:
        yUpper = y+1

    for x_cur in range (xLower, xUpper+1):
        for y_cur in range (yLower, yUpper+1):
            if(x_cur != x or y_cur != y):
                if(env[y_cur][x_cur]==1):
                    activeCells+=1
    
    return activeCells



#Starts stimulation
def startStimulation():
    while True:
        time.sleep(0.2)
        global env
        env_temp = copy.deepcopy(env)
        for current_col in range (0, env_wid):
            for current_row in range (0, env_len):
                total_active_neighbour_cells = totalActiveNeighbours(current_row, current_col)
                
                if (total_active_neighbour_cells <= 1):
                    env_temp[current_col][current_row]=0
                if(total_active_neighbour_cells >= 4):
                    env_temp[current_col][current_row]=0
                if (total_active_neighbour_cells == 3):
                    env_temp[current_col][current_row]=1
                if (total_active_neighbour_cells == 2):
                    env_temp[current_col][current_row]=1
        env = copy.deepcopy(env_temp)
        refreshEnv()

#Refreshing environment in the terminal
def refreshEnv():
        clear()
        for i in range (0,env_wid):
            for j in range (0, env_len):
                if(env[i][j]==1):
                    print(color(env[i][j], 'red','on_red'), " ", end = '')
                else:
                    print(color(env[i][j], 'white', 'on_white'), " ", end = '')
            print("\n")
        

'''
-----------------------------------------------------------------
                        MAIN                      
-----------------------------------------------------------------
'''

initEnv()
refreshEnv()
prepareEnv()
startStimulation()
input("Stimulation ends")