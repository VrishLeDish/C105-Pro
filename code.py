import os
import cv2 #pip  install opencv-python
path = "C:/Users/vrish_fl8o8kc/Downloads/Python Projects/105-Video Album/Images/PRO-C105-Project-Images-main/Images"

Images = []

for file in os.listdir(path):
    name , ext = os.path.splitext(file)
    

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']: #image extentions
        file_name = path+"/"+file

print(file_name)

Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])
width,height,channels = frame.shape
size = (width,height) #tuple
#print(size)

out = cv2.VideoWriter("FriendsVideo.mp4",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(count-1,0,-1):
    frame = cv2.imread(Images[i])
    out.write(frame)
out.release()
print("Done")