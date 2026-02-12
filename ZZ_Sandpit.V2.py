# list exploration / experiment
from traceback import print_tb

fruit_list = ['apple', 'banana', 'cherry', 'dragon fruit']

for item in fruit_list:

    print()

    # print the whole word...
    print("Fruit Name: ", item)

    # print the whole word...
    print("First letter ", item[0])

    # challenge - print the first TWO letter
    print(f"First two letters {item[:3]}")
    
