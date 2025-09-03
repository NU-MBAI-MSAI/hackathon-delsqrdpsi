# pair: Bhaskar Samineni (3655842) and George Pantazis (3730188)
# 09/03/2025
# Part 0 - Speeding ticket

def part0_speeding_ticket():
    speed_limit = int(input())
    speed_driven = int(input())

    if speed_driven <= speed_limit-10:
        print(50)
    elif (speed_driven - speed_limit) >= 6 and (speed_driven - speed_limit) <= 20:
        print(75)
    elif (speed_driven - speed_limit) >= 21 and (speed_driven - speed_limit) <= 40:
        print(150)
    elif speed_driven - speed_limit > 40:
        print(300)
    else:
        print(0)

part0_speeding_ticket()

# test cases
# 35 45 -> 75
# 35 26 -> 0
# 35 56 -> 150
# 35 76 -> 300
# 35 0 -> 50


