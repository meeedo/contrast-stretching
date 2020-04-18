import numpy as np
import cv2
import pylab as plt
import matplotlib.image as mpimg

# Load an color image in grayscale
imge = cv2.imread(r"C:\\Users\\A.N\\Desktop\\test.png",0)

x1 = np.min(imge)
x2 = np.max(imge)

y1 = input("enter the minimum of the new dynamic range : ")
y2 = input("enter the maximum of the new dynamic range : ")

index = len(imge[0])
oindex = len(imge)
size = index*oindex

myimage = cv2.imread(r"C:\\Users\\A.N\\Desktop\\test.png",0)
i = j = 0
for i in range(oindex):
    for j in range(index):
        myimage[i][j] = ((imge[i][j]-int(x1))*(((int(y2)-int(y1))/(int(x2)-int(x1)))+int(y1)))


fig = plt.figure()

# show original image
fig.add_subplot(221)
plt.title(' origenal')
plt.set_cmap('gray')
plt.imshow(imge)

fig.add_subplot(222)
plt.title('contrast stritching')
plt.set_cmap('gray')
plt.imshow(myimage)

cv2.imshow('origenal',imge)
cv2.imshow('contrast stritching',myimage)
cv2.waitKey(0)
cv2.destroyAllWindows()







##its the second way to make a contrast streching image 
#
#from PIL import Image
#import numpy as np
#from numpy import array
#
##from PIL import Image
#
#
#im_1 = Image.open(r"C:\Users\RS3\Desktop\test.png")
#
#ar = array(im_1)
#
#x1 = np.min(ar)
#x2 = np.max(ar)
#
#
#y1 = input("enter the minimum of the new dynamic range : ")
#y2 = input("enter the maximum of the new dynamic range : ")
#
#index = len(ar[0])
#oindex = len(ar)
#size = index*oindex
#
#myimage = ar
#i = j = 0
#for i in range(oindex):
#    for j in range(index):
#        myimage[i][j] = ((ar[i][j]-int(x1))*(((int(y2)-int(y1))/(int(x2)-int(x1)))+int(y1)))
#    
#    
#outpot = Image.fromarray(myimage, 'RGB')
##img.save('my.png')
#outpot.show()