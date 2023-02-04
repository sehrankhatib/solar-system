import cv2
img= cv2.imread("solar-system.jpg")
cv2.putText(img,"sun",(50,50),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
cv2.putText(img,"mercury",(100,200),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
cv2.putText(img,"venus",(130,250),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
cv2.putText(img,"earth",(250,300),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
cv2.imshow("display",img)

cv2.waitKey(3000)