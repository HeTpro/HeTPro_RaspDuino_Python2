
# HeTpro
# Herramientas Tecnologicas Profesionales
# http://www.hetpro.com.mx
# 
# Codigo para la tarjeta RaspDuino HeTPro
# Python
# Se requiere instalar el IDLE de pyton para comenzar a usar estos ejemplos

# Ideal para el shield con el MPR121 que tiene conversion de 3.3V a 5V
# si tienes el MPR121 sin la etapa de conversion, se puede conectar 
# directamente sin necesidad del RaspDuino.

# Se requiere instalar las bibliotecas para I2C
# http://hetpro-store.com/TUTORIALES/pic/python-i2c-uso-y-configuracion/

#!/usr/bin/python
print "HeTPro";
print "MPR121 TEST pruebas para el sensor touch";
print "i2c test 01";
print "No tocar el touch pad...!!!";
 
import smbus
import time
 
time.sleep(0.5) # Dormir por 0.5 segundos
 
bus = smbus.SMBus(1)
 
DEVICE_ADDRESS = 0x5a
DEVICE_REG_MODE = 0x00
 
bus.write_byte_data(DEVICE_ADDRESS , 0x2b , 0x01)
bus.write_byte_data(DEVICE_ADDRESS , 0x2c , 0x01)
bus.write_byte_data(DEVICE_ADDRESS , 0x2d , 0x00)
bus.write_byte_data(DEVICE_ADDRESS , 0x2e , 0x00)
bus.write_byte_data(DEVICE_ADDRESS , 0x2f , 0x01)
bus.write_byte_data(DEVICE_ADDRESS , 0x30 , 0x01)
bus.write_byte_data(DEVICE_ADDRESS , 0x31 , 0xFF)
bus.write_byte_data(DEVICE_ADDRESS , 0x32 , 0x02)
bus.write_byte_data(DEVICE_ADDRESS , 0x41 , 0x0f)
bus.write_byte_data(DEVICE_ADDRESS , 0x42 , 0x0a)
bus.write_byte_data(DEVICE_ADDRESS , 0x43 , 0x0f)
bus.write_byte_data(DEVICE_ADDRESS , 0x44 , 0x0a)
bus.write_byte_data(DEVICE_ADDRESS , 0x45 , 0x0f)
bus.write_byte_data(DEVICE_ADDRESS , 0x46 , 0x0a)
bus.write_byte_data(DEVICE_ADDRESS , 0x47 , 0x0f)
bus.write_byte_data(DEVICE_ADDRESS , 0x48 , 0x0a)
bus.write_byte_data(DEVICE_ADDRESS , 0x49 , 0x0f)
bus.write_byte_data(DEVICE_ADDRESS , 0x4a , 0x0a)
bus.write_byte_data(DEVICE_ADDRESS , 0x4b , 0x0f)
bus.write_byte_data(DEVICE_ADDRESS , 0x4c , 0x0a)
bus.write_byte_data(DEVICE_ADDRESS , 0x4d , 0x0f)
bus.write_byte_data(DEVICE_ADDRESS , 0x4e , 0x0a)
bus.write_byte_data(DEVICE_ADDRESS , 0x4f , 0x0f)
bus.write_byte_data(DEVICE_ADDRESS , 0x50 , 0x0a)
bus.write_byte_data(DEVICE_ADDRESS , 0x51 , 0x0f)
bus.write_byte_data(DEVICE_ADDRESS , 0x52 , 0x0a)
bus.write_byte_data(DEVICE_ADDRESS , 0x53 , 0x0f)
bus.write_byte_data(DEVICE_ADDRESS , 0x54 , 0x0a)
bus.write_byte_data(DEVICE_ADDRESS , 0x55 , 0x0f)
bus.write_byte_data(DEVICE_ADDRESS , 0x56 , 0x0a)
bus.write_byte_data(DEVICE_ADDRESS , 0x57 , 0x0f)
bus.write_byte_data(DEVICE_ADDRESS , 0x58 , 0x0a)
 
bus.write_byte_data(DEVICE_ADDRESS , 0x5d , 0x04)
bus.write_byte_data(DEVICE_ADDRESS , 0x5e , 0x0C)
 
print "Listo!!! Tocuh pad configurado";
for i in range (1,10):
 time.sleep(0.5)
 B=bus.read_byte_data(DEVICE_ADDRESS ,0x5d)
 time.sleep(0.5)
 C=bus.read_byte_data(DEVICE_ADDRESS ,0x5f)
A= bus.read_byte_data(DEVICE_ADDRESS ,0x01)
 print "Valor del registro"
 print A
 
 if A == 32:
 print "Tecla 2"
 elif A == 256:
 print "Tecla 4"
 elif A == 16:
 print "Tecla 5"
 elif A == 2:
 print "Tecla 6"
 elif A == 64:
 print "Tecla 7"
 elif A == 8:
 print "Tecla 8"
 elif A == 1:
 print "Tecla 9"
 else:
 print "."
 
print "End"