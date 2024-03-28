# 1. Register
# 2. Login
# 3. Display Profile
# 4. Logout

class Student:
    def __init__(self):
        self.data={}
    def register(self,username,rollno,email,password):
        if username in self.data:
            print("Already Registered")
        else:
            self.data[username]={'rollno':rollno, 'email':email, 'password':password}
            print("Registration Successful")
            
    def login(self,rollno,password):
        for i,j in self.data.items():
            if j['rollno']==rollno and j['password']==password:
                print("\nWelcome",i)
            if j["rollno"]!=rollno:
                print("Invalid rollno")
            if j['password']!=password:
                print("Invalid password")


    def display_profile(self,username):
        if username in self.data:
            print("Username:",username)
            print("Rollno:",rollno)
            print("Email:",email)
            print(self.data)
        else:
            print("User not found")


    def logout(self):
        print("Logged out successfully")

s=Student()

while True:
    print("\nMenu")
    print("\n1. Register")
    print("\n2. Login")
    print("\n3. Display profile")
    print("\n4. Logout\n")

    option=int(input("Enter an option:"))

    if option==1:
        username=input("Enter your name:")
        rollno=input("Enter rollno:")
        email=input("Enter mail id:")
        password=input("Enter password:")
        s.register(username,rollno,email,password)
    
    elif option==2:
        rollno=input("Enter rollno:")
        password=input("Enter password:")
        s.login(rollno,password)

    elif option==3:
        username=input("enter username:")
        s.display_profile(username)

    elif option==4:
        s.logout()
        break
    else:
        print("invalid option")
