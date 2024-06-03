import connectionDB as data

db = data.loanDB()

print()
print()


print("  ABC BANK LOAN Eligibility  ")

print()
print()

#input amount loan RM
amount = int(input("Enter the amount of loan: RM "))

print()
print()


print("  -- FILL IN THE DETAILS --  ")

print()
print()


#input name, ic number, salary
name = input("Enter your name: ")
icnumber = input("Enter your IC number: ")
salary = int(input("Enter your salary: RM "))

print()
print()


print("  -- LOAN STATUS --  ")

print()
print()


def calculate_loan_amount(salary):
    max_loan = 100000.00
    if salary > 8000:
        rate = 1.0
    elif 5000 <= salary <= 8000:
        rate = 0.7
    elif 3000 <= salary < 5000:
        rate = 0.5
    else:
        rate = 0.3
    return rate * max_loan

salary = float(input("Enter your monthly salary in RM: "))
loan_amount = calculate_loan_amount(salary)
print(f"The maximum loan you are eligible for is: RM{loan_amount:.2f}")

if amount <= loan_amount:
    loanStatus = 'Approved'
    print("Congratulations! Your loan has been approved.")
else:
    loanStatus = 'Rejected'
    print("Sorry, your loan has been rejected.")


#yes and no
mesej = input("Are you sure to Submit? (yes/no): ")

if mesej == 'yes':
    try:
        db.cur.execute('INSERT INTO listloan (icnumber, name, salary, amount, loanStatus) VALUES (%s,%s,%s,%s,%s)', 
            (icnumber, name, salary, amount, loanStatus))
        db.conn.commit()
        print("Record inserted")
    except:
        db.conn.rollback()
else:
    print("Record not inserted")

