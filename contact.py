#program for contact book

names = []
contact_numbers = []
emails =[]
addresses=[]
num = int(input("Enter the total number of contacts you want to save: "))
for i in range(num):
    name = input("Name: ")
    contact_number = int(input("Contact Number: ")) 
    email =input("Email: ")
    address=input("Address: ")
    names.append(name)
    contact_numbers.append(contact_number)
    emails.append(email)
    addresses.append(address)
print("\nName\t\t\tContact Number\t\t\tEmail\t\t\t\t\t\tAddress\n")
for i in range(num):
    print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(names[i], contact_numbers[i], emails[i], addresses[i]))
search_term = input("\nEnter search term: ")
print("Search result:")
if search_term in names:
    index = names.index(search_term)
    contact_number = contact_numbers[index]
    email = emails[index]
    adress = addresses[index]
    print("Name: {}, Phone Number: {}, Email: {}, Address= {}".format(search_term, contact_number, email, address))
else:
    print("No records")