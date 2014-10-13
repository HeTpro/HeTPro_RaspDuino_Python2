
# HeTpro
# Herramientas Tecnologicas Profesionales
# http://www.hetpro.com.mx
# 
# Codigo para la tarjeta RaspDuino HeTPro
# Python
# Se requiere instalar el IDLE de pyton para comenzar a usar estos ejemplos


# Uso de pines con GPIO (numeracion del pin respecto al header de la tarjeta)


import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
 
while True:
 GPIO.output(11, True)
 time.sleep(1)
 GPIO.output(11, False)
 time. sleep