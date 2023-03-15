#employee management system

from os import system
import re
#importing mysql connector for connection
import mysql.connector

#connection with database
mydb = mysql.connector.connect(
    host="localhost", username="root", password="1234", database="employee")
# mycursor=mydb.cursor()


# creating table with fields
# mycursor.execute("create table empdata (Id INT(10) PRIMARY KEY ,Name VARCHAR(50), Email_Id text(100) , Phone_no int(11) , Address text(500) ,Post text(100) , Salary bigint(20))")

#make a regular expression for validating an email
regax=r'\b[A-Za-z0-8,_%+-]+@[A-Za-z0-9,-]+\.[a-z|A-Z]{2,}\b'

#Add employee function
def Add_Employee():
    print("{:>60}".format("   *Add Employee Data*   "))
    
    Id= input("Enter Employee Id: ")
    #checking if id entered already exist or not
    if(check_employee(Id)==True):
        print("Employee Id already exist . Try again")
        press=input("Press any key to continue")
        Add_Employee()
    
    Name= input("Enter Employee Name: ")
    #checking if name entered already exist or not
    if(check_employee_name(Name)==True):
        print("Employee already exist . Try again")
        press=input("Press any key to continue")
        Add_Employee()
    Email_Id= input("Enter Employee Email Id: ")
    #checking if email is valid or not
    if(re.fullmatch(regax,Email_Id)):
        print("valid email")
    else:
        print("invalid email")
        press=input("enter any key to continue")
        Add_Employee()
    Phone_no=input("Enter Employee Phone no: ")  
    Address= input("Enter Employee Address: ")
    Post= input("Enter Employee Post: ")
    Salary= input("Enter Employee Salary: ")
    data=(Id, Name, Email_Id,Phone_no, Address, Post, Salary)
    # inserting data in employee (empdata) table
    sql= "insert into empdata values(%s,%s,%s,%s,%s,%s,%s)"
    mycursor=mydb.cursor()
    
    mycursor.execute(sql, data)
    mydb.commit()
    print("Successfully Added Employee Record")
    press=input("Press any key to continue")
    menu()
    
#checking if given name already exist or not
def check_employee_name(employee_name):
    #query to select all rows from table
    sql="select * from empdata where name= %s"
    
    #making cursor buffered to make rowcount method work properly 
    c=mydb.cursor(buffered=True)
    data=(employee_name,)
    c.execute(sql,data)
    
    #rowcount method to find no of rows with given value
    r=c.rowcount
    if r==1:
        return True
    else:
        return False
    
#checking if given id already exist or not
def check_employee(employee_id):
    #query to select all rows from table
    sql="select * from empdata where id= %s"
    
    #making cursor buffered to make rowcount method work properly 
    c=mydb.cursor(buffered=True)
    data=(employee_id,)
    c.execute(sql,data)
    
    #rowcount method to find no of rows with given value
    r=c.rowcount
    if r==1:
        return True
    else:
        return False
  
#function to display data
def Display_Employee():
    print("{:>60}".format("   *Display Employee Data*   "))
    #query to select all rows from table
    sql="select * from empdata"
    c=mydb.cursor()
    #executing sql query
    c.execute(sql)
    
    #fetching all details of all the employess
    data=c.fetchall()
    for i in data:
        print("Employee Id: ",i[0])
        print("Employee Name: ",i[1])
        print("Employee Email Id: ",i[2])
        print("Employee Phone no: ",i[3])
        print("Employee Address: ",i[4])
        print("Employee Post: ",i[5])
        print("Employee Salary: ",i[6])
        print("\n")
    press=input("Press any key to continue")
    menu()

# Function to update data 
def Update_Employee():
    print("{:>60}".format("   *Display Employee Data*   "))
    Id=input("Enter Employee Id: ")
    #checking if ID exist or not
    if(check_employee(Id)==False):
        print("Employye ID don't exist ")
        press=input("press any key to continue")
        menu()
    else:
        Email_Id= input("Enter Employee Email Id: ")
    #checking if email is valid or not
        if(re.fullmatch(regax,Email_Id)):
            print("valid email")
        else:
            print("invalid email")
            press=input("enter any key to continue")
            Update_Employee()

        Phone_no=input("Enter Employee Phone no: ")
        Address= input("Enter Employee Address: ")
        
        #updating Employee Details in Empdata table
        sql="update empdata set Email_Id=%s, Phone_no=%s, Address=%s where Id=%s"
        data=(Email_Id,Phone_no,Address,Id)
        c=mydb.cursor()
        
        #executing the query
        c.execute(sql,data)
        
        #commit() method to make changes in the table
        mydb.commit()
        print("Data Updated Successfully")
        press=input("Press any key to continue")
        menu()
        
# Function for Promote_Employee
def Promote_Employee():
    print("{:>60}".format("   *Promote Employee Data*   "))
    Id=input("Enter Employee Id: ")
    #checking if ID exist or not
    if(check_employee(Id)==False):
        print("Employye ID don't exist ")
        press=input("press any key to continue")
        menu()
    else:
        Increment=int(input("Enter Increment Amount"))
        #query to fetch salary with given data
        sql="select Salary from empdata where Id=%s"
        data=(Id,)
        c=mydb.cursor()
        
        #executing the sql query
        c.execute(sql,data)
        
        #fetching the salary of employee 
        s=c.fetchone()
        total=s[0]+Increment
        
        #query to update salary
        sql="update empdata set Salary=%s where Id=%s"
        NewSalary=(total,Id)
        
        #executing the sql queery
        c.execute(sql,NewSalary)
        
        #commit method to make changes 
        mydb.commit()
        print("Employee Promoted")
        press=input("Press any key to continue")
        menu()  
     
 # Function to remove Remove_Employee()
def Remove_Employee():
    print("{:>60}".format("   *Remove Employee Data*   "))
    Id=input("Enter Employee Id: ")
    #checking if ID exist or not
    if(check_employee(Id)==False):
        print("Employye ID don't exist ")
        press=input("press any key to continue")
        menu()
    else:
        #query to delete Employee From table
        sql="delete from empdata where Id= %s"
        data=(Id,)
        c=mydb.cursor()
        
        #executing the sql query
        c.execute(sql,data)
        
        #commit method to make changes in table
        mydb.commit()
        print("Employee Removed")
        press=input("Press any key to continue")
        menu()
        
#Function to Seach employee
def Search_Employee():
    print("{:>60}".format("   *Search Employee Data*   "))
    Id=input("Enter Employee Id: ")
    #checking if ID exist or not
    if(check_employee(Id)==False):
        print("Employye ID don't exist ")
        press=input("press any key to continue")
        menu()
    else:
        #query to search employee from table
        sql="select * from empdata where Id=%s"
        data=(Id,)
        c=mydb.cursor()
        
        #execute the sql query
        c.execute(sql,data)
        
        #fetching all details of employee
        detail=c.fetchall()
        for i in detail:
            print("Employee ID:",i[0])
            print("Employee Name:",i[1])
            print("Employee Email ID:",i[2])
            print("Employee Phone no:",i[3])
            print("Employee Address:",i[4])
            print("Employee Post:",i[5])
            print("Employee Salary:",i[6])
            print("\n")
    press=input("Press any key to continue")
    menu()
            
#creating menu function

def menu():
    system("cls")
    print("{:>60}".format("--------------------------------"))
    print("{:>60}".format("   Employee Management System   "))
    print("{:>60}".format("--------------------------------"))
    print("1. Add Employee")
    print("2. Display Employee Data")
    print("3. Update Employee Data")
    print("4. Promote Employee Data")
    print("5. Remove Employee Data")
    print("6. Search Employee Data")
    print("7. Exit\n")
    print("{:>60}".format("   Choice Options : 1,2,3,4,5,6,7"))
    
    choice=int(input("Enter your Choice: "))
    if choice == 1:
        system("cls")
        Add_Employee()
    elif choice==2:
        system("cls")
        Display_Employee()
    elif choice==3:
        system("cls")
        Update_Employee()
    elif choice==4:
        system("cls")
        Promote_Employee()
    elif choice==5:
        system("cls")
        Remove_Employee()
    elif choice==6:
        system("cls")
        Search_Employee()
    elif choice==7:
        system("cls")
        print("{:>60}".format("Have a nice day"))
    else:
        print("Invalid Choice")
        press=input("Press any key to continue")
        menu()
menu()
    