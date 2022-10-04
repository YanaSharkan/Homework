import pickle


running = True

#------------------------------------------------------------------------------
phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50,
               "phone_number":"+380501234567", "date_of_birth":"10.10.1972"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15,
               "phone_number":"+380507654321", "date_of_birth":"10.10.2007"},
             ]


#------------------------------------------------------------------------------
def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print ("| Phone:   %20s |" % entry["phone_number"])
    print ("| Date of birth: %14s |" % entry["date_of_birth"])


#------------------------------------------------------------------------------
def print_phonebook_header():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()


#------------------------------------------------------------------------------
def print_phonebook_entries(entries):
    number = 1
    for entry in entries:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
def print_phonebook():
    print_phonebook_header()
    print_phonebook_entries(phone_book)


#------------------------------------------------------------------------------
def find_entry_by_field_phonebook(field_name, field_value):
    found = False
    idx = 1
    for entry in phone_book:
        if entry[field_name] == field_value:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def add_entry_phonebook():
    surname = input("    Enter surname: ")
    name    = input("    Enter name: ")
    age     = int(input("    Enter age: "))
    phone_number   = input("    Enter phone num.: ")

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    phone_book.append(entry)


#------------------------------------------------------------------------------
def printError(message):
    print ("ERROR: %s" % message)


#------------------------------------------------------------------------------
def printInfo(message):
    print ("INFO: %s" % message)


#------------------------------------------------------------------------------
def find_entry_name_phonebook():
    name = str(input("    Enter name: "))
    find_entry_by_field_phonebook("name", name)


#------------------------------------------------------------------------------
def find_entry_age_phonebook():
    age = int(input("    Enter age: "))
    find_entry_by_field_phonebook("age", age)


#------------------------------------------------------------------------------
def delete_entry_name_phonebook():
    name = str(input("    Enter name: "))
    count = 0
    for i, entry in enumerate(phone_book):
        if entry["name"] == name:
            phone_book.pop(i)
            count += 1
    if count == 0:
        printError("Not found!!")
    else:
        print(f"Number of contacts removed: {count}")


#------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print("Total number of entries: ", len(phone_book))


#------------------------------------------------------------------------------
def print_phonebook_by_age():
    print_phonebook_header()

    sorted_by_age = sorted(phone_book, key=lambda x: x["age"])
    print_phonebook_entries(sorted_by_age)



#------------------------------------------------------------------------------
def increase_age():
    age_increase = int(input("    Enter number to increase: "))
    for entry in phone_book:
        entry["age"] += age_increase
    print("Ages were increased for all contacts!")
    print_phonebook_by_age()




#------------------------------------------------------------------------------
def avr_age_of_all_persons():
    ages = []
    average = 0
    for entry in phone_book:
        ages.append(entry["age"])

    if len(phone_book) > 0:
        average = sum(ages) / len(phone_book)

    print(f"Average age is: {average}")


#------------------------------------------------------------------------------
def change_phone_number():
    name = input("    Enter a name, for which you want to change number: ")
    phone_number = input("    Enter new phone number: +380")
    check_number = phone_number[0:4]
    has_phone_code = check_number != "+380"

    if not has_phone_code:
        phone_number = "+380" + phone_number

    found = False
    for entry in phone_book:
        if entry["name"] == name:
            found = True
            entry["phone_number"] = phone_number
            print(f"Phone number of {name} was changed!")
    if found is False:
        printError("Not found!!")


#------------------------------------------------------------------------------
def find_by_date_birth():
    date = input("    Enter date of birth (dd.mm.yyyy): ")
    name = input("    Enter name (optional): ")

    idx = 1
    found = False
    for entry in phone_book:
        if (len(name) == 0 or entry["name"] == name) and entry["date_of_birth"] == date:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")





#------------------------------------------------------------------------------
def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


#------------------------------------------------------------------------------
def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


#------------------------------------------------------------------------------
def exit():
      global running
      running = False


#------------------------------------------------------------------------------
def print_prompt():
      print()
      print()
      print()
      print("~ Welcome to phonebook ~")
      print("Select one of actions below:")
      print("     1 - Print phonebook entries")
      print("     2 - Print phonebook entries (by age)")
      print("     3 - Add new entry")
      print("     4 - Find entry by name")
      print("     5 - Find entry by age")
      print("     6 - Delete entry by name")
      print("     7 - The number of entries in the phonebook")
      print("     8 - Avr. age of all persons")
      print("     9 - Increase age by num. of years")
      print("     10 - Change phone number")
      print("     11 - Find by date of birth")
      print("-----------------------------")
      print("     s - Save to file")
      print("     l - Load from file")
      print("     0 - Exit")
      print()


#------------------------------------------------------------------------------
def main():

    while running:
        try:

            menu = {
                  '1':  print_phonebook,
                  '2':  print_phonebook_by_age,
                  '3':  add_entry_phonebook,
                  '4':  find_entry_name_phonebook,
                  '5':  find_entry_age_phonebook,
                  '6':  delete_entry_name_phonebook,
                  '7':  count_all_entries_in_phonebook,
                  '8':  avr_age_of_all_persons,
                  '9':  increase_age,
                  '10': change_phone_number,
                  '11': find_by_date_birth,

                  '0':  exit,
                  's':  save_to_file,
                  'l':  load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()