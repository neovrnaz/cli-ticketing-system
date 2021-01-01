import sys
import bitcoin

tickets_stock = 200
USD_TICKET_PRICE = 14
event = 'Monty Python Q&A Session'
bitcoin_exchange_rate = bitcoin.bitcoin_price()
name = input('What is your name?: ')


def print_welcome():
    if tickets_stock == 0:
        sys.exit('Sorry we\'re all out of tickets!')

    print(f'\nHello {name}!')
    print('\n----------------------\n')
    print('Welcome to the CLI Ticketing System')
    print('----------------------\n')

    print(f'We are currently selling tickets for the {event}')
    print(f'Each ticket costs: ${USD_TICKET_PRICE}\n')


def show_ticket_stock():
    if tickets_stock == 1:
        print('We\'re down to our last ticket!')
    elif 1 < tickets_stock < 100:
        print(f'Buy now! We only have {tickets_stock} tickets remaining!\n')
    elif tickets_stock > 100:
        print(f'There are currently {tickets_stock} tickets remaining.')


def ticket_quantity_request():
    while True:
        try:
            tickets_request = int(input('How many tickets would you like to purchase?: '))
            while tickets_request > tickets_stock:
                print(f'Sorry, we only have {tickets_stock} tickets in stock! Try again...\n')
                tickets_request = int(input('How many tickets would you like to purchase?: '))
            return tickets_request
        except ValueError:
            print('\nOops! That was an invalid number. Try again...')


def calculate_purchase_cost(tickets):
    return tickets * USD_TICKET_PRICE


def usd_to_bitcoin(cost):
    return cost / bitcoin_exchange_rate


def ask_for_payment_method():
    while True:
        try:
            payment_method = input('Will you be paying using a Credit Card or by Bitcoin? (c/b): ')
            if payment_method == 'c':
                print('\nSelected payment method: Credit Card\n')
                return 'usd'
            elif payment_method == 'b':
                print('\nSelected payment method: Bitcoin\n')
                return 'bitcoin'
            else:
                print(f'Hmm... I didn\'t understand {payment_method}')
        except BaseException as e:
            print('Hmm, there was an error: ' + str(e))


def payment_method_symbol(pymt):
    if pymt == 'bitcoin':
        return '฿'
    elif pymt == 'usd':
        return '$'


def cost_string(symbol, cost):
    return f'{symbol}{cost}'


def cost_string_after_considering_payment_method(tickets, payment_method):
    usd_cost = calculate_purchase_cost(tickets)
    currency_symbol = payment_method_symbol(payment_method)
    if payment_method == 'usd':
        return cost_string(currency_symbol, usd_cost)
    elif payment_method == 'bitcoin':
        cost_in_bitcoin = usd_to_bitcoin(usd_cost)
        return cost_string(currency_symbol, cost_in_bitcoin)


def confirm_purchase(tickets, string):
    while True:
        response = input(f'You are purchasing {tickets} tickets for {string}. '
                         f'\nIs this order correct? (y/n): ')
        if response == 'y':
            purchase_tickets(tickets, string)
            return tickets
        elif response == 'n':
            print(f'Cancelling order...')
            break
        elif response == ('exit' or 'e' or 'c' or 'cancel'):
            print('Your order was canceled')
            sys.exit()
        else:
            print(f'\nHmm, I don\'t recognize the option "{response}"...\n')


def purchase_tickets(tickets, string):
    response = input('Purchase tickets (p): ')
    if response == 'p':
        print('\nPurchase complete...')

        print(f'\n\nPurchase Confirmation for {name}:')
        print('---------------')
        print(f'Your payment of {string} was received.')
        print('\n***')
        print(f'Congratulations! You now have {tickets} tickets to the "{event}"')
        print('***')
        sys.exit()
    else:
        print('goodbye...')
        sys.exit()


def payment_process():
    ticket_quantity = ticket_quantity_request()
    payment_method = ask_for_payment_method()
    show_cost = cost_string_after_considering_payment_method(ticket_quantity, payment_method)
    confirm_purchase(ticket_quantity, show_cost)
    purchase_tickets(ticket_quantity, show_cost)
    return


def main():

    print_welcome()
    show_ticket_stock()
    payment_process()


if __name__ == '__main__':
    main()
