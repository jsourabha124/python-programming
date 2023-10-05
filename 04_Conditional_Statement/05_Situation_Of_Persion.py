"""
Given temperature of person, analyse the situation of person and give him advice.
Situations and advice related with temperature are :
1. temp is in range of [85.0 to 91.0] then advice is "Serious Hypothermia".
2. temp is in range of (91.0 to 95.0) then advice is "Mild Hypothermia".
3. temp is in range of [95.0 to 98.0] then advice is "Normal Temperature".
4. temp if in range of (98.0 to 100.0] then advice is "Mild Fever".
5. temp if in range of (100.0 to 105.0] then advice is "High Fever".
"""

try:
    input_temp = input("Enter a temperature of person : ")
    temp = float(input_temp)
    if temp.is_integer():
        temp = int(input_temp)

    if (temp >= 85.0 and temp <=91.0):
        print("Serious Hypothermia")
    elif (temp > 91.0 and temp <95.0):
        print("Mild Hypothermia")
    elif (temp >= 95.0 and temp <=98.0):
        print("Normal Temperature")
    elif temp > 98.0 and temp <=100.0:
        print("Mild Fever")
    elif temp<85:
        print("Very Low")
    else:
        print("High Fever")


except:
    print("Error")
