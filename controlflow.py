# ex1

x = 7
x = 10
if x < 10:
 print("Less than 10")
else: 
 print("Greater than or equal to 10")


 # ex2

 x = 7
 if x < 10:
   print("Less than 10")
 elif x > 10:
  print("Greater than 10")
x = 15

# ex3

x = 15
if x < 10:
  print("Less than 10")
elif 10 <= x < 20:
  print("Between 10 and 20")
else:
  print("Greater than 20")

  # ex4

  x = 15
  if x < 10 or x > 20:
     print("Out of range")
  else:
     print("In range")
     x = 5

     # ex5

     score = int(input("Enter your score:"))
     if score > 100 or score < 0:
        print("Score out of range")
     elif score >= 90:
        print ("A")
     elif score >= 80:
       print("B")
     elif score >= 70:
       print("C")
     elif score >= 60:
       print("D")
     else:
       print("F")

       # ex6

def calculate_tax(status, income):
    tax_rate = 0
    if status == "Single":
        if income < 10000:
            tax_rate = 0.10
        elif income < 40000:
            tax_rate = 0.12
        else:
            tax_rate = 0.22
    elif status == "Married Filing Jointly":
        if income < 20000:
            tax_rate = 0.10
        elif income < 80000:
            tax_rate = 0.12
        else:
            tax_rate = 0.22

    tax = income * tax_rate
    return tax

status = input("Enter your filing status (Single, Married Filing Jointly): ")
income = float(input("Enter your taxable income: "))
print(f"Tax to be paid: ${calculate_tax(status, income):.2f}")

