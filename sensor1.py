#!/usr/bin/python

import sys
import Adafruit_DHT
import time

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
