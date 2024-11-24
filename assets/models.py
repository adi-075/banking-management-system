from django.db import models
from django.core.validators import RegexValidator

class Customer(models.Model):
    CustomerID = models.IntegerField(primary_key=True)
    SSN = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DOB = models.DateField()
    Email = models.EmailField(max_length=100)
    Address = models.CharField(max_length=255)
    Phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        help_text="Phone number should be in the format: +999999999. Up to 15 digits allowed."
    )
    CustomerSince = models.DateField()

    # Referral relationship
    Referral = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='referrals')

class Account(models.Model):
    AccountID = models.IntegerField(primary_key=True)
    AccountNumber = models.CharField(max_length=50)
    DateOpened = models.DateField()
    Balance = models.DecimalField(max_digits=15, decimal_places=2)
    Status = models.CharField(max_length=50)

    # Relationships
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='accounts')
    Branch = models.ForeignKey('Branch', on_delete=models.CASCADE, related_name='accounts')

    # Account Types
    is_savings = models.BooleanField(default=False)
    is_loan = models.BooleanField(default=False)
    is_checking = models.BooleanField(default=False)

    def __str__(self):
        return f"Account {self.AccountNumber}"

class Transaction(models.Model):
    TransactionID = models.AutoField(primary_key=True)
    Account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    TransactionDate = models.DateField()
    Amount = models.DecimalField(max_digits=15, decimal_places=2)
    Type = models.CharField(max_length=50)  # E.g., 'Deposit', 'Withdrawal', etc.
    Description = models.CharField(max_length=255)

    def __str__(self):
        return f"Transaction {self.TransactionID}"

class AccountBalance(models.Model):
    Account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='balance')
    Date = models.DateField()
    Balance = models.DecimalField(max_digits=15, decimal_places=2)

class InterestRateHistory(models.Model):
    Account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='interest_rate_history')
    Date = models.DateField()
    InterestRate = models.DecimalField(max_digits=5, decimal_places=2)

class Manager(models.Model):
    ManagerID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    HireDate = models.DateField()
    Department = models.CharField(max_length=100)

class Supervisor(models.Model):
    SupervisorID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    HireDate = models.DateField()
    Department = models.CharField(max_length=100)

class Employee(models.Model):
    EmployeeID = models.IntegerField(primary_key=True)
    Supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, related_name='employees')
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    HireDate = models.DateField()
    Department = models.CharField(max_length=100)

class Branch(models.Model):
    BranchID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        help_text="Phone number should be in the format: +999999999. Up to 15 digits allowed."
    )
    Manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
