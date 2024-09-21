outer_dict = {}
inner_dict = {}

choice = "yes"
while True:
    if choice == "yes":
        contact_id = int(input("Enter the contact_id: "))
        name = input("Enter the contact_name:")

        ph_choice = []
        ph_number_count = int(input("Enter how many number you want to add: "))
        for i in range(ph_number_count):
            phone_num = int(input("Enter the phone_number:"))
            ph_choice.append(phone_num)

        email = input("Enter the email_id: ")
        inner_dict['Name'] = name
        inner_dict['Phone_number'] = ph_choice
        inner_dict['Email'] = email
        outer_dict[contact_id] = inner_dict
    choice = input("Enter the yes or no for add contact details:")
    if choice == "no":
        break

print(f"Contact Dictionary: {outer_dict}")

operation = int(input("Enter IVR choice:\n1. Add these details to a file\n2. retrieve details from file\n3. update details\n"))
if operation == 1:
    with open("contacts.txt","w") as file:
        for contact_id, details in outer_dict.items():
            file.write(f"Contact ID: {contact_id}\n")
            for key, value in details.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")  # Add a newline for separation between contacts

elif operation == 2:
    with open("contacts.txt",'r') as file:
        data = file.readlines()

    print(data)

# elif operation == 3:


