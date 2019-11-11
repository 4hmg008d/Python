# Record all name cards
card_list = []


def show_menu():
    """Show function list"""
    print("*" * 50)
    print("Welcome to Name [Card Management System] V 1.0\n")
    print("1. Add new name card")
    print("2. Show all name cards")
    print("3. Find name card\n")

    print("0. Exit")
    print("*" * 50)


def new_card():
    """Add new name card"""
    print("-" * 50)
    print("Add new name card")

    # 1. ask user to fill in name card details
    name_str = input("Please type in name: ")
    phone_str = input("Please type in phone number: ")
    qq_str = input("Please type in qq number: ")
    email_str = input("Please type in email: ")
    # 2. setup a dictionary key
    card_dict = {"Name": name_str,
                 "Phone": phone_str,
                 "QQ": qq_str,
                 "Email": email_str}

    # 3. add name card into list
    card_list.append(card_dict)
    print(card_list)

    # 4. inform user that the new name card has been successfully added
    print("Successfully added name card for %s" % name_str)


def show_all():
    """Show all name cards"""
    print("-" * 50)
    print("Show all name cards")

    # determine if name exists, if not, inform user and return
    if len(card_list) == 0:
        print("No any records now, please add one first!")

        # return will stop the function
        return

    # print table header
    for name in ["Name", "Phone", "QQ", "Email"]:
        print(name, end="\t\t")
    print("")

    # print separator line
    print("=" * 50)

    # loop through all name cards
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["Name"],
                                        card_dict["Phone"],
                                        card_dict["QQ"],
                                        card_dict["Email"]))


def search_card():
    """Find name card"""
    print("-" * 50)
    print("Find name card")

    # 1. ask user to type the name to search
    find_name = input("Please type the name you want to search: ")

    # 2. loop through list and show result
    for card_dict in card_list:
        if card_dict["Name"] == find_name:
            for name in ["Name", "Phone", "QQ", "Email"]:
                print(name, end="\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["Name"],
                                            card_dict["Phone"],
                                            card_dict["QQ"],
                                            card_dict["Email"]))
            edit_card(card_dict)
            break

    else:
        print("Sorry, could not find %s" % find_name)


def edit_card(find_dict):

    action_str = input("Please type your action: "
                       "[1] Edit / [2] Delete / [0] Return to last menu ")

    if action_str == "1":
        find_dict["Name"] = input_card_info(find_dict["Name"], "Name: ")
        find_dict["Phone"] = input_card_info(find_dict["Phone"], "Phone: ")
        find_dict["QQ"] = input_card_info(find_dict["QQ"], "QQ: ")
        find_dict["Email"] = input_card_info(find_dict["Email"], "Email: ")
        print("Edit name card")

    elif action_str == "2":
        card_list.remove(find_dict)
        print("Successfully deleted name card! ")


def input_card_info(dict_value, tip_message):
    # 1. inform user to input
    result_str = input(tip_message)

    # 2. if input is not empty, show results
    if len(result_str) > 0:
        return result_str

    # 3. if no input, return original value
    else:
        return dict_value