
file="contact_book.txt"
def load_data():
    data={}
    try:
        with open(file,'r') as f:
            lines=f.readlines()
            data = dict(line.strip().split(":") for line in lines if ":" in line)
    except FileNotFoundError:
        pass
    return data
data=load_data()
def save_data(data):
    with open(file,'w') as f:
        for n, p in data.items():
            f.write(f"{n}:{p}\n")
    
def add_contact():
    global data
    name=input("Enter the Name: ").strip()
    phone=input("Enter the Number: ").strip()
    if name  in data:
        return "Contact existed..."
    data[name]=phone
    save_data(data)
    return "Added Successfully"      
        
def delete_contact():
    global data
    if  not data:
        return "No Contacts"
    name=input("Enter the Contact: ").strip()
    if name not in data:
        return "Contact not found"
    del data[name]
    save_data(data)
    return "Deleted Successfully"

def show_contacts():
    global data
    if not data:
        return "No Contacts to Show"
    print("\n***Contacts***")
    for i in sorted(data.keys()):
        print(f"Contact name: {i} | Number: {data[i]}")
    return f"Total Contacts {len(data)}"
    
def search():
    global data
    if not data:
        return "Contact Book is Empty"
    name=input("Enter the Contact: ").strip()
    if name not in data:
        return "Contact Not Found"
    return f"Contact Found:\nContact Name: {name} | Number: {data[name]}"

print("   ***MENU***   \n0.Exit \n1.Add Contact \n2.Delete Contact \n3.View Contacts \n4.Search Contact")
while True:
    try:
        n=int(input("Enter the operation: "))
    except:
        print("Wrong input...!! Try again")
        continue
    if n==1:
        print(add_contact())
    elif n==2:
        print(delete_contact())
    elif n==3:
        print(show_contacts())
    elif n==4:
        print(search())
    elif n==0:
        print("Good Bye 👋👋")
        break
    else:
        print("Invalid Choice..!!")
