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



def part0_count_input_length():
    count = 0 
    string = input()
    unsuitable = [" ",".","!",","]
    for i in string:
        if i in unsuitable:
            continue
        else:
            count+=1

    print(count)


def part0_stock_trading(prices):
    maxprofit = 0
    for i in range(0,len(prices)-2):
        for j in range(i,len(prices)-1):
            profit = prices[j] - prices[i]
            # print(profit)
            # print(i,j)
            if profit>maxprofit:
                maxprofit = profit

    return maxprofit


    
        

if __name__ == '__main__':
#### Execution
    # part0_speeding_ticket()
    # part0_heating_cooling_days()
    # part0_count_input_length()

    #stock_trading
    print(part0_stock_trading([1,1,1,1])==0)
    print(part0_stock_trading([2,1,11,44,29,1])==43)
    print(part0_stock_trading([7,1,5,3,6,4])==5)
    print(part0_stock_trading([7,6,4,3,1])==0)
    print(part0_stock_trading([7])==0)
    





