#!/usr/bin/env python3
########################################################################
# Filename    : SteppingMotor.py
# Description : Motor paso a paso
# Author      : antonio2709
# modification: 21/04/2020
########################################################################
import RPi.GPIO as GPIO
import time 

motorPins = (12, 16, 18, 22)    # definir pines de la 4 fases del motor paso a paso
CCWStep = (0x01,0x02,0x04,0x08) # definir el orden de la fuente de alimentacion para girar en sentido antihorario
CWStep = (0x08,0x04,0x02,0x01)  #  definir el orden de la fuente de alimentacion para girar en sentido horario

def setup():    
    GPIO.setmode(GPIO.BOARD)       # usar Fisico numeracion  GPIO 
    for pin in motorPins:
        GPIO.setup(pin,GPIO.OUT)
        
# el motor paso a paso de cuatro fases es un ciclo,la siguiente funcion se utiliaza para conducir el motor en un sentido u otro 
def moveOnePeriod(direction,ms):    
    for j in range(0,4,1):      # ciclo para el orden de la fuente de alimentacion
        for i in range(0,4,1):  # asignar a cada pin
            if (direction == 1):# orden de la fuente de alimentacion en el sentido de las agujas del reloj
                GPIO.output(motorPins[i],((CCWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
            else :              # orden de la fuente de alimentacion en el sentido contrario de las agujas del reloj
                GPIO.output(motorPins[i],((CWStep[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
        if(ms<3):       # el retraso no puede ser inferior a 3msg, de lo contario excedera la velocidad del limite del motor
            ms = 3
        time.sleep(ms*0.001)    
        
# cfuncion de rotacion continua, los pasos del parametro especifican los ciclos de rotacion , cada cuatro
def moveSteps(direction, ms, steps):
    for i in range(steps):
        moveOnePeriod(direction, ms)
        
# funcion para parar el  motor
def motorStop():
    for i in range(0,4,1):
        GPIO.output(motorPins[i],GPIO.LOW)
            
def loop():
    while True:
        moveSteps(1,3,512)  # girando 360º en el sentido de las agujas del reloj, de un total de 2048 pasos en un circulo
        time.sleep(0.5)
        moveSteps(0,3,512)  # girando 360º en el sentido contrario de las agujas del reloj,
        time.sleep(0.5)

def destroy():
    GPIO.cleanup()             # recurso de limpieza de pines

if __name__ == '__main__':     # 
    print ('El programa esta iniciado...')
    print('presiona control+C para finalizar el programa')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  
        destroy()


