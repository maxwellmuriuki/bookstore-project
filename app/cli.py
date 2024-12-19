from app.database import session
from app.models import Book, Customer, Order
from datetime import datetime

def add_book():
    try:
        title = input("Enter book title: ").strip()
        author = input("Enter book author: ").strip()
        genre = input("Enter book genre: ").strip()
        price = float(input("Enter book price: ").strip())
        stock = int(input("Enter book stock: ").strip())

        book = Book(title=title, author=author, genre=genre, price=price, stock=stock)
        session.add(book)
        session.commit()
        print("Book added successfully!")
    except ValueError:
        print("Invalid input. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_books():
    books = session.query(Book).all()
    if books:
        print("\nAvailable Books:")
        for book in books:
            print(f"ID: {book.id} | Title: {book.title} | Author: {book.author} | Genre: {book.genre} | Price: {book.price} | Stock: {book.stock}")
    else:
        print("\nNo books available.")

def place_order():
    try:
        customer_name = input("Enter customer name: ").strip()
        contact = input("Enter customer contact: ").strip()

        customer = Customer(name=customer_name, contact=contact)
        session.add(customer)
        session.commit()

        book_id = int(input("Enter book ID to order: ").strip())
        book = session.query(Book).get(book_id)

        if book and book.stock > 0:
            order = Order(customer_id=customer.id, book_id=book.id, order_date=datetime.now().strftime("%Y-%m-%d"))
            book.stock -= 1
            session.add(order)
            session.commit()
            print("Order placed successfully!")
        else:
            print("Book is out of stock or not found.")
    except ValueError:
        print("Invalid input. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_orders():
    orders = session.query(Order).all()
    if orders:
        print("\nCurrent Orders:")
        for order in orders:
            print(f"Order ID: {order.id} | Customer: {order.customer.name} | Book: {order.book.title} | Date: {order.order_date}")
    else:
        print("\nNo orders found.")

def delete_order():
    try:
        print("\nCurrent Orders:")
        orders = session.query(Order).all()
        for order in orders:
            print(f"Order ID: {order.id} | Customer: {order.customer.name} | Book: {order.book.title} | Date: {order.order_date}")

        order_id = int(input("\nEnter the ID of the order to delete: ").strip())
        order = session.query(Order).get(order_id)

        if order:
            book = session.query(Book).get(order.book_id)
            if book:
                book.stock += 1

            session.delete(order)
            session.commit()
            print(f"\nOrder ID {order_id} has been deleted successfully!")
        else:
            print("\nOrder not found.")
    except ValueError:
        print("\nInvalid input. Please enter a valid order ID.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
