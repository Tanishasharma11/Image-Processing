#Importing the libraries
import cv2
#Reading image using opencv
i=cv2.imread('face.jpeg')
#Printing shape of image
print(i.shape)
#Printing the stored image array
print(i)
#Converting to grayscale
i_gray=cv2.imread('face.jpeg',0)
#Selecting region in the image
r=cv2.selectROI(i)
#Displaying the selected area
print(r)
#Changing colour of selected region to red
i[r[1]:r[1]+r[3],r[0]:r[0]+r[2],0]=0
i[r[1]:r[1]+r[3],r[0]:r[0]+r[2],1]=0
i[r[1]:r[1]+r[3],r[0]:r[0]+r[2],2]=255
#Displaying the output
cv2.imshow(i)
cv2.waitkey(0)
#Replacing ROI with an image
k=cv2.imread('spongebob.jpg')
#Pasting new image in ROI by resizing it
k1=cv2.resize(k,(r[2],r[3]))
i[r[1]:r[1]+r[3],r[0]:r[0]+r[2]]=k1
cv2.imshow("Modified image",i)
cv2.waitkey(0)
