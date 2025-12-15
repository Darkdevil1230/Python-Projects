file="students.txt"
def load_data():
    data={}
    try:
        with open(file,'r') as f:
            lines=f.readlines()
            for line in lines:
                if "|" in line.strip() and line:
                    roll,name,marks=line.split("|")
                    marks=list(map(int,marks.split(",")))
                    roll,name=roll.strip(),name.strip()
                    data[roll]={"name":name,"marks":marks}
    except FileNotFoundError:
        pass
    return data

def save_data(data):
    with open(file,'w') as f:
        for i in sorted(data.keys()):
            f.write(f"{i}|{data[i]['name']}|{','.join(map(str, data[i]['marks']))}\n")

def calculate_grade(marks):
    total=sum(marks)
    avg=round(total/3,2)
    grade=''
    if avg>=90:     grade='O'
    elif 90>avg>=80:   grade='A'
    elif 80>avg>=70:   grade='B'
    elif 70>avg>=60:   grade='C'
    elif 60>avg>=50:   grade='D'
    else:    grade='Fail'
    return total,avg,grade

def add_student():
    data=load_data()
    i_d=input("Enter the Roll Number: ").strip()
    if i_d in data:
        return "Student Already Existed..!"
    name=input("Enter Student Name: ").strip()
    while True:
        try:
            marks=list(map(int,input("Enter 3 marks: ").split()))
            if len(marks)!=3:
                print("Please enter exactly 3 marks")
                continue
            break
        except ValueError:
            print("Marks must be Numbers Only..!")

    total,avg,grade=calculate_grade(marks)
    data[i_d]= {'name':name,'marks':marks,'total':total,'average':avg,'grade':grade}
    save_data(data)
    return "Student Added Successfully..!"

def delete_student():
    data=load_data()
    if not data:
        return "No Students Found..!"
    i_d=input("Enter the ID of the Student: ").strip()
    if i_d not in data:
        return "Student Not Found..!"
    del data[i_d]
    save_data(data)
    return "Student Deleted Successfully..!"

def view_students():
    data=load_data()
    if not data:
        return "No Students Found" 
    for i in sorted(data.keys()):
        total,average,grade=calculate_grade(data[i]['marks'])
        print(f"ID: {i} \nName: {data[i]['name']} \nMarks: {data[i]['marks']} \nTotal: {total} \nAverage: {average} \nGrade: {grade}\n")
    return f"Total {len(data)} Students Found"

def search_student():
    data=load_data()
    if not data:
        return "No Students Found..!"
    i_d=input("Enter ID of the Student: ").strip()
    if i_d not in data:
        return "Student Not Found..!"
    total,average,grade=calculate_grade(data[i_d]['marks'])
    return f"Student Found\nID: {i_d}\nName: {data[i_d]['name']} \nMarks: {data[i_d]['marks']} \nTotal: {total} \nAverage: {average} \nGrade: {grade}"

def update_marks():
    data=load_data()
    if not data:
        return "No Students Found..!"
    i_d=input("Enter ID of the Student: ").strip()
    if i_d not in data:
        return "Student Not Found..!"
    while True:
        try:
            marks = list(map(int, input("Enter new 3 marks: ").split()))
            if len(marks) != 3:
                print("Please enter exactly 3 marks")
                continue
            break
        except ValueError:
            print("Marks must be numbers only")
    total,avg,grade=calculate_grade(marks)
    print(f"Old Marks: {data[i_d]['marks']}")
    data[i_d]['marks']=marks 
    save_data(data)
    print(f"New Marks: {data[i_d]['marks']}")
    return "Student Marks Updated Successfully..!"

while True:
    try:
        print("***MENU*** \n0.Exit \n1.Add Student \n2.Delete Student \n3.View Students \n4.Search Student\n5.Update Marks\n")
        n=int(input("Enter Your Choice: "))
    except ValueError:
        print("Invalid input try again")
        continue
    if n==1:
        print(add_student())
    elif n==2:
        print(delete_student())
    elif n==3:
        print(view_students())
    elif n==4:
        print(search_student())
    elif n==5:
        print(update_marks())
    elif n==0:
        print("Good Bye..!")
        break
    else:
        print("Invalid Option..!")
