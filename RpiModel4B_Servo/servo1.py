
import RPi.GPIO as GPIO
import time

#GPIO'yu numerik moda gecirdik
GPIO.setmode(GPIO.BOARD)

#11. pini output ayarladık 
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) #pini ve frekansı belirliyoruz

#PWM başlatılıyor fakat pulse kapalı duruyor
servo1.start(0)
print ("2 sn bekleyin")
time.sleep(2)


print ("10 adımda 180 derece donduruluyor")

#duty degerini belirledik
duty = 2

# duty degerini 2 den 12 ye getiren dongu (0 dan 180 dereceye)
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1


time.sleep(2)

# tekrar 90 dereceye donduruyurouz
print ("2 saniye icinde 90 tereceye donecek")
servo1.ChangeDutyCycle(7)
time.sleep(2)

#0 dereceye tekrar donduruyoruz
print ("0 derceye tekrar donuluyor")
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

#tekrar kullanım icin GPIO'yu temizliyoruz ve servo PWM'ini durduruyoruz
servo1.stop()
GPIO.cleanup()
print ("occakal")