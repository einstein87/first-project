#cat.bmp라는 파일을 그레이스케일로 불러오고
#예외처리 코드 주고
#cat_gray.bmp파일로 저장하고, 
#image라는 윈도우 만들어서
#해당영상 보여주고
#10초 기다린다음에 key
#key를 프린트 하고
#이미지 닫는다.



import cv2
import sys

print(cv2.__version__)

img = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)  #img라는 변수에 어떤 형태의 컬러 etc 처리하면서 파일을 읽어와서 img란 변수로 return할거야. 

# 파일이 없다면? 나갈게!
if img is None:
    print('image load failed')
    sys.exit()

cv2.imwrite('cat_gray.bmp',img) #내가 처리한 이미지를 이렇게 저장할게

cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)   #어떤 이름의 윈도우라는 스케치북을 열고, 이 윈도우의 속성과 크기를 결정. 얼만큼의 스케치북을 줄지
cv2.imshow('image',img)  #어떤 이름의 스케치북에, 어떤 이미지를 보여줄지


key = cv2.waitKey(10000)   #key입력 기다려준다. 얼만큼? 10000 ms만큼! 이 안에 입력 없으면 그냥 지나간다.
print(key)    #key를 출력해준다. (Ascii code 값으로), key 입력이 없었다면? -1 나온다. space는 32, enter는 13

cv2.destroyWindow('image')
cv2.destroyAllWindows()

# github test중

