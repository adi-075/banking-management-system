from rest_framework import serializers
from .models import Customer, Account, Transaction, AccountBalance, InterestRateHistory, Manager, Supervisor, Employee, Branch

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['CustomerID', 'SSN', 'FirstName', 'LastName', 'DOB', 'Email', 'Address', 'Phone', 'CustomerSince', 'Referral']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['AccountID', 'AccountNumber', 'DateOpened', 'Balance', 'Status', 'Customer', 'Branch', 'is_savings', 'is_loan', 'is_checking']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['TransactionID', 'Account', 'TransactionDate', 'Amount', 'Type', 'Description']

class AccountBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountBalance
        fields = ['Account', 'Date', 'Balance']

class InterestRateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestRateHistory
        fields = ['Account', 'Date', 'InterestRate']

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['ManagerID', 'FirstName', 'LastName', 'Position', 'HireDate', 'Department']

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = ['SupervisorID', 'FirstName', 'LastName', 'Position', 'HireDate', 'Department']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['EmployeeID', 'Supervisor', 'FirstName', 'LastName', 'Position', 'HireDate', 'Department']

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['BranchID', 'Name', 'Address', 'Phone', 'Manager']
