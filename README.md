# Data-Clean


![数据格式](https://user-images.githubusercontent.com/107409155/173545990-e02811bb-5132-4bfe-b081-367058e48bb4.png)

![image](https://user-images.githubusercontent.com/107409155/174744343-ba1efdcc-0eb2-405c-ae96-123c9bf75329.png)


deletepic：定义的函数同时删除imgs和segs文件夹图片

new_path：当前处理的被试文件夹路径

  首先显示被试文件夹中存在多个序列的情况
  
    该情况包括：绿幕图片、他人的非数据采集区域图片、被试正反面图片等

    
    通过缩略图查看数据，删除以上干扰文件
    
  其次通过查看序列图像确定需要保留的起始和终止帧图像，输入其文件名，进行删除
  
