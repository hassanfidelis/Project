#!/usr/bin/python

import sys
import Adafruit_DHT
import time

humidity, temperature = Adafruit_DHT.read_retry(11, 4)

while True:
    if humidity is not None and temperature is not None:
        print("Coletando informacoes...\n")

        print("Temperatura (em graus Celsius): %2d" % (temperature))
        print("Humidade (relativa): %2d" (humidity))

        humidity, temperature = Adafruit_DHT.read_retry(11, 4)

        print("Temperatura: %2d" % (temperature))
        print("Humidade: %2d" % (humidity))

        print("Hey")

        time.sleep(2)

        print("\n")

    else:
        print("ERRO DE LEITURA: %d" % result.error_code)
        print("Tente novamente.")
