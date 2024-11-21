#!/usr/bin/env python3
#test_adventssonntage.py

from datetime import date, timedelta

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

if __name__=='__main__':

    current_year = date.today().year
    advent_sundays = get_advent_sundays(current_year)

    for sonntag in advent_sundays:
        print(f"Advent {sonntag}: {advent_sundays[sonntag]}")
