#-*-coding:utf-8 -*-
#获取公会直播的直播时长
# author by jack.hou
import os
import re
dir_path =r"E:\西凌主播4-28"
zb_time =[]
for root ,dirs,files in os.walk(dir_path,topdown=False):
    for name in files:
        # print(os.path.join(root,name)) #返回文件的绝对路径
        if name.endswith('.txt'):
            file_abs_path = os.path.join(root,name) #返回.txt文件的绝对路径
            with open(file_abs_path,'r') as f:
                zb_name = file_abs_path.split("\\")[2]  # 返回主播名字
                item = f.read()  #返回记录内容
                if item is not None:
                    zb_bf_time = re.findall('\d+',item)[0] #返回主播播放时长
                zb_time.append("{0}:{1}".format(zb_name,zb_bf_time))

#把主播名字和播放时长写到文件中
with open('zb_time.txt','w',encoding='utf-8') as f:
    for item in zb_time:
        f.write(item+'\n')



    #
    # for name in dirs:
    #     print(os.path.join(root,name)) #返回目录的绝对路径
    #     print(name)



