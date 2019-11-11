import cards_tools

# Infinite loop
while True:

    # Print function list
    cards_tools.show_menu()
    action_str = input("Please type in your action: ")
    print("Your action is: %s " % action_str)

    if action_str in ["1", "2", "3"]:

        # Add new name card
        if action_str == "1":
            cards_tools.new_card()
        # Show all name cards
        elif action_str == "2":
            cards_tools.show_all()
        # Find name card
        elif action_str == "3":
            cards_tools.search_card()

    elif action_str == "0":

        print("Have a good day!")
        break
        # pass is used if no codes are not writen yet

    else:
        print("Invalid action, please choose again")