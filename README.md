# Data-Clean

deletepic：定义的函数同时删除imgs和segs文件夹图片

new_path：当前处理的被试文件夹路径

  首先显示被试文件夹中存在多个序列的情况
  
    该情况包括：绿幕图片、他人的非数据采集区域图片、被试正反面图片等
    
    ![image](https://user-images.githubusercontent.com/107409155/173396462-078ebd1f-d621-4f9a-8313-cf7358ccd863.png)

    
    通过缩略图查看数据，删除以上干扰文件
    
  其次通过查看序列图像确定需要保留的起始和终止帧图像，输入其文件名，进行删除
  
