def fahrenheit(temp_celsius):
    return 32 + 1.8 * temp_celsius

def gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid):
    return temp_celsius - (luchtvochtigheid / 100 * windsnelheid)

def weerrapport(temp_celsius, windsnelheid, luchtvochtigheid):
    gevoel_temp = gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid)

    if gevoel_temp < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel_temp < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= gevoel_temp < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gevoel_temp < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gevoel_temp < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"

def weerstation():
    totaal_temp = 0
    dagen = 0

    while dagen < 7:
        temp = input(f"Wat is op dag {dagen + 1} de temperatuur[C]: ")
        if temp == "":
            break

        temp = float(temp)
        wind = float(input(f"Wat is op dag {dagen + 1} de windsnelheid[m/s]: "))
        vocht = float(input(f"Wat is op dag {dagen + 1} de vochtigheid[%]: "))

        temp_f = fahrenheit(temp)
        rapport = weerrapport(temp, wind, vocht)

        totaal_temp += temp
        dagen += 1
        gem_temp = totaal_temp / dagen

        print(f"Het is {temp:.1f}C ({temp_f:.1f}F)")
        print(rapport)
        print(f"Gem. temp tot nu toe is {gem_temp:.1f}")
        print("=" * 40)

weerstation()


# Bronnen: Testraamwerk van Bart, lessen + presentaties 01 tot 05 van PROG, w3schools.com
