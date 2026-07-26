def table(num,lim):
    print(f"The multiplication table of {num} is: \n")
    for i in range(1,lim+1):
        print(f"{num} * {i} = {num * i}")
    
a = int(input("Enter a number to find multiplication: "))
l = int(input("Enter the limit: "))
table(a,l)