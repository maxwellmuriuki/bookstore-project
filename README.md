# bookstore-project
Bookstore Inventory Management System

Description

The Bookstore Inventory Management System is a command-line application designed to help manage a bookstore's inventory. It allows users to add books, view available books, place orders, view orders, and delete orders. This system is built with Python and SQLite for efficient data handling and storage.

Features

Add Books: Add new books to the inventory by providing details such as title, author, genre, price, and stock.

View Books: Display all books available in the inventory along with their details.

Place Orders: Allow customers to place orders for books. The stock is automatically updated upon a successful order.

View Orders: View all placed orders with details of the customer and books ordered.

Delete Orders: Delete an existing order from the system.

Installation

Prerequisites

Python 3.8 or later

SQLite (bundled with Python)

Project Structure

bookstore-project/
├── app/
│   ├── __init__.py
│   ├── models.py       # Database models
│   ├── database.py     # Database initialization
│   ├── cli.py          # Command-line interface functions
├── main.py             # Entry point of the application
├── env/                # Virtual environment
└── README.md           # Documentation

Example Workflow

Adding a Book

Select 1 from the main menu.

Enter book details (title, author, genre, price, stock).

Placing an Order

Select 3 from the main menu.

Provide customer details and the book ID.

Viewing Orders

Select 4 from the main menu.

View a list of all orders placed.

Deleting an Order

Select 5 from the main menu.

Provide the ID of the order to delete.

Technologies Used

Programming Language: Python

Database: SQLite (via SQLAlchemy ORM)


