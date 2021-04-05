weight = 80
height = 1.785

bmi = weight / float(height) ** 2
roundedBMI = round(bmi, 2)
print(f"BMI: {roundedBMI}")

if roundedBMI >= 25:
    print("Overweight")
    print("Please do more exercise")
elif (roundedBMI >= 18.5) & (roundedBMI < 25):
    print("Healthy weight")
else:
    print("Underweight")
    print("Please eat a bit more")
