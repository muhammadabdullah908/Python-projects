name = input("Enter your name:")
age = int(input("Enter your age:"))
weight = float(input("Enter your weight(kg):")) 
height = float(input("Enter your height(m):"))

bmi = weight/(height**2)
print(f"Your BMI is {round(bmi,2)}")

if bmi<=18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You are normal.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")