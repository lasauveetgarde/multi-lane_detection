#!/home/blackwidow/catkin_ws/src/multi_lane_detection/venv38/bin/python3 

import numpy as np
x = []
y = []
test_array = [ (145.0, 107), (145.0, 112), (145.0, 117), (145.0, 122), (145.0, 127), (145.0, 132),
                (145.0, 137), (145.0, 142), (145.0, 147), (145.0, 152), (145.0, 157), (145.0, 162),
                (145.0, 167), (145.0, 172), (145.0, 177), (145.0, 182), (145.0, 187), (145.0, 192),
                (145.0, 197), (145.0, 202), (145.0, 207), (145.0, 212), (145.0, 217), (145.0, 222),
                (145.0, 227), (145.0, 232), (145.0, 237), (145.0, 242), (145.0, 247), (145.0, 252),
                (145.0, 257), (145.0, 262), (145.0, 267), (145.0, 272), (145.0, 277), (145.0, 282),
                (145.0, 287), (145.0, 292), (145.0, 297), (145.0, 302), (145.0, 307), (145.0, 312)]
for i in range(len(test_array)-1):
    x.append(test_array[i][0])
    y.append(test_array[i][1])
    print(x,y)