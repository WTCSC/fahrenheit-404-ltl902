def temp_converter():
    temp = input("Would you like to convert from Fahrenheit (F), Celsius (C), or Kelvin (K)?\n").upper()
    if temp == "F":
        F = float(input("Please enter temperature in Fahrenheit:\n"))
        c = (F - 32) * 5/9
        k = c + 273.15
        print(F, "degrees Fahrenheit is", round(c, 2), "degrees Celsius or", round(k, 2), "degrees Kelvin")
    elif temp == "C":
        C = float(input("Please enter temperature in Celsius:\n"))
        f = (C * 9/5) + 32
        k = C + 273.15
        print(C, "degrees Celsius is", round(f, 2), "degrees Fahrenheit or", round(k, 2), "degrees Kelvin")
    elif temp == "K":
        K = float(input("Please enter temperature in Kelvin:\n"))
        c = K - 273.15
        f = (K - 273.15) * 9/5 + 32
        print(K, "degrees Kelvin is", round(c, 2), "degrees Celsius or", round(f, 2), "degrees Fahrenheit")
    else:
        print("Error please input F, K, or C")

temp_converter()

rep = input("Do you want to convert another temperature (Y/N)\n").upper()

while rep == "Y":
    temp_converter()
    rep = input("Would you like to convert another temperature? (Y/N)\n").upper()
    if rep == "N":
        print("Thank you for using the temp converter")
    elif rep != "Y":
        print("Error please input Y or N")
        break








