# Initial inventory
inventory = [
    {"title": "Book 1", "price": 10.0, "quantity": 100},
    {"title": "Book 2", "price": 15.0, "quantity": 50},
    {"title": "Book 3", "price": 20.0, "quantity": 30},
    {"title": "Book 4", "price": 25.0, "quantity": 10},
    {"title": "Book 5", "price": 30.0, "quantity": 5}
]

def menu():
    print("\nWelcome to Bookstore")
    print(" 1. Add book")
    print(" 2. Search book")
    print(" 3. Update price")
    print(" 4. Delete book")
    print(" 5. Total inventory value")
    print(" 6. Exit")

def add_book(title, price, quantity):
    for book in inventory:
        if book["title"] == title:
            book["quantity"] += quantity
            print(f"Book '{title}' already exists. Quantity updated to {book['quantity']}.")
            return
    inventory.append({"title": title, "price": price, "quantity": quantity})
    print(f"Book '{title}' added successfully.")

def search_book(title):
    for book in inventory:
        if book["title"] == title:
            print(f"Title: {book['title']}, Price: ${book['price']:.2f}, Quantity: {book['quantity']}")
            return book
    print(f"The book '{title}' is not in the inventory.")
    return None

def update_price(title, new_price):
    for book in inventory:
        if book["title"] == title:
            book["price"] = new_price
            print(f"The price of '{title}' has been updated to ${new_price:.2f}.")
            return
    print(f"The book '{title}' is not in the inventory.")

def delete_book(title):
    for book in inventory:
        if book["title"] == title:
            inventory.remove(book)
            print(f"The book '{title}' has been deleted from the inventory.")
            return True
    print(f"The book '{title}' is not in the inventory.")
    return False

def calculate_total():
    return sum(book["price"] * book["quantity"] for book in inventory)

# Main loop
while True:
    menu()
    option_str = input("Enter the desired option: ").strip()
    
    if not option_str.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    option = int(option_str)

    match option:
        case 1:
            try:
                title = input("Enter the title of the book: ").strip()
                if not title:
                    raise ValueError("The title cannot be empty.")
                price = float(input("Enter the price: "))
                if price < 0:
                    raise ValueError("Price cannot be negative.")
                quantity = int(input("Enter the quantity: "))
                if quantity < 0:
                    raise ValueError("Quantity cannot be negative.")
                add_book(title, price, quantity)
            except ValueError as e:
                print(f"Error: {e}")

        case 2:
            title = input("Enter the title to search: ").strip()
            if title:
                search_book(title)
            else:
                print("Title cannot be empty.")

        case 3:
            try:
                title = input("Enter the book title to update: ").strip()
                if not title:
                    raise ValueError("Title cannot be empty.")
                new_price = float(input("Enter the new price: "))
                if new_price < 0:
                    raise ValueError("Price cannot be negative.")
                update_price(title, new_price)
            except ValueError as e:
                print(f"Error: {e}")

        case 4:
            title = input("Enter the book title to delete: ").strip()
            if title:
                delete_book(title)
            else:
                print("Title cannot be empty.")

        case 5:
            total = calculate_total()
            print(f"Total inventory value: ${total:.2f}")

        case 6:
            print("Exiting the program. Goodbye!")
            break

        case _:
            print("Invalid option. Please choose a number from the menu.")
