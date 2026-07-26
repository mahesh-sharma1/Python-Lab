  
def check(num):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"

a = int(input("Enter a positive number: "))
print("The number is: ",check(a))

# if a % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# for i in range(11):
#     print(f"{i} is {check(i)}")