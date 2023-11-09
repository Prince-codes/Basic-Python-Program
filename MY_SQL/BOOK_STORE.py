import os
import pickle
from time import *

print("\n**********Welcome to BOOK STORE********\n")
print()

# Customer Details
cus_name = input("Enter Customer Name: ")

cus_id = input("Enter Customer Id: ")

# Receipt Details
bill_no = input("Enter bill no.: ")
print()

# - Discount
print("\n---------------------------------------------------")
print()
print("Hello", cus_name, "!")
print("\nWe are giving great discount aplicable on your purchase!")
print("Discount applicable as follows:")
print("On purchase above:")
print("Rs 2000 - 5% discount")
print("Rs 5000 - 10% discount")
print("Rs 10000 - 20% discount")
print("So ,let's start shopping!\n")
print()
print("--------------------------------------------------\n")

# Creating a list to store shopping items
shopping_items = []


# Shopping function
def shopping():
  while True:
    try:
      item_id = int(input("Enter item id: "))
      item_name = input("Enter item name: ")
      item_price = float(input("Enter item price: "))
      item_quantity = int(input("Enter quantity: "))
      item_cost = item_price * item_quantity

      item = {
          "ITEM Id": item_id,
          "ITEM NAME": item_name,
          "ITEM PRICE": item_price,
          "ITEM QUANTITY": item_quantity,
          "COST": item_cost,
      }

      shopping_items.append(item)
      save_items()
      ch = input("Do you wish to continue? Type 'Y' for YES, 'N' for NO : ")
      if ch.upper() == "N":
        break
    except:
      print("-----------------------")
      print("Invalid Inputs")
      ch = input(
          "Do you wish to continue? Type Any key for YES, 'N' for NO : ")
      if ch.lower() == "n":
        break
      print("-----------------------")


# Saving items to a binary file
def save_items():
  with open("shopping_items.dat", "ab") as file:
    pickle.dump(shopping_items, file)
  print("\nYour cart is Updated!\n")


# Reading items from the binary file
def read_items():
  if os.path.exists("shopping_items.dat"):
    with open("shopping_items.dat", "rb") as file:
      shopping_items.extend(pickle.load(file))


# Show items
def show_items():
    with open("shopping_items.dat", "rb") as file:
        while True:
            try:
                itm=pickle.load(file)
                for i in itm:
                    print(i)
            except EOFError:
                break


# Count items
def count_items():
  count = len(shopping_items)
  print("Total number of items:", count)


# Search item
def search_item():
  print()
  try:
    search_name = input("Enter item name to search: ").lower()
    found_items = [
        item for item in shopping_items
        if item["ITEM NAME"].lower() == search_name
    ]
    for i in range(1, 4):
      print("Searching" + "." * i)
      sleep(0.5)
    print()
    if found_items:
      print("Item found:")
      for item in found_items:
        print(item)
      print("----------------")
    else:
      print("Item not found")
      print()
  except:
    print("-----------------------")
    print("Invalid Inputs")
    ch = input("Do you wish to continue? Type Any key for YES, 'N' for NO : ")
    if ch.lower() == "n":
      pass
    else:
      search_item()
    print("-----------------------")


# Delete item
def delete_item():
  try:
    delete_id = int(input("Enter item id to delete: "))
    for item in shopping_items:
      if item["ITEM Id"] == delete_id:
        shopping_items.remove(item)
        print("\nItem deleted\n")
        return

    print("n\Item not foundn\n")
  except:
    print("-----------------------")
    print("\nInvalid Inputs\n")
    ch = input("Do you wish to continue? Type Any key for YES, 'N' for NO : ")
    if ch.lower() == "n":
      pass
    else:
      delete_item()
    print("-----------------------")


# Update item
def update_item():
  try:
    update_id = int(input("Enter item id to update: "))
    for item in shopping_items:
      if item["ITEM Id"] == update_id:
        item_name = input("Enter new item name: ")
        item_price = float(input("Enter new item price: "))
        item_quantity = int(input("Enter new quantity: "))
        item_cost = item_price * item_quantity

        item["ITEM NAME"] = item_name
        item["ITEM PRICE"] = item_price
        item["ITEM QUANTITY"] = item_quantity
        item["COST"] = item_cost

        print("\nItem updated\n")
        return
    print("\nItem not found\n")
    print()
    print("---------------------------------------")
  except:
    ch = input("Do you wish to continue? Type Any key for YES, 'N' for NO : ")
    if ch.lower() == "n":
      pass
    else:
      update_item()


# Add item
def add_item():
  try:
    item_id = int(input("Enter item id: "))
    item_name = input("Enter item name: ")
    item_price = float(input("Enter item price: "))
    item_quantity = int(input("Enter quantity: "))
    item_cost = item_price * item_quantity

    item = {
        "ITEM Id": item_id,
        "ITEM NAME": item_name,
        "ITEM PRICE": item_price,
        "ITEM QUANTITY": item_quantity,
        "COST": item_cost,
    }

    shopping_items.append(item)

    print("Item added")
  except:
    print("-----------------------")
    print("Invalid Inputs")
    ch = input("Do you wish to continue? Type Any key for YES, 'N' for NO : ")
    if ch.lower() == "n":
      pass
    else:
      add_item()
    print("-----------------------")


# Sort item
def sort_item():
  print("Items Before Sorting:-")
  print()
  for item in shopping_items:
    print(item)
  shopping_items.sort(key=lambda x: x["ITEM Id"])
  print("Items sorted")
  print("Items after Sorting:- ")
  for item in shopping_items:
    print(item)
  print("---------------------------------------------")


# Bill out
def bill_out():
  print("/n*****Receipt*****")
  print("Customer details:")
  print("Name:", cus_name)
  print("Id:", cus_id)
  print("Bill No.:", bill_no)
  print("Date:", strftime("%Y-%m-%d"))
  print("Time:", strftime("%H:%M:%S"))
  print("Items purchased:")
  for item in shopping_items:
    print(item)
  print()
  print("/nThank you for shopping!")
  print("***********/n")


# Main menu
def menu():
  print("\n1. shopping")
  print("2. show items")
  print("3. count items")
  print("4. search item")
  print("5. delete item")
  print("6. update item")
  print("7. add item")
  print("8. sort item")
  print("9. billing and logging out\n")


# Loading items when the program starts
read_items()

while True:
  print()
  print("\n******MENU*********\n")
  menu()
  try:
    choice = int(input("Enter your choice: "))
    if choice == 1:
      shopping()
      # Save items to the binary file after shopping
    elif choice == 2:
      show_items()
      print()
    elif choice == 3:
      count_items()
      print()
    elif choice == 4:
      search_item()
      print()
    elif choice == 5:
      delete_item()
      print()
    elif choice == 6:
      update_item()
      print()
    elif choice == 7:
      add_item()
      print()
    elif choice == 8:
      sort_item()
      print()
    elif choice == 9:
      bill_out()
      print()
      save_items()
      print()# Save items to the binary file before logging out
      break
    else:
      print("In Valid Input")
  except Exception as e:
    print("Try Again")

#Finished.
