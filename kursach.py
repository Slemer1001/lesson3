import sys
import json
import random


# Функція для оновлення курсу
def update_rate(config, state):
    new_rate = round (random.uniform (state['rate'] - config['delta'], state['rate'] + config['delta']), 2)
    state['rate'] = new_rate
    save_state (state)


# Функція для здійснення покупки
def buy_usd(amount, state):
    required_uah = round (amount * state['rate'], 2)
    if state['uah_balance'] >= required_uah:
        state['uah_balance'] = round (state['uah_balance'] - required_uah, 2)
        state['usd_balance'] = round (state['usd_balance'] + amount, 2)
        save_state (state)
        print (f"Bought {amount} USD")
    else:
        print (f"UNAVAILABLE, REQUIRED BALANCE UAH {required_uah}, AVAILABLE {state['uah_balance']}")


# Функція для здійснення продажу
def sell_usd(amount, state):
    if state['usd_balance'] >= amount:
        received_uah = round (amount * state['rate'], 2)
        state['uah_balance'] = round (state['uah_balance'] + received_uah, 2)
        state['usd_balance'] = round (state['usd_balance'] - amount, 2)
        save_state (state)
        print (f"Sold {amount} USD")
    else:
        print (f"UNAVAILABLE, REQUIRED BALANCE USD {amount}, AVAILABLE {state['usd_balance']}")


# Функція для збереження стану у файл
def save_state(state):
    with open ('state.json', 'w') as f:
        json.dump (state, f)


# Функція для відновлення початкового стану
def restart(config):
    state = {
        "rate": config['rate'],
        "uah_balance": config['uah_balance'],
        "usd_balance": config['usd_balance']
    }
    save_state (state)
    print ("Game restarted")


# Основний код
if __name__ == '__main__':
    # Завантаження конфігурації
    with open ('config.json', 'r') as f:
        config = json.load (f)

    # Завантаження стану
    with open ('state.json', 'r') as f:
        state = json.load (f)

    if len (sys.argv) > 1:
        command = sys.argv[1].upper ()
        if command == 'RATE':
            print (state['rate'])
        elif command == 'AVAILABLE':
            print (f"USD {state['usd_balance']} UAH {state['uah_balance']}")
        elif command == 'BUY':
            if len (sys.argv) == 3:
                if sys.argv[2].upper () == 'ALL':
                    amount = state['uah_balance'] / state['rate']
                    buy_usd (amount, state)
                else:
                    amount = float (sys.argv[2])
                    buy_usd (amount, state)
        elif command == 'SELL':
            if len (sys.argv) == 3:
                if sys.argv[2].upper () == 'ALL':
                    amount = state['usd_balance']
                    sell_usd (amount, state)
                else:
                    amount = float (sys.argv[2])
                    sell_usd (amount, state)
        elif command == 'NEXT':
            update_rate (config, state)
        elif command == 'RESTART':
            restart (config)
        else:
            print ("Invalid command")
    else:
        print ("No command provided")
