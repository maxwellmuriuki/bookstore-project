from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', stock={self.stock})>"

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact = Column(String)

    def __repr__(self):
        return f"<Customer(name='{self.name}', contact='{self.contact}')>"

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    order_date = Column(String, nullable=False)

    customer = relationship('Customer', backref='orders')
    book = relationship('Book', backref='orders')

    def __repr__(self):
        return f"<Order(customer_id={self.customer_id}, book_id={self.book_id})>"
