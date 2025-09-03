# pair: Bhaskar Samineni (3655842) and George Pantazis (3730188)
# 09/03/2025
# Part 0 - Speeding ticket

# def part0_speeding_ticket():
#     speed_limit = int(input())
#     speed_driven = int(input())

#     if speed_driven <= speed_limit-10:
#         print(50)
#     elif (speed_driven - speed_limit) >= 6 and (speed_driven - speed_limit) <= 20:
#         print(75)
#     elif (speed_driven - speed_limit) >= 21 and (speed_driven - speed_limit) <= 40:
#         print(150)
#     elif speed_driven - speed_limit > 40:
#         print(300)
#     else:
#         print(0)


# test cases
# 35 45 -> 75
# 35 26 -> 0
# 35 56 -> 150
# 35 76 -> 300
# 35 0 -> 50

def part0_heating_cooling_days():
    temp = 0
    heating_days = 0
    cooling_days = 0

    while temp > -459:
        try:
            temp = int(input("Enter the average daily temperature: "))
        except ValueError:
            print("use an integer stupid")
            continue
        if temp < 60 and temp >= -459:
            heating_days += 1
        elif temp > 80:
            cooling_days += 1
        
    print("Heating days:",heating_days)
    print("Cooling days:",cooling_days)


part0_heating_cooling_days()

# test cases
