# Functions go here

def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""
    print(f"{decoration * 3} {statement} {decoration * 3}")

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

def instructions():
    make_statement("Instructions", "ℹ️")

    print('''
For each holder enter:
- Their name
- Their age
- Their payment method (cash/credit)

The program will record the ticket sale and calculate the
ticket cost (and the profit).

Once you have either sold all of the tickets or entered the 
exit code ('xxx'), the program will display the ticket
sales information and write the data to a text file.

It will also choose one lucky ticket holder who wins the 
draw (their ticket is free).
    ''')


# Main routine goes here

yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

make_statement("Mini-movie Fundraiser Program", "🍿")
print()

want_instructions = string_check(
    "Do you want to see the instructions? ",
    yes_no_list,
    1
)

if want_instructions == "yes":
    instructions()

print()
print("Program continues...")

pay_method = string_check("Payment method: ", payment_list, 2)
print(f"You chose {pay_method}")




