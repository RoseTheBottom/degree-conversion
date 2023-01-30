import sys
response = input("Input degrees in Fahrenheit, ")
try:
  F = int(response)
except Exception:
  print("Not a number")
  sys.exit()
C = (F-32)*5/9
print("F degrees Fahrenheit is", C, "In Celcius")