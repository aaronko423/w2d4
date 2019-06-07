#!/usr/bin/env python3

def main_menu():
    print("\nWelcome to Trader Terminal!")
    print("\n1) create account\n2) log in\n3) quit")
    return input("\nYour choice: ")

def account_creation_menu():
    print("\nAccount Creation Menu\n")
    create_username = input("Username: ")
    Pin1 = input("Password: ")
    Pin2 = input("Confirm Password: ")
    print("\nYour account has been successfully created!")
    return("")

def login_menu():
    print("Please log into your account\n")
    input_username = input("Username: ")
    input_password = input("Password: ")

def account_menu():
    print("\n1) Check money balance\n2) Purchase stocks\n3) Sell stocks\n4) Check stock holdings\n5) Sign out")
    return input("\nYour choice: ")

def purchase_stocks_menu():
    purchased_stocks = input("Insert ticker of stocks you would like to buy: ")
    purchase_quantity = input("Insert quantity of stocks you would like to buy: ")
    return("")

def sell_stocks_menu():
    sold_stocks = input("Insert ticker of stocks you would like to sell: ")
    sold_quantity = input("Insert quantity of stocks you would like to sell: ")
    return("")

def user_quit():
    return("Goodbye!")

if __name__ == "__main__":
    #print(main_menu())
    #print(account_creation_menu())
    #print(login_menu())
    #print(account_menu())
    #print(purchase_stocks_menu())
    #print(sell_stocks_menu())
    #print(user_quit())
