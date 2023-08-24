makes_sense = False
distance = int(input("How far do you need to travel? "))
mode_transport = input("What mode of transportation are you taking? ")
while makes_sense != True:
  mode_transport = input("What mode of transportation are you taking? ")
  if mode_transport == "Walk":
      mode_transport = int("5")
      makes_sense = True
  elif mode_transport == "Run":
      mode_transport = int("10")
      makes_sense = True
  elif mode_transport == "Bike":
      mode_transport = int("20")
      makes_sense = True
  elif mode_transport == "Car":
      mode_transport = int("50")
      makes_sense = True
  else:
      print("Sorry, could you tell if again?")

Time = int(distance/mode_transport)
print("This will be how long it takes", Time,"hours.")
