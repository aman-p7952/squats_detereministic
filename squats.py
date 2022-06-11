#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 11:09:35 2022

@author: aman
"""
import numpy as np
import json
with open('frame/frames.json', 'r') as f:
  data = json.load(f)
prv_state=0
state=0
count=0
def angle(frame,p1,p2,p3):
    a_x= frame[p1*2+0]
    a_y= frame[p1*2+1]
    b_x= frame[p2*2+0]
    b_y= frame[p2*2+1]
    c_x= frame[p3*2+0]
    c_y= frame[p3*2+1]
    a=np.array([a_x,a_y])
    b=np.array([b_x,b_y])
    c=np.array([c_x,c_y])
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle1 = np.arccos(cosine_angle)
    return np.degrees(angle1)
def knee_position(frame):
    left_knee_y=frame[13*2+1] #13
    right_knee_y=frame[14*2+1] #14
    left_ankle_y=frame[15*2+1] #15
    leg_height=left_ankle_y-left_knee_y
    if abs(left_knee_y-right_knee_y)<0.5*leg_height:
        return True
    else:
        return False
th=150
for frame in data:
    angle_lk=angle(frame,11,13,15,)
    angle_rk=angle(frame,12,14,16)
    angle_lh=angle(frame,5,11,13)
    angle_rh=angle(frame,6,12,14)
    # print (angle_lk,end=" ")
    # if angle_lk>110 and angle_rk>110 and angle_lh>100 and angle_rh>100 and knee_position(frame):
    if angle_lk>th and angle_rk>th and angle_lh>th and angle_rh>th and knee_position(frame):
         state=0
    # elif angle_rh<100 and angle_lh<100 and angle_rk<100 and angle_lh<100 and knee_position(frame):
    elif angle_rh<th and angle_lh<th and angle_rk<th and angle_lh<th and knee_position(frame):
         state=1
    if prv_state==1 and state== 0:
        count+=1
    prv_state=state
    # print(state,end=" ")
print(count)
