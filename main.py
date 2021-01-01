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
    try:
        tickets_request = int(input('How many tickets would you like to purchase?: '))
        return tickets_request
    except ValueError:
        print('Oops! That was an invalid number. Try again...')


def ticket_confirmation(num_of_tickets):
    while True:
        confirmation_response = input(f'Are you sure that you would like to purchase {num_of_tickets}? (y/n): ')
        purchase_cost = num_of_tickets * 12
        if confirmation_response == 'y':
            print(f'Purchase Confirmation: \n${num_of_tickets} will be{purchase_cost} please...')
            return
        elif confirmation_response == 'n':
            print(f'Cancelling purchase...')
            break
        elif confirmation_response == 'exit':
            print('Okay, come again soon!')
            sys.exit()


def main():
    while True:
        tickets_request = ask_for_ticket_amount()

        ticket_confirmation(tickets_request)


if __name__ == '__main__':
    main()
