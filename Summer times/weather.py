temp = float(input('Enter the temperature in Celsius:'))
if temp > 0:
    print('Freezing weather')
elif temp >0 and temp < 20:
    print('Very Cold weather')
elif temp > 20 and temp < 40:
    print('Normal in Temperature')
elif temp > 40 and temp < 60:
    print('Its Hot')