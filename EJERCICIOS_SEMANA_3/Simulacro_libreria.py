# Initial book inventory (at least 5 books)
inventory = [
    {"title": "The Alchemist", "price": 12.99, "quantity": 10},
    {"title": "1984", "price": 15.50, "quantity": 7},
    {"title": "To Kill a Mockingbird", "price": 18.00, "quantity": 5},
    {"title": "Sapiens", "price": 22.75, "quantity": 4},
    {"title": "The Hobbit", "price": 14.20, "quantity": 6}
]

# Function to add a new book
def add_book():
    title = input("Enter book title: ").strip()
    if any(book['title'].lower() == title.lower() for book in inventory):
        print("Book already exists in the inventory.")
        return

    while True:
        price_input = input("Enter book price: ")
        if price_input.replace('.', '', 1).isdigit() and float(price_input) > 0:
            price = float(price_input)
            break
        else:
            print("Invalid price. Must be a positive number.")

    while True:
        quantity_input = input("Enter quantity: ")
        if quantity_input.isdigit() and int(quantity_input) > 0:
            quantity = int(quantity_input)
            break
        else:
            print("Invalid quantity. Must be a positive integer.")

    inventory.append({"title": title, "price": price, "quantity": quantity})
    print(f"Book '{title}' added successfully.")

# Function to search for a book
def search_book():
    title = input("Enter the book title to search: ").strip()
    for book in inventory:
        if book["title"].lower() == title.lower():
            print(f"Title: {book['title']}")
            print(f"Price: ${book['price']:.2f}")
            print(f"Quantity: {book['quantity']}")
            return
    print("Book not found in inventory.")

# Function to update book price
def update_price():
    title = input("Enter the book title to update price: ").strip()
    for book in inventory:
        if book["title"].lower() == title.lower():
            while True:
                new_price = input("Enter the new price: ")
                if new_price.replace('.', '', 1).isdigit() and float(new_price) > 0:
                    book["price"] = float(new_price)
                    print(f"Price updated for '{title}'.")
                    return
                else:
                    print("Invalid price. Must be a positive number.")
    print("Book not found in inventory.")

# Function to delete a book
def delete_book():
    title = input("Enter the book title to delete: ").strip()
    for book in inventory:
        if book["title"].lower() == title.lower():
            inventory.remove(book)
            print(f"Book '{title}' has been removed from inventory.")
            return
    print("Book not found in inventory.")

# Function to calculate total inventory value using lambda
def calculate_inventory_value():
    total_value = sum(map(lambda book: book["price"] * book["quantity"], inventory))
    print(f"\nTotal inventory value: ${total_value:.2f}\n")

# Interactive menu using match-case
def menu():
    while True:
        print("\n=== Bookstore Inventory Menu ===")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Update Book Price")
        print("4. Delete Book")
        print("5. Calculate Inventory Value")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        match choice:
            case "1":
                add_book()
            case "2":
                search_book()
            case "3":
                update_price()
            case "4":
                delete_book()
            case "5":
                calculate_inventory_value()
            case "6":
                print("Exiting the system.")
                break
            case _:
                print("Invalid option. Please try again.")

# Start the program
menu()
