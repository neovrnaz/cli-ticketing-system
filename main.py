import sys

tickets_stock = 200
event = 'Monty Python Q&A Session'


def subtract_tickets(curr_ticket_stock, amt_of_tickets):
    return curr_ticket_stock - amt_of_tickets


print('Welcome to the CLI Ticketing System')
print('----------------------\n')

print(f'We are currently selling tickets for the "{event}"')
print(f'Our current ticket stock for this event is: {tickets_stock} tickets\n')


def ask_for_ticket_amount():
    while True:
        try:
            tickets_request = int(input('How many tickets would you like to purchase?: '))
            while tickets_request > tickets_stock:
                print(f'Sorry, we only have {tickets_stock} left. Try again...')
                tickets_request = int(input('How many tickets would you like to purchase?: '))
            return tickets_request
        except ValueError:
            print('Oops! That was an invalid number. Try again...')


def purchase_tickets(tickets):
    response = input('Purchase tickets (p): ')
    if response == 'p':
        print('\nPurchase complete...')
        print(f'Congratulations! You\'ve purchased {tickets} tickets.')
        print('Have a great day!')
        sys.exit()
    else:
        print('goodbye...')
        sys.exit()


def ticket_confirmation(num_of_tickets):
    while True:
        response = input(f'Are you sure that you would like to purchase {num_of_tickets} tickets? (y/n): ')
        purchase_cost = num_of_tickets * 12
        if response == 'y':
            print(f'\n\nPurchase Confirmation:')
            print('---------------')
            print(f'{num_of_tickets} tickets will be ${purchase_cost} please...')
            purchase_tickets(num_of_tickets)
            return
        elif response == 'n':
            print(f'Cancelling purchase...')
            break
        elif response == 'exit':
            print('Okay, come again soon!')
            sys.exit()


def main():
    tickets_request = ask_for_ticket_amount()

    ticket_confirmation(tickets_request)


if __name__ == '__main__':
    main()
