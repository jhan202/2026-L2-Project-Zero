import pandas

# lists to hold ticket details
all_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

mini_movie_dict = {
    'Name': all_names,
    'Ticket price': all_tickets_costs,
    'Surcharge': all_surcharges

}

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
print(mini_movie_frame)