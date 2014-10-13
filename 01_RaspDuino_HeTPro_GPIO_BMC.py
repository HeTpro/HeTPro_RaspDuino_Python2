
# HeTpro
# Herramientas Tecnologicas Profesionales
# http://www.hetpro.com.mx
# 
# Codigo para la tarjeta RaspDuino HeTPro
# Python
# Se requiere instalar el IDLE de pyton para comenzar a usar estos ejemplos


# Uso de pines con BMC (numeracion del pin del IC)


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

while True:
 GPIO.output(17, True)
 time.sleep(1)
 GPIO.output(17, False)
 time. sleep