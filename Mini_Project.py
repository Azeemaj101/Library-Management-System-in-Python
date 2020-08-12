import os
import time


class Library:
    Library_Name = "AJ_Library"
    Name = " "

    def __init__(self, B_Name, B_ID, B_Lend):
        self.Book_N = B_Name
        self.Book_ID = B_ID
        self.Book_L = B_Lend

    def Add_Book(self):
        with open("Library.txt", "a") as cout:
            self.Book_N = input()
            self.Book_ID = int(input())
            cout.write(f"{self.Book_N}~{self.Book_ID}\n")

    @staticmethod
    def View():
        with open("Library.txt", "r") as cin:
            ch = ' '
            while ch:
                ch = cin.readline()
                val = ch.split("~")
                if len(ch) > 0:
                    print(f"Book: {val[0]} \nID: {val[1]}")

    @staticmethod
    def Search():
        with open("Library.txt", "r") as cin:
            ch = ' '
            inpu = int(input("Enter ID_Number For Search\n"))
            while ch:
                ch = cin.readline()
                val = ch.split("~")
                if len(ch) > 0:
                    if inpu == int(val[1]):
                        print(f"Book: {val[0]} \nID: {val[1]}")

    @staticmethod
    def delete():
        cin = open("Library.txt", "r")
        cout = open("temp.txt", "a")
        ch = ' '
        inpu = int(input("Enter ID_Number For Delete\n"))
        while ch:
            ch = cin.readline()
            val = ch.split("~")
            if len(ch) > 0:
                if inpu != int(val[1]):
                    cout.write(ch)
        cout.close()
        cin.close()
        os.remove("Library.txt")
        os.rename("Temp.txt", "Library.txt")

    def update(self):
        cin = open("Library.txt", "r")
        cout = open("temp.txt", "a")
        ch = ' '
        inpu = int(input("Enter ID_Number For Delete\n"))
        while ch:
            ch = cin.readline()
            val = ch.split("~")
            if len(ch) > 0:
                if inpu == int(val[1]):
                    self.Book_N = input()
                    self.Book_ID = int(input())
                    cout.write(f"{self.Book_N}~{self.Book_ID}\n")
                else:
                    cout.write(ch)

        cout.close()
        cin.close()
        os.remove("Library.txt")
        os.rename("Temp.txt", "Library.txt")

    @classmethod
    def lend(cls):
        with open("All Books", "r") as cin1:
            ch = ' '
            while ch:
                ch = cin1.readline()
                val = ch.split("~")
                if len(ch) > 0:
                    print(f"Book: {val[0]} \nID: {val[1]}")
        with open("Library.txt", "r") as cin:
            le = open("Lend.txt", "a")
            le1 = open("Lend.txt", "r")
            cout = open("temp.txt", "a")
            ch = ' '
            inpu = int(input("Enter ID_Number For Search\n"))
            while ch:
                ch = cin.readline()
                val = ch.split("~")
                if len(ch) > 0:
                    if inpu == int(val[1]):
                        print("Yes! Available")
                        print("Please Enter Your Name")
                        cls.Name = input()
                        print(f"Book: {val[0]} \nID: {val[1]}")
                        a = val[0]
                        b = val[1]
                        les = [a, b, cls.Name]
                        le.write(f"{les[0]}~{les[1].strip()}~{les[2]}\n")
                    else:
                        cout.write(ch)
                        ch1 = ' '
                        while ch1:
                            ch1 = le1.readline()
                            val1 = ch1.split("~")
                            if len(ch1) > 0:
                                if inpu == int(val1[1]):
                                    print("Not Available: Current Lend User")
                                    print(f"Book         : {val1[0]} "
                                          f"\nID           : {val1[1]} "
                                          f"\nCurrent User : {val1[2]} ")
        le.close()
        le1.close()
        cout.close()
        os.remove("Library.txt")
        os.rename("temp.txt", "Library.txt")

    @classmethod
    def Return(cls):
        with open("Lend.txt", "r") as cin1:
            ch = ' '
            while ch:
                ch = cin1.readline()
                val = ch.split("~")
                if len(ch) > 0:
                    print(f"Book         : {val[0]} "
                          f"\nID           : {val[1]} "
                          f"\nCurrent User : {val[2]} ")
        with open("Lend.txt", "r") as cin:
            le = open("Library.txt", "a")
            cout = open("temp.txt", "a")
            ch = ' '
            inpu = int(input("Enter Return Book ID_Number\n"))
            while ch:
                ch = cin.readline()
                val = ch.split("~")
                if len(ch) > 0:
                    if inpu == int(val[1]):
                        print("Yes! Available in Lend List")
                        print(f"Book         : {val[0]} "
                              f"\nID           : {val[1]} "
                              f"\nCurrent User : {val[2]} ")
                        le.write(f"\n{val[0]}~{val[1]}")
                    else:
                        cout.write(ch)

        le.close()
        cout.close()
        os.remove("Lend.txt")
        os.rename("temp.txt", "Lend.txt")


if __name__ == '__main__':
    Obj = Library("Urdu", 1, "Ali")
    menu = True
    print("\033[34m\033[01m\t\t\t\t\t\t\t\t\t\t\t\t*****************Library Management System*****************")
    while menu:
        print("\033[01m\033[33mPlease Enter 1 for Manager ")
        print("Please Enter 2 for Customer")
        print("Please Enter 3 for Exits   ")
        user = int(input())
        if user == 1:
            passs = True
            while passs:
                pas = int(input("Please Enter Your Password\n"))
                print("\033[31mLoading <", end="")
                for i in range(20):
                    print("|", end="")
                    time.sleep(0.25)
                print(">Processing....\n\n")
                if pas == 1234:
                    GotoM = True
                    while GotoM:
                        print("\033[35mPlease Enter 1 For Add    Books")
                        print("Please Enter 2 For View   Books")
                        print("Please Enter 3 For Search Books")
                        print("Please Enter 4 For Delete Books")
                        print("Please Enter 5 For Update Books")
                        man = int(input())
                        if man == 1:
                            Obj.Add_Book()
                            GotoM = False
                        elif man == 2:
                            Obj.View()
                            GotoM = False
                        elif man == 3:
                            Obj.Search()
                            GotoM = False
                        elif man == 4:
                            Obj.delete()
                            GotoM = False
                        elif man == 5:
                            Obj.update()
                            GotoM = False
                        else:
                            print("Wrong Key ")
                    passs = False
                    os.system("pause")

                else:
                    print("Wrong Key ", end="")
                    os.system("PAUSE")

        elif user == 2:
            cu = True
            while cu:
                print("\033[35mPress 1 Lend   Book")
                print("Press 2 Return Book")
                cus = int(input())
                if cus == 1:
                    Obj.lend()
                    cu = False
                elif cus == 2:
                    Obj.Return()
                    cu = False
                else:
                    print("Wrong Key", end=" ")
                    os.system("PAUSE")
        elif user == 3:
            menu = False
        else:
            print("Wrong Key", end=" ")
            os.system("PAUSE")
