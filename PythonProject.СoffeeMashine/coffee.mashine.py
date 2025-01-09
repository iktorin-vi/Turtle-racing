#TODO-1: Prompt User for Action:
#     Implement a function to ask the user: "What would you like? (espresso/latte/cappuccino):".
#     Include options for "report" to show the status and "off" to turn off the machine.
# chose=input("What would you like? (espresso/latte/cappuccino): ").lower()

#TODO-2: Turn Off the Machine:
#     If the user enters "off", terminate the program.
#
#TODO-3: Generate a Report**:
#     Implement a function to print the current status of resources (water, milk, coffee, money).
#
#TODO-4: Check Resources:
#    Add a function to check if there are enough resources to make the selected drink.
#    If not enough resources, print: "Sorry there is not enough [resource].".
#
#TODO-5: Process Coins:
#    Create a function to handle coin input from the user.
#    Calculate the total value of the inserted coins.
#
#TODO-6: Verify Transaction:
#    Check if the inserted money is enough to pay for the selected drink.
#    If insufficient funds, print: "Sorry that's not enough money. Money refunded.".
#    If extra money is provided, calculate and return change to the user.
#
#TODO-7: Make the Coffee:
#    Implement a function to:
#    Deduct the required resources from the machine.
#    Print: "Here is your [drink]. Enjoy!".
#
#TODO-8: Main Program Loop:
#    Organize the logic into a continuous loop until the user enters "off".
#    Repeat the prompt after each action (e.g., making a drink or showing a report).
#
#TODO-9: Data Structure:
#    Store resources and drink recipes in a structured format, like a dictionary.