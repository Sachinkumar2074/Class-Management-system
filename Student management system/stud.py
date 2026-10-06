import pickle



#To Get All Student

def getStudent():
    file = open('student1.bin','rb')
    stu = {}
    try:
        while True:
            stu.update(pickle.load(file))
    except:
        pass
    file.close()
    return stu

# To add new student 
def addStudent():
    sid = input("\n\tEnter New Student Id :")
    if not getStudent().get(sid,False):
        sname  = input("\tEnter New Student Name:")
        sclass = input("\tEnter New Student Class :")
        sdob = input("\tEnter New Student Date of Birth :")
        smob = input("\tEnter New Student Mobile NO.:")
        sfname = input("\tEnter Student Father Name :")
        data = {sid: [sname,sclass,sdob,smob,sfname]}
        file = open('student1.bin','ab')
        pickle.dump(data,file)
        file.close()
        print("\n\tStudent Added Succesfully!")
    else:
        print("\n\t This id is Already Exist \n\t Chosse Another!")


# To View all student

def viewStudent():   
    file = open('student1.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            for sid,info in data.items():
                print("\n\tStudent Rollno.:",sid)
                print("\tStudent Name:",info[0])
                print("\tStudent Class : ",info[1])
                print("\tStudent Date of Birth :",info[2])
                print("\tStudent Mobile no. :",info[3])
                print("\tStudent Father's Name :",info[4])
                print("\t------------------------------------------------")
    except:
        print("\n\t Student Record Found!")
        file.close()
                 
# To update Student Information
def updateStudent(stu):
    file= open('student1.bin','wb')
    for sid,info in stu.items():
       pickle.dump({sid:info},file)
    file.close()
    


# To delete Student information
def deleteStudent():
    sid=input("\n\t Enter Student id To Delete Student :")
    stu = getStudent()
    if stu.get(sid,False):
        s=stu.get(sid,False)
        stu.pop(sid)
        updateStudent(stu)
        print(f"\n\t{s[0]} Deleted successfully!")
    else :
        print("\n\t Student Not Found!")


#Too get the all teacher

def getTeacher():
    file = open('teacher1.bin','rb')
    tea = {}
    try:
        while True:
            tea.update(pickle.load(file))
    except:
        pass
    file.close()
    return tea


#To Add The Class Teacher
def addTeacher():
    tid = input("\n\t Enter the ID of The Teacher :")
    if not getTeacher().get(tid,False):
        tname = input("\t Enter the Name of the Teacher :")
        tsub = input("\t Enter The Subject Of Teacher :")
        tmob = input("\t Enter The Mobile no. of Teacher :")
        tcla = input("\t Enter The Teacher Class :")
        data = {tid :[tname,tsub,tmob,tcla]}
        file = open('teacher1.bin','ab')
        pickle.dump(data,file)
        file.close()
        print("\n\tTeacher INFO save Successfully!")
    else:
        print("\n\t This id is Already Exist \n\t Chosse Another!")


#To View All Teacher
def viewTeacher():   
    file = open('teacher1.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            for tid,info in data.items():
                print("\n\t Teacher Id.:",tid)
                print("\t Teacher  Name:",info[0])
                print("\t Teacher Subject : ",info[1])
                print("\t Teacher Mobile no. :",info[2])
                print("\t Class Teacher of Class :",info[3])
                print("\t------------------------------------------------")
    except:
        print("\n\t Teacher Record Found!")
        file.close()


# To get Teacher Information
def updateTeacher(tea):
    file= open('teacher1.bin','wb')
    for tid,info in tea.items():
       pickle.dump({tid:info},file)
    file.close()
    


# To delete Teacher information
def deleteTeacher():
    tid=input("\n\t Enter Teacher id To Delete Teacher :")
    tea = getTeacher()
    if tea.get(tid,False):
        t=tea.get(tid,False)
        tea.pop(tid)
        updateTeacher(tea)
        print(f"\n\t{t[0]} Deleted successfully!")
    else :
        print("\n\t Teacher Not Found!")





#To get All student marks
def getmarks():
    file = open('StudentMarks1.bin','rb')
    mar = {}
    try:
        while True:
            mar.update(pickle.load(file))
    except:
        pass
    file.close()
    return mar



# To Input The Marks Of Student in every Subject
def Studentmarks():
     smrk = input("\n\tEnter  Student Id :")
     print("\n\tGive all Sub. Marks In Out Of 100.")
     if not getmarks().get(smrk,False):
         sub1  = int(input("\tEnter marks in Maths   :"))
         sub2 = int(input("\tEnter Marks in Science :"))
         sub3 = int(input("\tEnter Marks in English :"))
         sub4 = int(input("\tEnter Marks in Hindi:"))
         sub5 = int(input("\tEnter Marks in GK :"))
         tmark = sub1 + sub2 + sub3 + sub4 + sub5
         data = {smrk  : [sub1,sub2,sub3,sub4,sub5,tmark]}
         file = open('StudentMarks1.bin','ab')
         pickle.dump(data,file)
         file.close()
         print("\n\tStudent Marks Added Succesfully!")
     else:
        print("\n\t This id is Already Exist \n\t Chosse Another!")

#Too view  Students Marks:
def viewmarks():   
    file = open('StudentMarks1.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            for smrk,infu in data.items():
                print("\n\tStudent Rollno.:",smrk)
                print("\tStudent marks in Maths :",infu[0],"out of 100")
                print("\tStudent Marks in Science :",infu[1],"out of 100")
                print("\tStudent Marks in English :",infu[2],"out of 100")
                print("\tStudent Marks in Hindi:",infu[3],"out of 100")
                print("\tStudent Marks in GK :",infu[4],"out of 100")
                print("\tStudent Marks in all Subjects :",infu[5],"out of 500")
                if infu[5]>=400:
                    print("\n\tYou Pass With First Division!")
                elif 400>infu[5]>=300:
                    print("\n\tYou Pass With Second Division!")
                elif 300>infu[5]>165:
                    print("\n\tYou Pass With Third Division!")
                else :
                    print("\n\tYou Are Fail ! Try again")
                    print("\t------------------------------------------------")
    except:
        print("\n\t Student Marks  Found!")
        file.close()


# To get Student Marks Information
def updatemarks(mar):
    file= open('StudentMarks1.bin','wb')
    for smrk,info in mar.items():
       pickle.dump({smrk:info},file)
    file.close()
    


# To delete Marks information
def deletemarks():
    smrk=input("\n\t Enter Student ID  To Delete Marks :")
    mar = getmarks()
    if mar.get(smrk,False):
        m=mar.get(smrk,False)
        mar.pop(smrk)
        updatemarks(mar)
        print(f"\n\t{smrk} Deleted successfully!")
    else :
        print("\n\t Student ID Not Found!")



