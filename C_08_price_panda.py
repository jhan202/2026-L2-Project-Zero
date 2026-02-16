import pandas

# Functions go here
def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer."

    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def string_check(question, valid_ans_list=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            if response == item:
                return item

            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# currency formatting function
def currency(x):
    return "${:,.2f}".format(x)


# Main routine starts here

# initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# Ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge (5%)
CREDIT_SURCHARGE = 0.05

# Lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket price': all_ticket_costs,
    'Surcharge': all_surcharges
}

# Main loop
while True:
    print()

    name = not_blank("Name (or 'xxx' to quit): ")

    if name.lower() == "xxx":
        break

    # Ask user for their age and check it's between
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue

    # Child ticket price is $7.50
    elif age < 16:
        ticket_price = CHILD_PRICE

    # Adult ticket ($10.50)
    elif age < 65:
        ticket_price = ADULT_PRICE

    # Senior Citizen ticket price ($6.50)
    elif age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method (cash / credit): ", payment_ans, 2)

    if pay_method == "cash":
        surcharge = 0

    # if paying by credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # Store ticket data
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)


# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total payable & profit for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket price'] - 5

# Work out total paid and total profit
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# Output movie frame without index

print(mini_movie_frame.to_string(index=False))

print()
print(f"Total paid: ${total_paid:.2f}")
print(f"Total profit: ${total_profit:.2f}")
