def add_expense():
    cat = input("Enter the Category: ")
    amo = int(input("Enter the amount: "))

    file = open("expenses.csv","r")
    data = file.readlines()
    data = [line for line in data if line.strip()]
    if len(data) == 1:
        new_id = 1
    else:
        last_id = int((data[-1]).split(",")[0])
        new_id = last_id + 1
    file.close()
    row = f"{new_id},{cat},{amo}\n"
    
    file = open("expenses.csv","a")
    file.write(row)
    file.close()
    print("Expense Added Successfully")

def view_expense():
    file = open("expenses.csv","r")
    data = file.read()
    print(data)
    file.close()

def total_expense():
    file = open("expenses.csv","r")
    data = file.readlines()
    total = 0 
    for row in data[1:]:
        parts = row.split(',')
        total+=int((parts[2]))
    print(f"Total expense is {total}")
    file.close()


def delete_expense():
    n = int(input("Which Category do u want to delete - pls provide the respective ID: "))
    file = open("expenses.csv","r")
    data = file.readlines()
    new_list = [data[0]]
    for row in data[1:]:
        parts = row.split(',')
        if int(parts[0]) != n:
            new_list.append(row)
    file = open("expenses.csv","w")
    for i in new_list:
        file.write(i)
    file.close()
    print("Expense Deleted Successfully")


while True:
    print("===============")
    print("EXPENSE TRACKER")
    print("===============")

    print("1. Add Expense")
    print("2. View Expense")
    print("3. Delete Expense")
    print("4. Show Total")
    print("5. Exit")
    n = int(input("Enter Choice , what do u want to do : "))
    if n == 1:
        add_expense()
    
    elif n == 2:
        view_expense()
    elif n == 3:
        delete_expense()
    elif n == 4:
        total_expense()
    elif n == 5:
        break
    else:
        print("Invalid Operation ")


