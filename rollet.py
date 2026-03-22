import random
import time
from itertools import count


def how_much_to_bet(money) -> int:
    """
    get curent money amount and update it - can't be negative
    :param money: how much money in reserve
    :return: how much to bet (not mor then reserved)
    """
    print('you have: ', money)
    print('if you want to quit write - quit')
    bet_amount = input("how much to bet?: ")
    if money.isdigit():
        money = int(money)
        if bet_amount.isdigit():
            bet_amount2 = int(bet_amount)
            while bet_amount2 <= 1 or bet_amount2 > money:
                print("can't bet, money is to low or higer then owned cash")
                bet_amount2 = input("how much to bet, ?: ")
            return bet_amount2
        else:
            return 'I understand'
    else:
        return 'I understand'



def random_symbol(symbols) -> str:
    """
    choose 1 random symbol at a time- 3 in total
    :param symbols: choose 1 random symbol at a time
    :return:all chosen symbols
    """
    symbols_chosen = []
    for i in range(3):
        symbol = random.choice(symbols)
        symbols_chosen.append(symbol)
        time.sleep(1.5)
        print('|'.join(symbols_chosen) if len(symbols_chosen) <= 2 else "")
    print(f'🥁🥁drum roll🥁🥁 {time.sleep(1.5)}\n')
    return "".join(symbols_chosen)

def check_symbols(symbol_dict, your_symbols_are, bet):
    rates_are = []
    count = 0
    for symbol in your_symbols_are:
        rates_are.append(symbol_dict[symbol])
        if symbol_dict[symbol] in rates_are:
            count += 1
        else:
            continue
    return count
















# main
rate    = [2, 3, 9, 7, 11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
symbol_dict = {"🍒": 2, "🍋": 3, "⭐": 9, "🔔": 7, "💎": 11}
money = str(50)
print("=== SLOT MACHINE === \n")
while True:
    bet = int(how_much_to_bet(money))
    money = str(int(money) - bet)
    if money == 'I understand':
        print('sorry to see you live, good bye')
        break
    print(f'you got - {money} left')
    your_symbols_are = (random_symbol(symbols))
    print(your_symbols_are)
    you_won = check_symbols(symbol_dict, your_symbols_are, money)
    print(you_won)


    # check_symbol(money, your_symbols_are)


    # how_much_bet(money)
    # amount_lest(money, win_or_lost)
