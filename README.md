# Data-Clean


![数据格式](https://user-images.githubusercontent.com/107409155/173545990-e02811bb-5132-4bfe-b081-367058e48bb4.png)

![image](https://user-images.githubusercontent.com/107409155/174745031-e734aa3f-e287-4c5e-8665-80e9ec380a72.png)


deletepic：定义的函数同时删除imgs和segs文件夹图片

new_path：当前处理的被试文件夹路径

  首先显示被试文件夹中存在多个序列的情况
  
    该情况包括：绿幕图片、他人的非数据采集区域图片、被试正反面图片等

    
    通过缩略图查看数据，删除以上干扰文件
    
  其次通过查看序列图像确定需要保留的起始和终止帧图像，输入其文件名，进行删除
  
![image](https://user-images.githubusercontent.com/107409155/174769269-c78b6e22-539c-42b1-b84a-2423c7f4d31a.png)

process：定义拆分序列正反面（面向，背向镜头）
  
path=new_path

angle_list=0-26（需要自己选择拆分的文件夹）

video_name：不同task的文件

front_start,front_end：正面起始和中止帧

back_start,back_end：背面起始和中止帧

![image](https://user-images.githubusercontent.com/107409155/176110834-689f7a7d-297a-4f74-a9fe-1b954952cef1.png)

# data_merge数据合并

输入所有文件的总目录

针对一个人的多个序列（一般多的话是两个）进行合并，综合成一个文件夹whole

#data_check数据检查

输入所有文件的总目录

将所有清洗好的数据文件夹内的RGB图片（imgs：前中后各5张）输出给用户检查，主要观察front和back文件是否拆分得当，以及绿幕图片等是否删除完全。

清洗完以后的最终数据格式

![image](https://user-images.githubusercontent.com/107409155/176111807-1f85cc5a-7d9e-49ed-95fb-71c06fae4446.png)
