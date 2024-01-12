print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0
if height >= 120:
  print("You lucky sonofabitch you get to ride!")
  if age < 12:
    print("Child tickets are $5")
    bill = 5
  elif age <= 18:
    print("Teen tickets are $7")
    bill = 7
  elif age >= 45 and age <= 55:
    print("You sorry bastard, go in free")
    bill = 0
  else:
    print("adult tickets are $12")
    bill = 12
  wants_photo = input("Do you want a photo Y or N. ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bil is {bill}")
  
else:
  print("Go away asshole, you cannot ride")