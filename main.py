import sys
import bitcoin

tickets_stock = 10
USD_ticket_cost = 14
event = 'Monty Python Q&A Session'
bitcoin_exchange_rate = bitcoin.bitcoin_price()


def show_ticket_stock():
    if tickets_stock > 100:
        print(f'There are currently {tickets_stock} tickets remaining.')
    elif tickets_stock < 50:
        print(f'Buy now! We only have {tickets_stock} tickets remaining!\n')
    elif tickets_stock == 1:
        print(f'We\'re down to our last ticket!')
    elif tickets_stock == 0:
        print(f'Sorry we\'re all out of tickets!')


def ticket_quantity_request():
    while True:
        try:
            tickets_request = int(input('How many tickets would you like to purchase?: '))
            while tickets_request > tickets_stock:
                print(f'Sorry, we only have {tickets_stock} tickets in stock. Try again...\n')
                tickets_request = int(input('How many tickets would you like to purchase?: '))
            return tickets_request
        except ValueError:
            print('Oops! That was an invalid number. Try again...')


def calculate_purchase_cost(tickets):
    return tickets * USD_ticket_cost


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
        except BaseException as e:
            print('Hmm, there was an error: ' + str(e))


def payment_method_symbol(pymt):
    if pymt == 'bitcoin':
        return '฿'
    elif pymt == 'usd':
        return '$'


def cost_as_string(symbol, cost):
    return f'{symbol}{cost}'


# def payment_method_to_string(usd_cost, payment_method):
#     if payment_method == 'usd':
#         cost_in_usd = usd_to_bitcoin(usd_cost)
#         payment_method_usd = cost_as_string(payment_method, cost_in_usd)
#         return payment_method_usd
#     elif payment_method == 'bitcoin':
#         cost_in_bitcoin = usd_to_bitcoin(usd_cost)
#         payment_method_bitcoin = cost_as_string(payment_method, cost_in_bitcoin)
#         return payment_method_bitcoin


def payment_method_to_string(tickets, payment_method):
    usd_cost = calculate_purchase_cost(tickets)
    if payment_method == 'usd':
        return cost_as_string(payment_method, usd_cost)
    elif payment_method == 'bitcoin':
        cost_in_bitcoin = usd_to_bitcoin(usd_cost)
        return cost_as_string(payment_method, cost_in_bitcoin)


def purchase_tickets(tickets, pur_formatted):
    response = input('Purchase tickets (p): ')
    if response == 'p':
        print('\nPurchase complete...')
        print(f'Congratulations! You have purchased {tickets} tickets for {pur_formatted}')
        print('\nHave a nice day!')
        sys.exit()
    else:
        print('goodbye...')
        sys.exit()


def purchase_confirmation(num_of_tickets, purchase_string):
    while True:
        response = input(f'Are you sure that you would like to purchase '
                         f'{num_of_tickets} tickets for {purchase_string}? (y/n): ')
        if response == 'y':
            print(f'\n\nPurchase Confirmation:')
            print('---------------')
            purchase_tickets(num_of_tickets, purchase_string)
            return num_of_tickets
        elif response == 'n':
            print(f'Cancelling purchase...')
            break
        elif response == 'exit':
            print('Okay, come again soon!')
            sys.exit()


def main():
    print('Welcome to the CLI Ticketing System')
    print('----------------------\n')

    print(f'We are currently selling tickets for the {event}')

    show_ticket_stock()

    amount_of_tickets_requested = ticket_quantity_request()
    payment_method = ask_for_payment_method()
    symbol = payment_method_symbol(payment_method)
    cost_in_usd = calculate_purchase_cost(amount_of_tickets_requested)
    payment_method_string = payment_method_to_string(cost_in_usd, payment_method)

    purchase_confirmation(amount_of_tickets_requested, payment_method_string)
    purchase_tickets(amount_of_tickets_requested, payment_method_string)


if __name__ == '__main__':
    main()
