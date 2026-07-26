def add(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i
    return sum

a = int(input("Enter a number: "))
total = add(a)
print(f"The sum of numbers upto {a} is: {total}")