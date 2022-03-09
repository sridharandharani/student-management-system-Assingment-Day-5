import sqlite3
from prettytable import PrettyTable

folder = sqlite3.connect("studentdata.db")

listoftables = folder.execute("select name from sqlite_master where type = 'table' and name = 'studentdata.db' ").fetchall()

if listoftables != []:
    print("Table already exits !")
else:
    folder.execute(''' create table student(
                    id integer primary key autoincrement,
                    name text,
                    rollno integer,
                    admno integer,
                    examname text,
                    english integer,
                    maths integer,
                    physics integer,
                    chemistry integer,
                    biology integer ); ''')
    print("Table is created")

while True:
        print("Select the option in menu:")
        print("1. add student data ")
        print("2. view all students ")
        print("3. search a student using their partial names ")
        print("4. search using Adm No or Roll No students ")
        print("5. update the student data with Adm No ")
        print("6. delete using Adm No ")
        print("7. display the student details of topper physics ")
        print("8. display the count of total number of students in the class ")
        print("9. display the average of a student in english ")
        print("10. display the details of all students who score less than average in maths")
        print("11. display the details of above average in chemistry ")
        print("12. Exit ")

        choice = int(input("Enter your choice :"))
        if choice == 1:
            getname = input("Enter the name :")
            getroll = input("Enter the roll no :")
            getadmno = input("Enter the adm no: ")
            getexam = input("Enter the exam name :")
            geteng = input("Enter the english mark :")
            getmat = input("Enter the maths mark : ")
            getphy = input("Enter the physics mark :")
            getche = input("Enter the chemistry mark :")
            getbio = input("Enter the biology mark :")

            folder.execute("insert into student(name,rollno,admno,examname,english,maths,physics,chemistry,biology)\
            values('"+getname+"',"+getroll+","+getadmno+",'"+getexam+"',"+geteng+","+getmat+","+getphy+","+getche+","+getbio+")")
            folder.commit()
            print("Inserted sucessfully")

        elif choice == 2:
            result = folder.execute("select * from student ")
            table = PrettyTable(
                ["Student Id","Student Name","Roll number","Admission Number","Exam Name",
                 "English Marks","Maths Marks","Physics Marks","Chemistry mark","Biology marks"])
            for i in result:
                table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]])
            print(table)

        elif choice == 3:
            getname = input("Enter the name :")

            result = folder.execute("select * from student where name like '%"+getname+"%'")
            table = PrettyTable(
                ["Student Id", "Student Name", "Roll number", "Admission Number", "Exam Name",
                 "English Marks", "Maths Marks", "Physics Marks", "Chemistry mark", "Biology marks"])
            for i in result:
                table.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]])
            print(table)

        elif choice == 4:
            getadmno = input("Enter the adm no")
            getroll = input("Enter the roll no")

            result = folder.execute("select * from student where admno="+getadmno+" or rollno="+getroll )
            table = PrettyTable(
                ["Student Id", "Student Name", "Roll number", "Admission Number", "Exam Name",
                 "English Marks", "Maths Marks", "Physics Marks", "Chemistry mark", "Biology marks"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5],i[6], i[7],i[8],i[9]])
            print(table)


        elif choice == 5:
            getadmno = input("Enter the adm no")

            getname = input("Enter the name :")
            getroll = input("Enter the roll no")
            getexam = input("Enter the exam name")
            geteng = input("Enter the english mark")
            getmat = input("Enter the maths mark")
            getphy = input("Enter the physics mark")
            getche = input("Enter the chemistry mark")
            getbio = input("Enter the biology mark")

            result = folder.execute("update student set \
            name = '"+getname+"',rollno = "+getroll+",examname = '"+getexam+"'\
            ,english = "+geteng+",maths = "+getmat+",physics = "+getphy+",chemistry = "+getche+",biology = "+getbio+"\
             where admno ="+getadmno)
            folder.commit()
            print("updated sucessfully")

        elif choice == 6:
            etadmno = input("Enter the adm no")

            folder.execute("delete from student where admno="+getadmno)
            folder.commit()
            print("deleted sucessfully")

        elif choice == 7:
            result = folder.execute("select * from student where physics=(select max(physics) as physics from student )")
            table = PrettyTable(
                ["Student Id", "Student Name", "Roll number", "Admission Number", "Exam Name",
                 "English Marks", "Maths Marks", "Physics Marks", "Chemistry mark", "Biology marks"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5],i[6], i[7],i[8],i[9]])
            print(table)

        elif choice == 8:
            result = folder.execute("select count(*) as count from student")
            table = PrettyTable(["COUNT"])
            for i in result:
                table.add_row([i[0]])
            print(table)

        elif choice == 9:
            result = folder.execute("select avg(english) as english from student")
            table = PrettyTable(["Averange english mark"])
            for i in result:
                table.add_row([i[0]])
            print(table)

        elif choice == 10:
            result = folder.execute("select * from student where maths<(select avg(maths) as maths from student)")
            table = PrettyTable(
                ["Student Id", "Student Name", "Roll number", "Admission Number", "Exam Name",
                 "English Marks", "Maths Marks", "Physics Marks", "Chemistry mark", "Biology marks"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5],i[6], i[7],i[8], i[9]])
            print(table)


        elif choice == 11:
            result = folder.execute("select * from student where chemistry>(select avg(chemistry) as chemistry from student)")
            table = PrettyTable(
                ["Student Id", "Student Name", "Roll number", "Admission Number", "Exam Name",
                 "English Marks", "Maths Marks", "Physics Marks", "Chemistry mark", "Biology marks"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5],i[6], i[7],i[8], i[9]])
            print(table)

        elif choice == 12:
            folder.close()
            break
        else:
            print("invalid option !")







