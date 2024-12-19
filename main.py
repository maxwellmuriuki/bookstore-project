from app.database import initialize_database
from app.cli import add_book, view_books, place_order, view_orders,delete_order

def main():
    initialize_database()
    
    while True:
        print("\nBookstore Inventory Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Place Order")
        print("4. View Orders")
        print("5. Delete Order")  # New option
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            place_order()
        elif choice == "4":
            view_orders()
        elif choice == "5":  
            delete_order()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
