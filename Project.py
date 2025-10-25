# Mini Library Management System with Payment-Verified Delivery

library = {
    "The Alchemist": {"available": True, "borrower": None},
    "Atomic Habits": {"available": True, "borrower": None},
    "Python Crash Course": {"available": False, "borrower": {
        "name": "James", "phone": "0551234567", "location": "Accra",
        "delivery": {"method": "Delivery", "paid": True, "fee": 15, "reference": "TXN20251001"}
    }},
    "Think and Grow Rich": {"available": True, "borrower": None}
}

LIBRARIAN_PASSWORD = "library123"
DELIVERY_FEE = 15

# Library payment accounts
MOMO_ACCOUNT = "0555550000 (Library Momo - NOLAP Library)"
BANK_ACCOUNT = "NOLAP Library Bank - 001234567890 (Access Bank)"


def display_books():
    """Show available books without borrower details."""
    print("\n Library Books:")
    for book, info in library.items():
        status = "Available " if info["available"] else "Borrowed "
        print(f" - {book}: {status}")


def borrow_book():
    """Borrow a book with delivery and payment verification."""
    book_name = input("\nEnter the name of the book you want to borrow: ").title()

    if book_name in library:
        if library[book_name]["available"]:
            print("\n Please enter your details before borrowing:")
            name = input(" Full name: ").title()
            phone = input(" Telephone number: ")
            location = input(" Location: ").title()

            print("\n Delivery Options:")
            print("1. Deliver to my location (₵15 fee)")
            print("2. I’ll pick it up from the library")
            choice = input("Choose delivery option (1 or 2): ")

            delivery_method = "Pickup"
            paid_status = None
            payment_reference = None
            fee = 0

            if choice == '1':
                delivery_method = "Delivery"
                fee = DELIVERY_FEE
                print(f"\n Delivery fee is ₵{DELIVERY_FEE}.")
                print("To proceed, please pay using one of the following accounts:")
                print(f" MoMo Account: {MOMO_ACCOUNT}")
                print(f" Bank Account: {BANK_ACCOUNT}")

                paid = input("\nHave you made the payment? (yes/no): ").lower()
                if paid == "yes":
                    payment_reference = input("Enter your payment reference/transaction ID: ").upper()
                    paid_status = True
                    print(" Payment confirmed. Your book will be delivered shortly!")
                else:
                    print("\n You must complete payment before delivery can be processed.")
                    print(" You can visit the library to pick up your book instead.")
                    delivery_method = "Pickup"  # fallback
                    paid_status = False
            else:
                print(" You chose to pick up your book from the library.")

            # Save borrower details
            library[book_name]["available"] = False
            library[book_name]["borrower"] = {
                "name": name,
                "phone": phone,
                "location": location,
                "delivery": {
                    "method": delivery_method,
                    "paid": paid_status,
                    "fee": fee,
                    "reference": payment_reference
                }
            }

            print(f"\n Thank you, {name}! You have successfully borrowed '{book_name}'.")
        else:
            print(f" Sorry, '{book_name}' is already borrowed.")
    else:
        print(" This book is not in our library records.")


def return_book():
    """Return a borrowed book."""
    book_name = input("\nEnter the name of the book you want to return: ").title()
    if book_name in library:
        if not library[book_name]["available"]:
            borrower_name = library[book_name]["borrower"]["name"]
            library[book_name]["available"] = True
            library[book_name]["borrower"] = None
            print(f" Thank you, {borrower_name}, for returning '{book_name}'.")
        else:
            print(f" '{book_name}' was not borrowed.")
    else:
        print(" This book does not exist in our records.")


def add_book():
    """Add new books to the system."""
    book_name = input("\nEnter the name of the new book: ").title()
    if book_name in library:
        print(" This book already exists in the library.")
    else:
        library[book_name] = {"available": True, "borrower": None}
        print(f" '{book_name}' has been added successfully!")


def view_confidential_records():
    """Allow librarian to see all borrower details."""
    password = input("\n Enter librarian password: ")
    if password == LIBRARIAN_PASSWORD:
        print("\n Confidential Borrower & Delivery Records:")
        for book, info in library.items():
            if info["borrower"]:
                b = info["borrower"]
                d = b["delivery"]
                print(f"""
 {book}
   Borrower: {b['name']}
   Phone: {b['phone']}
   Location: {b['location']}
   Delivery: {d['method']}
   Fee: ₵{d['fee']}
   Paid: {d['paid']}
   Reference: {d['reference']}
                """)
        print("\n End of confidential report.")
    else:
        print(" Access denied. Incorrect password.")



def main():
    print(" Welcome to the Library System with Verified Delivery Service!")

    while True:
        print("\n--- MENU ---")
        print("1. View all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Add a new book")
        print("5. View confidential records (Librarian only)")
        print("6. Exit")

        choice = input("\nEnter your choice (1–6): ")

        if choice == '1':
            display_books()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            add_book()
        elif choice == '5':
            view_confidential_records()
        elif choice == '6':
            print(" Thank you for using the library system. Goodbye!")
            break
        else:
            print( "Invalid choice. Please try again.")


main()

