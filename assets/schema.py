from marshmallow import Schema, fields
from .models import Customer, Account, Transaction, AccountBalance, InterestRateHistory, Manager, Supervisor, Employee, Branch

class CustomerSchema(Schema):
    CustomerID = fields.Int()
    SSN = fields.Str()
    FirstName = fields.Str()
    LastName = fields.Str()
    DOB = fields.Date()
    Email = fields.Email()
    Address = fields.Str()
    Phone = fields.Str()
    CustomerSince = fields.Date()
    Referral = fields.Int()

class AccountSchema(Schema):
    AccountID = fields.Int()
    AccountNumber = fields.Str()
    DateOpened = fields.Date()
    Balance = fields.Decimal()
    Status = fields.Str()
    Customer = fields.Int()
    Branch = fields.Int()
    is_savings = fields.Bool()
    is_loan = fields.Bool()
    is_checking = fields.Bool()

class TransactionSchema(Schema):
    TransactionID = fields.Int()
    Account = fields.Int()
    TransactionDate = fields.Date()
    Amount = fields.Decimal()
    Type = fields.Str()
    Description = fields.Str()

class AccountBalanceSchema(Schema):
    Account = fields.Int()
    Date = fields.Date()
    Balance = fields.Decimal()

class InterestRateHistorySchema(Schema):
    Account = fields.Int()
    Date = fields.Date()
    InterestRate = fields.Decimal()

class ManagerSchema(Schema):
    ManagerID = fields.Int()
    FirstName = fields.Str()
    LastName = fields.Str()
    Position = fields.Str()
    HireDate = fields.Date()
    Department = fields.Str()

class SupervisorSchema(Schema):
    SupervisorID = fields.Int()
    FirstName = fields.Str()
    LastName = fields.Str()
    Position = fields.Str()
    HireDate = fields.Date()
    Department = fields.Str()

class EmployeeSchema(Schema):
    EmployeeID = fields.Int()
    Supervisor = fields.Int()
    FirstName = fields.Str()
    LastName = fields.Str()
    Position = fields.Str()
    HireDate = fields.Date()
    Department = fields.Str()

class BranchSchema(Schema):
    BranchID = fields.Int()
    Name = fields.Str()
    Address = fields.Str()
    Phone = fields.Str()
    Manager = fields.Int()
