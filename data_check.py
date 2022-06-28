import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 检查所有imgs文件
path=r'D:\gait-depression\depression_4 - 副本'
#input your path
for iddir in os.listdir(path):
    new_path=os.path.join(path,iddir)
    for i in range(26):
        new_dirlist=os.listdir(os.path.join(new_path,str(i)))
        for new_dir in new_dirlist:
            
            new_seg_list=os.listdir(os.path.join(new_path,str(i),new_dir))
            if(len(new_seg_list)>1):
                
                for root,dirs,filenames in os.walk(os.path.join(new_path,str(i),new_dir)):
                    if('imgs' in root):
                        file_size=len(filenames)
                        plt.figure(root.split('depression_4')[-1][1:-5])
                        
                        filenames.sort()
                        # print(filenames)
                        if(len(filenames)<5):
                            print('path file is less than 5: ',root)
                        else:
                            mid=int(len(filenames)/2)
                            index_list=[0,1,2,3,4,mid-2,mid-1,mid,mid+1,mid+2,-5,-4,-3,-2,-1]
                            for j in range(1,16):
                                img=mpimg.imread(os.path.join(root,filenames[index_list[j-1]]))
                                plt.subplot(3,5,j)
                                plt.imshow(img)
                            # plt.title(root.split('depression_4')[-1][1:-5])
                            figManager = plt.get_current_fig_manager()
                            figManager.window.showMaximized()
                            plt.show()
                            
                print(str(i),new_dir,str(len(new_seg_list)))