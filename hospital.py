patientName = ["Armaan", "Zaara", "Zoe"]

Readings = [[35.0, 44.0, 45.0],     # Temprature -> 0
            [66.0, 65.0, 140.0]]    # Pulse -> 1

def hoSystem(hospitalNumber):
    if hospitalNumber >= 0 and hospitalNumber <= 1000:
        print("Hospital Number Valid")
        print(patientName[hospitalNumber])
        if Readings[0][hospitalNumber] >= 31 and Readings[0][hospitalNumber] <= 37 and Readings[1][hospitalNumber] >= 55 and Readings[1][hospitalNumber] <= 100:
            print("Normal Readings")
        elif Readings[0][hospitalNumber] < 31 or Readings[0][hospitalNumber > 37] and (Readings[1][hospitalNumber] < 55 or Readings[1][hospitalNumber] > 100):
            print("Severe Warning All parameters out of range")
        elif Readings[0][hospitalNumber] < 32 or Readings[0][hospitalNumber] > 37:
            print("Warning Param out of range(temprature)")
        elif Readings[1][hospitalNumber] < 55 or Readings[1][hospitalNumber] > 100:
            print("Warning Param out of range(pulse)")


    else:
        print("Sorry Invalid Hospital No try again!")

inp = int(input("Enter Patient No: "))
hoSystem(inp)