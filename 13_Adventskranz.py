#!/usr/bin/env python3
from datetime import date, timedelta
import RPi.GPIO as GPIO
import time  # Importiere das time-Modul für Verzögerungen

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
    GPIO.setwarnings(False)  # Unterdrücke Warnungen
    for pin in LED_PINS.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)  # LEDs ausschalten

def clear_gpio():
    """Räumt die GPIO-Konfiguration auf."""
    GPIO.cleanup()

def control_leds(active_leds):
    """
    Steuert die LEDs.
    :param active_leds: Liste der aktiven LEDs (1 bis 4)
    """
    for led, pin in LED_PINS.items():
        if led in active_leds:
            GPIO.output(pin, GPIO.HIGH)  # LED an
            print(f"LED {led} an (GPIO {pin})")  # Debug-Ausgabe
        else:
            GPIO.output(pin, GPIO.LOW)   # LED aus
            print(f"LED {led} aus (GPIO {pin})")  # Debug-Ausgabe

def get_active_leds(test_date=None):
    """
    Gibt die aktiven LEDs basierend auf dem aktuellen oder angegebenen Datum zurück.
    :param test_date: Optionales Testdatum im Format YYYY-MM-DD.
    :return: Liste der aktiven LEDs.
    """
    # Aktuelles Datum verwenden, falls kein Testdatum angegeben ist
    today = test_date or date.today()
    
    # Adventssonntage berechnen
    year = today.year
    advent_sundays = get_advent_sundays(year)
    
    # Debug-Ausgabe der berechneten Adventssonntage
    print(f"Berechnete Adventssonntage für {year}:")
    for i in range(1, 5):
        print(f"Advent {i}: {advent_sundays[i]}")
    
    # Bestimmen der aktiven LEDs basierend auf dem Datum
    active_leds = []
    for i in range(1, 5):
        if today >= advent_sundays[i]:
            active_leds.append(i)
    return active_leds

def get_advent_sundays(year):
    """
    Berechnet die Adventssonntage für das gegebene Jahr.
    :return: Dictionary mit Adventssonntagen.
    """
    christmas = date(year, 12, 25)
    # Berechnung des 4. Advent (letzter Sonntag vor Weihnachten)
    fourth_advent = christmas - timedelta(days=(christmas.weekday() + 1))
    third_advent = fourth_advent - timedelta(weeks=1)
    second_advent = third_advent - timedelta(weeks=1)
    first_advent = second_advent - timedelta(weeks=1)
    
    return {
        1: first_advent,
        2: second_advent,
        3: third_advent,
        4: fourth_advent
    }

def main(test_date=None):
    """Hauptprogramm."""
    setup_gpio()
    try:
        while True:  # Endlosschleife für kontinuierliche Ausführung
            active_leds = get_active_leds(test_date)
            print(f"Aktive LEDs: {active_leds}")
            control_leds(active_leds)  # Funktion zur Steuerung der LEDs aufrufen
            time.sleep(60)  # Warte 60 Sekunden bevor die nächste Überprüfung
    except KeyboardInterrupt:
        print("Programm wurde durch Benutzer beendet.")
    finally:
        clear_gpio()

if __name__ == "__main__":
    # Testmodus aktivieren, z.B. für den 2. Advent (Testdatum)
    test_date = date(2024,12,8 )  # Beispiel: 2. Advent 2024    
    main(test_date)