# -*- coding: utf-8 -*-

import numpy as np
import csv
import cv2
import os

workspace = "./"
tmp_workspace = os.path.join(workspace,"slice_image/")

file_path = "data_sample.txt"
radar_echos = []
#这里取第三条数据为样本作出灰度图像
i = 0
with open(file_path,"r") as infile:
    for line in infile:
        i = i+1
        if i==3:
            context = line.split(",")
            #print context[0]
            radar_echos = context[2].split(" ")
            #print len(radar_echos)
            break

radar_np = np.array(radar_echos[0:10201])

#将np中的字符变为数字
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

new_radar_list = []

for e in radar_np:
    e = parse_maybe_int(e)
    new_radar_list.append(e)
#print new_radar_list[0:3]
new_radar_np = np.array(new_radar_list)

radar_map = new_radar_np.reshape(101,101)
print len(radar_map)

cv2.imwrite(os.path.join(tmp_workspace, "%04d_%04d_%04d_%s.jpg" % (0,0,0,1)),radar_map)
