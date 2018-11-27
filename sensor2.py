#!/usr/bin/python

import sys
import Adafruit_DHT
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(32, gpio.OUT)

gpio.output(32, 1) #ligando o pino 32
time.sleep(3) #pausa de 3 seg para ver ligar e desligar o pino 32
gpio.output(32, 0) #desligando o pino 32

humidity, temperature = Adafruit_DHT.read_retry(11, 4)

while True:
    if humidity is not None and temperature is not None:
        print("Coletando informações...\n")

        print("Temperatura (em graus Celsius): %2d" % (temperature))
        print("Humidade (relativa): %2d" (humidity))

        time.sleep(2)

        print("\n")

    else:
        print("ERRO DE LEITURA: %d" % result.error_code)
        print("Tente novamente.")
