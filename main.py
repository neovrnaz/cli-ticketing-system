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
        print(f'Hurry! We only have {tickets_stock} tickets remaining!')
    elif tickets_stock == 1:
        print(f'We\'re down to our last ticket!')
    elif tickets_stock == 0:
        print(f'Sorry we\'re all out of tickets!')


def calculate_purchase_cost(tickets):
    return tickets * USD_ticket_cost


def bitcoin_to_usd(cost):
    return cost / bitcoin_exchange_rate


def method_of_payment():
    while True:
        try:
            method = input('Will you be paying using a Credit Card or by Bitcoin? (c/b): ')
            if method == 'c':
                print('Selected payment method: Credit Card\n')
                return 'dollar'
            elif method == 'b':
                print('Selected payment method: Bitcoin\n')
                return 'bitcoin'
        except BaseException as e:
            print('Hmm, there was an error: ' + str(e))


def payment_method_symbol(pymt):
    if pymt == 'bitcoin':
        return '฿'
    elif pymt == 'dollar':
        return '$'


def format_purchase(pur_method, cost):
    return f'{pur_method}{cost}'


def ask_for_ticket_amount():
    while True:
        try:
            tickets_request = int(input('How many tickets would you like to purchase?: '))
            while tickets_request > tickets_stock:
                print(f'Sorry, we only have {tickets_stock} tickets in stock. Try again...\n')
                tickets_request = int(input('How many tickets would you like to purchase?: '))
            return tickets_request
        except ValueError:
            print('Oops! That was an invalid number. Try again...')


def purchase_confirmation(num_of_tickets, pur_formatted):
    while True:
        response = input(f'Are you sure that you would like to purchase '
                         f'{num_of_tickets} tickets for {pur_formatted}? (y/n): ')
        if response == 'y':
            print(f'\n\nPurchase Confirmation:')
            print('---------------')
            return num_of_tickets
        elif response == 'n':
            print(f'Cancelling purchase...')
            break
        elif response == 'exit':
            print('Okay, come again soon!')
            sys.exit()


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


def main():
    print('Welcome to the CLI Ticketing System')
    print('----------------------\n')

    print(f'We are currently selling tickets for the {event}')

    show_ticket_stock()

    tickets_request = ask_for_ticket_amount()
    payment_method = method_of_payment()
    payment_method_symbol = payment_method_symbol(payment_method)

    cost_in_usd = calculate_purchase_cost(tickets_request)
    purchase_formatted = format_purchase(payment_method_symbol, cost_in_usd)

    number_of_tickets_requested = purchase_confirmation(tickets_request, purchase_formatted)

    purchase_tickets(number_of_tickets_requested, purchase_formatted)


if __name__ == '__main__':
    main()
