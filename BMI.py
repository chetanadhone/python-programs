def bmi_calc(weight, height):
    bmi = weight / height ** 2 #weight/pow(height,2)
    return bmi


wt = float(input("Enter your weight in kg: "))
ht = float(input("Enter your height in metres: "))
print(bmi_calc(wt, ht))

