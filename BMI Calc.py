
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

heightw= float(height)
weightw= float(weight)

bmi = int(weightw / heightw**2)

print(f"Your BMI is {bmi}") 
