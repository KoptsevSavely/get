from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = camera.MAX_RESOLUTION

#camera.quality = 100

camera.sharpness = 50

#camera.contrast = 50



sleep(2)

camera.capture('/home/b03-501/laba228/get/light/fil_blue2.jpeg')
print ("фото сохранено")

camera.close()