import cv2 as opencv
import numpy as num

def FaceDetectionFromImage(filename,cascade):
  opencv.namedWindow("Faces Detected", opencv.WINDOW_NORMAL)        
  
  Imageinput = opencv.imread(filename)
  Imageinput = opencv.cvtColor(Imageinput, opencv.COLOR_BGR2GRAY)

  output = cascade.detectMultiScale(Imageinput, 1.5, 4)
  #Output = opencv.cvtColor(totalFacesDetect, opencv.COLOR_BGR2GRAY)
 
  for (x, y, w, h) in output:
    coordinatesOfXY = x + w // 2, y + h // 2
    radius = w // 2 
    opencv.circle(Imageinput, coordinatesOfXY, radius, (42, 187, 155, 1), 3)

  
  outputimg = Imageinput
  outputimg = opencv.resize(outputimg, (960, 540)) 
  opencv.imshow('Faces Detected', outputimg)
  opencv.waitKey()


def EyeDetectionFromImage(filename,cascade):
    Imageinput = opencv.imread(filename)

    gray = opencv.cvtColor(Imageinput, opencv.COLOR_BGR2GRAY)

    output = cascade.detectMultiScale(gray, 1.1, 4)
  
    for (x, y, w, h) in output:
        coordinatesOfXY = x + w // 2, y + h // 2 
        radius = w // 2 
        opencv.circle(Imageinput, coordinatesOfXY, radius, (42, 187, 155, 1), 3)

   
    
    outputimg = Imageinput
    outputimg = opencv.resize(outputimg, (960, 540))
    opencv.imshow('Eyes Detected', outputimg)
    opencv.waitKey()


def FaceDetectionFromCamera(cascade):
    
  cap = opencv.VideoCapture(0,opencv.CAP_DSHOW)
   


  while True:
    
      _, Imageinput = cap.read()

    
      Imageinput = opencv.cvtColor(Imageinput, opencv.COLOR_BGR2GRAY)

   
      Output = cascade.detectMultiScale(Imageinput, 1.1, 4)

    
      for (x, y, w, h) in Output:
         opencv.rectangle(Imageinput, (x, y), (x+w, y+h), (255, 0, 0), 2)


      opencv.imshow('Detecting Faces', Imageinput)

   
      k = opencv.waitKey(0) 
      if k==13:
        break
        

  cap.release()


def main():

   while(1):
    chooseopt = input("Want to run application ? Press 'y' otherwise 'n' :")
    if chooseopt == 'y' or chooseopt == 'Y':

     face_cascade = opencv.CascadeClassifier('FaceDetection.xml')
     eye_cascade = opencv.CascadeClassifier('EyeDetection.xml')
     userinput =  input('Press 1 For Face Detection From Image:\n 2 for Eyes From Image:\n 3 For Face Detection From Camera:\n')
     print(userinput)
     if int(userinput) == 1:
       FaceDetectionFromImage(r'ImagesData\positiveimg6.jpeg',face_cascade)
     elif int(userinput) ==2:
      EyeDetectionFromImage(r'ImagesData\PositiveImg4.jpeg',eye_cascade)
     elif int(userinput) == 3:
      FaceDetectionFromCamera(face_cascade)
     else:
        print("No such a feature is available")
    else:
       break
main()