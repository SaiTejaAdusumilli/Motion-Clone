import shutil, os
arr = os.listdir('C:\\Users\\Asus\\Desktop\\pix2pix-tensorflow\\photos_pose_test\\result\\images')
s='C:\\Users\\Asus\\Desktop\\pix2pix-tensorflow\\photos_pose_test\\result\\images\\'
for i in arr:
    if('outputs' in i):
        f=(s+i)
        shutil.copy(f, 'C:\\Users\\Asus\\Desktop\\pix2pix-tensorflow\\photos_pose_test\\images')
    
