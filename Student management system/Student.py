from stud import addStudent , viewStudent , deleteStudent , Studentmarks ,viewmarks
from stud import addTeacher , viewTeacher , deleteTeacher , deletemarks 
while True:
    print("\n\t Mother Academy Khurja ")
    print("\n\t\tFor Class 9th")
    print('''
        1. Add Student
        2. View all student
        3. Delete Student
        4. Add Class Teachers
        5. View All Teachers Information
        6. Delete Teacher 
        7. Student Marks
        8. View Students Marks 
        9. Delete Student Marks
        0. Return(Exit) 
        
        ''')
    ch=int(input("\tEnter your choice :"))
    if ch==0:
        print("\n\t\t Thank You !")
        break
    elif ch==1:
        addStudent()
        input("\tPress Enter To Continue...")
    elif ch==2:
        viewStudent()
        input("\tPress Enter to Continue...")
    elif ch==3:
        deleteStudent()
        input("\tPress Enter to Continue...")
    elif ch==4:
        addTeacher()
        input("\tPress Enter to Continue...")
    elif ch==5:
        viewTeacher()
        input("\tPress Enter to Continue...")
    elif ch==6:
        deleteTeacher()
        input("\tPress Enter to Continue...")
    elif ch==7:
        Studentmarks()
        input("\tPress Enter to Continue...")
    elif ch==8:
        viewmarks()
        input("\tPress Enter to Continue...")
    elif ch==9:
        deletemarks()
        input("\tPress Enter to Continue...")
    else :
        print("\n\tEnter the Right Choice ...!!")
    
        

        
        
        
        
        
        
        
        
   
