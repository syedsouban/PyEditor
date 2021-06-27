import sys
print("Welcome to Python 3 Text Editor")
condition = True
while condition == True:
        print("""What do you want to do:
        1. Creating a new file
        2. Writing to a saved file
        3. Viewing a saved file
        4. Exit """)
        choice=eval(input("Enter your choice: "))
        if choice==4:
                sys.exit()
        elif choice==3:
                mode="r"
                file_name=input("Enter your filename: ")
                File=open(file_name,mode)
                print(File.read())
        elif choice==2:
                mode="a+"
                file_name=input("Enter your filename: ")
                File=open(file_name,mode)
                print(File.read())
                File.close()
                File=open(file_name,mode)
                while True:
                        new_text=input()
                        File.write((new_text)+'\n')
        elif choice==1:
                mode="w+"
                file_name=input("Enter your filename: ")
                File=open(file_name,mode)
                File.truncate()
                print("Start writing your text from here(Press Ctrl+Z and then Press Enter for stop writing): ")
                while True:
                        new_text=input()
                        File.write((new_text)+'\n')
        else:
                print("Invalid choice entered")
        char=input("Press C/c to continue and Q/q to quit: ")
        if char=='C' or char == 'c':
                condition=True
        elif char=='q' or char=='Q':
                condition=False
        else:
                print("Invalid choice entered")
File.close()

#adding a commit, bruuuh.
