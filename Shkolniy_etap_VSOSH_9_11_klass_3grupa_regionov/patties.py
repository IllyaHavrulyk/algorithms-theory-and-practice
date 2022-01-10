def calculate_next_buy(todays_purchase):
    if todays_purchase == 1:
        return 2
    elif todays_purchase == 2:
        return 3
    elif todays_purchase == 3:
        return 1


def main():
    cranberries_price = int(input())
    blueberries_price = int(input())
    cherries_price = int(input())
    days = int(input())
    buy_today = int(input())
    total_spent = 0
    if(buy_today == 1):
        total_spent += cranberries_price
    if(buy_today == 2):
        total_spent += blueberries_price
    if(buy_today == 3):
        total_spent += cherries_price
    for i in range(1, days):
        if(calculate_next_buy(buy_today) == 1):
            total_spent += cranberries_price
        elif(calculate_next_buy(buy_today) == 2):
            total_spent += blueberries_price
        elif(calculate_next_buy(buy_today) == 3):
            total_spent += cherries_price
        buy_today = calculate_next_buy(buy_today)
    print(total_spent)


main()
