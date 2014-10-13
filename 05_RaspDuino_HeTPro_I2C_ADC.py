
# HeTpro
# Herramientas Tecnologicas Profesionales
# http://www.hetpro.com.mx
# 
# Codigo para la tarjeta RaspDuino HeTPro
# Python
# Se requiere instalar el IDLE de pyton para comenzar a usar estos ejemplos

# Se requiere instalar las bibliotecas para I2C
# http://hetpro-store.com/TUTORIALES/pic/python-i2c-uso-y-configuracion/

# Obten ADC en tu Raspberry Pi

print "i2c test 01";
 
import smbus
import time
 
time.sleep(0.5) # Dormir por 0.5 segundos
 
bus = smbus.SMBus(1)
 
DEVICE_ADDRESS = 0x08
 
print "Configurado";
 
#S/D = 1   Single ended / Una entrada a tierra
#O/S = 0   Odd / sin signo
#S1  = 0   Seleccion de canal
#S0  = 0   Seleccion de canal / Canal 0 pin A3
#UNI = 1   Bit unipolar
#SLP = 0   Activo
 
# 100010xx
# 0x88
 
time.sleep(1) # Dormir por 0.5 segundos
 
for i in range (1,40):
    time.sleep(0.2)
    data_raw1 = bus.read_word_data(DEVICE_ADDRESS,0xDC)
    data_fix = ((data_raw1&0xFF00)>>8)+((data_raw1&0x00FF)<<8)
    data_fix2= float(data_fix>>4)
    data_volt= float (data_fix2 * 5/4096)
    print float(data_volt)
 
print "End"