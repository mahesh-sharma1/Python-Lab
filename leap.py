# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# # Test multiple years
# # years = [2020, 2021, 2022, 2023, 2024, 1900, 2000]
# years = []
# for i in range(5):
#     yr = int(input())
#     years.append(yr)
# for yr in years:
#     if is_leap_year(yr):
#         print(f"{yr} is a leap year")
#     else:
#         print(f"{yr} is not a leap year")

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
       return False

yr = int(input("Enter a year: "))
# year = is_leap_year(yr)
if is_leap_year(yr):
        print(f"{yr} is a leap year")
else:
        print(f"{yr} is not a leap year")
