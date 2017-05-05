# -*- coding: utf-8 -*-

import numpy as np
import csv
import cv2
import os

workspace = "./"
tmp_workspace = os.path.join(workspace,"slice_image/")

#将np中的字符变为数字
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)


file_path = "data_sample.txt"
radar_echos = []
#这里取第三条数据为样本作出灰度图像
i = 0
with open(file_path,"r") as infile:
    for line in infile:
        context = line.split(",")
        print context[0]
        radar_echos = context[2].split(" ")
        i = 0
        while i<612060:
            radar_np = np.array(radar_echos[i:i+10201])
            new_radar_list = []
            for e in radar_np:
                e = parse_maybe_int(e)
                new_radar_list.append(e)
            new_radar_np = np.array(new_radar_list)
            radar_map = new_radar_np.reshape(101,101)
            k = (i / 10201)
            #print k/4
            #print k%4
            cv2.imwrite(os.path.join(tmp_workspace, "%s_%s_%s_%s.jpg" % (context[0],context[1],k/4,k%4)),radar_map)
            i = i + 10201
        break
