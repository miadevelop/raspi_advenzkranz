#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

"""
    GPIO 17 ---[100 Ω]---|>|--- GND  (LED 1)
    GPIO 27 ---[100 Ω]---|>|--- GND  (LED 2)
    GPIO 22 ---[100 Ω]---|>|--- GND  (LED 3)
    GPIO 5  ---[100 Ω]---|>|--- GND  (LED 4)
    |>| symbolisiert die LED.
    100 Ω ist der Vorwiderstand, der den Strom auf ein sicheres Niveau begrenzt.
"""

# GPIO-Pins für die LEDs
LED_PINS = {
    1: 17,  # LED 1 an GPIO 17
    2: 27,  # LED 2 an GPIO 27
    3: 22,  # LED 3 an GPIO 22
    4: 5    # LED 4 an GPIO 5
}

def setup_gpio():
    """Initialisiert die GPIO-Pins."""
    GPIO.setmode(GPIO.BCM)
    for pin in LED_PINS.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)  # LEDs ausschalten

def clear_gpio():
    """Räumt die GPIO-Konfiguration auf."""
    GPIO.cleanup()

def test_leds():
    """Testet alle LEDs nacheinander."""
    for led, pin in LED_PINS.items():
        GPIO.output(pin, GPIO.HIGH)  # LED an
        print(f"LED {led} an (GPIO {pin})")
        time.sleep(1)  # 1 Sekunde warten
        GPIO.output(pin, GPIO.LOW)   # LED aus
        print(f"LED {led} aus (GPIO {pin})")
        time.sleep(1)  # 1 Sekunde warten

def main():
    """Hauptprogramm für den LED-Test."""
    setup_gpio()
    try:
        test_leds()
    finally:
        clear_gpio()

if __name__ == "__main__":
    main()
