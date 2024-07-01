def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(item_name ,shopping_list):
    if not item_name:
        return "Item name Invalid"
    shopping_list.append(item_name)

def remove_item(item_name ,shopping_list):
    if item_name in shopping_list:
        shopping_list.remove(item_name)
    return "Item is not on list"

def display_shopping_list(shopping_list):
    return shopping_list

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            user_input = input("Enter a name of item: ")
            add_item(user_input ,shopping_list)
            # Prompt for and add an item
            pass
        elif choice == '2':
            user_input = input("Enter name of item you want to remove: ")
            remove_item(user_input ,shopping_list)
            # Prompt for and remove an item
            pass
        elif choice == '3':
            print(display_shopping_list(shopping_list))
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()