from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Date, Boolean, Decimal

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'
    CustomerID = db.Column(Integer, primary_key=True)
    SSN = db.Column(String(100))
    FirstName = db.Column(String(100))
    LastName = db.Column(String(100))
    DOB = db.Column(Date)
    Email = db.Column(String(100))
    Address = db.Column(String(255))
    Phone = db.Column(String(15))  # No direct regex validation in SQLAlchemy
    CustomerSince = db.Column(Date)

    # Relationships
    referrals = relationship('Customer', backref='referral', remote_side=[CustomerID])

class Account(db.Model):
    __tablename__ = 'accounts'
    AccountID = db.Column(Integer, primary_key=True)
    AccountNumber = db.Column(String(50))
    DateOpened = db.Column(Date)
    Balance = db.Column(Decimal(15, 2))
    Status = db.Column(String(50))

    # Relationships
    customer_id = db.Column(Integer, db.ForeignKey('customers.CustomerID'))
    customer = relationship('Customer', backref='accounts')
    branch_id = db.Column(Integer, db.ForeignKey('branches.BranchID'))
    branch = relationship('Branch', backref='accounts')

    # Account Types
    is_savings = db.Column(Boolean, default=False)
    is_loan = db.Column(Boolean, default=False)
    is_checking = db.Column(Boolean, default=False)

    def __str__(self):
        return f"Account {self.AccountNumber}"

class Transaction(db.Model):
    __tablename__ = 'transactions'
    TransactionID = db.Column(Integer, primary_key=True, autoincrement=True)
    AccountID = db.Column(Integer, db.ForeignKey('accounts.AccountID'))
    account = relationship('Account', backref='transactions')
    TransactionDate = db.Column(Date)
    Amount = db.Column(Decimal(15, 2))
    Type = db.Column(String(50))  # E.g., 'Deposit', 'Withdrawal', etc.
    Description = db.Column(String(255))

    def __str__(self):
        return f"Transaction {self.TransactionID}"

class AccountBalance(db.Model):
    __tablename__ = 'account_balances'
    AccountID = db.Column(Integer, db.ForeignKey('accounts.AccountID'), primary_key=True)
    account = relationship('Account', backref='balance')
    Date = db.Column(Date)
    Balance = db.Column(Decimal(15, 2))

class InterestRateHistory(db.Model):
    __tablename__ = 'interest_rate_histories'
    AccountID = db.Column(Integer, db.ForeignKey('accounts.AccountID'), primary_key=True)
    account = relationship('Account', backref='interest_rate_history')
    Date = db.Column(Date)
    InterestRate = db.Column(Decimal(5, 2))

class Manager(db.Model):
    __tablename__ = 'managers'
    ManagerID = db.Column(Integer, primary_key=True)
    FirstName = db.Column(String(100))
    LastName = db.Column(String(100))
    Position = db.Column(String(100))
    HireDate = db.Column(Date)
    Department = db.Column(String(100))

class Supervisor(db.Model):
    __tablename__ = 'supervisors'
    SupervisorID = db.Column(Integer, primary_key=True)
    FirstName = db.Column(String(100))
    LastName = db.Column(String(100))
    Position = db.Column(String(100))
    HireDate = db.Column(Date)
    Department = db.Column(String(100))

class Employee(db.Model):
    __tablename__ = 'employees'
    EmployeeID = db.Column(Integer, primary_key=True)
    SupervisorID = db.Column(Integer, db.ForeignKey('supervisors.SupervisorID'))
    supervisor = relationship('Supervisor', backref='employees')
    FirstName = db.Column(String(100))
    LastName = db.Column(String(100))
    Position = db.Column(String(100))
    HireDate = db.Column(Date)
    Department = db.Column(String(100))

class Branch(db.Model):
    __tablename__ = 'branches'
    BranchID = db.Column(Integer, primary_key=True)
    Name = db.Column(String(255))
    Address = db.Column(String(255))
    Phone = db.Column(String(15))
    ManagerID = db.Column(Integer, db.ForeignKey('managers.ManagerID'))
    manager = relationship('Manager', backref='branches')

    def __str__(self):
        return self.Name
