#            BMI calculator using PYTHON using IF,ELIF



weight=float(input("\n Enter the weight of the person in Kg " ))
height=float(input(" \n Enter the height of the person in metres "))

BMI = weight/height**2
print("\n")

print("  Your bmi is :", BMI )


if BMI<18.5 :
    print("The person is Underweight")
elif 18.5<BMI<24.9 :
    print("The person is Normal")
else :
    print("The person is Overweight")