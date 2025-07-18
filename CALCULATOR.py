def calculator(num1,num2,operator):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1 * num2
    elif operator=="/":
        if num2==0:
            return "Error: Division by Zero"
        return num1/num2
    elif operator=="**":
        return num1**num2
    else:
        return "Invalid operation"

print("CALCULATOR")
try:
    num1=float(input("Enter the first number: ").strip())
    num2=float(input("Enter the second number: ").strip())
    print("Choose the operator: \n 1.Add(+) \n 2.Subtraction(-) \n 3.Multiplication(*) \n 4.Division(/) \n 5.Power(**)")
    operation=input()
    result=calculator(num1,num2,operation)
    print(f"Result: {result}")
except:
    print("Error: Enter a valid number")
    exit()
while True:
    if not isinstance(result, (int, float)):
        print("Further calculation not possible due to previous error.")
        break

    print("Do you want to further use the solution for the calculation? (yes/no)")
    ans = input().lower()
    if ans != "yes":
        break
    try:
        num3=float(input("Enter the next number: ").strip())
        print("Choose the operator: \n 1.Add(+) \n 2.Subtraction(-) \n 3.Multiplication(*) \n 4.Division(/) \n 5.Power(**)")
        operation=input()
        result=calculator(result,num3,operation)
        print(f"Result: {result}")
    except:
        print("Error: Enter a valid number")

print("THANKYOU 😄!!")