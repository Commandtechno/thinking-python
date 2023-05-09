today_f = int(input("Enter today's temperature in farenheit: "))
today_c = (today_f - 32) * (5 / 9)
today_k = (today_c) + 273.15

boiling_lead_f = 3180
boiling_lead_c = (boiling_lead_f - 32) * (5 / 9)
boiling_lead_k = (boiling_lead_c) + 273.15

boiling_water_c = 100
boiling_water_k = boiling_water_c + 273.15
boiling_water_f = (boiling_water_c * 9 / 5) + 32

print("today farenheit:", today_f)
print("today celsius:", today_c)
print("today kelvin:", today_k)

print("boiling lead farenheit:", boiling_lead_f)
print("boiling lead celsius:", boiling_lead_c)
print("boiling lead kelvin:", boiling_lead_k)

print("boiling water celsius:", boiling_water_c)
print("boiling water kelvin:", boiling_water_k)
print("boiling water farenheit:", boiling_water_f)
