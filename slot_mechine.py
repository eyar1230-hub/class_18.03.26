import random
import time

def how_much_to_bet(money) -> int | str:
    """
    get curent money amount and update it - can't be negative
    :param money: how much money in reserve
    :return: how much to bet (not mor then reserved)
    """
    print('you have: ', money)
    print('if you want to quit write - quit')
    bet_amount = input("how much to bet?: ")

    money = int(money)
    if bet_amount.isdigit():
        bet_amount_int = int(bet_amount)
        while bet_amount_int < 1 or bet_amount_int > money:
            print("can't bet, money is to low or higer then owned cash")
            bet_amount_int = input("how much to bet, ?: ")
        return int(bet_amount_int)
    else:
        return 0

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
    print(f'🥁🥁drum roll🥁🥁\n')
    time.sleep(1.5)
    return "".join(symbols_chosen)

def check_symbols_and_ernings(symbol_dict, your_symbols_are, bet):
    """

    :param symbol_dict: aplying symbols into rates
    :param your_symbols_are: the symbols randomly chosen for player
    :param bet: amount of $$ chosen by player
    :return: hoe much did plyer earned
    """
    rates_are = [symbol_dict[symbol] for symbol in your_symbols_are]
    counter = 1
    win = None
    max_matches = 0
    winning_rate = 0
    for rate in set(rates_are):
        count = rates_are.count(rate)
        if count > max_matches:
            max_matches = count
            winning_rate = rate

    if max_matches == 3:
        win = (bet * 777 * winning_rate)
        counter = 3
    elif max_matches == 2:
        win = (bet * winning_rate)
        counter = 2
    elif max_matches == 1:
        win = 0
        counter = 1
    return win
########################## main game ##########################
########################## main game ##########################
# main
rate    = [2, 3, 9, 7, 11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
symbol_dict = {"🍒": 2, "🍋": 3, "⭐": 9, "🔔": 7, "💎": 11}
print(f'reate per rolled symbol:\n{symbol_dict}')
money = str(50)
print("=== SLOT MACHINE === \n")
while True:
    bet = int(how_much_to_bet(money))
    if bet == 0:
        print('sorry to see you live, good bye')
        break
    money = str(int(money) - bet)
    print(f'you got - {money} left')
    your_symbols_are = (random_symbol(symbols))
    print(your_symbols_are)
    you_won = check_symbols_and_ernings(symbol_dict, your_symbols_are, bet)
    money = str(int(money) + you_won)
    print(f'your earnings are:\n{you_won}')

