class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""Welcome to Chatbook! How would you like to proceed?
                           1.Press 1 to Sign Up
                           2.Press 2 to Log In
                           3.Press 3 to write post
                           4.Press 4 to message a friend
                           5.Press any other key to exit 
                           
                           """)

        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.login()
        elif user_input == '3':
            self.mypost()
        elif user_input == '4':
            self.send_message()
        else:
            print("Exiting the application. Thank you for using Chatbook!")
            exit()
    
    def signup(self):
        email = input("enter your email ->")
        pwd = input("setup your password here ->")
        self.username = email
        self.password = pwd
        print("You have successfully signed up!")
        print("\n")
        self.menu()
        
    def login(self):
        if self.username == '' and self.password == '':
            print("No user found, please sign up first")
            self.menu()
        else:
            uname = input("enter your email/username here ->")
            pwd = input("enter your password here ->")
            if self.username == uname and self.password == pwd:
                print("you have successfully logged in!")
                self.loggedin = True
            else:
                print("Invalid credentials, please try again")
        print("\n")
        self.menu()
        
    def mypost(self):
        if self.loggedin == True:
            post = input("write your post here ->")
            print(f"Your post has been published -> {post}")
        else:
            print("Please log in to write a post...")
        print("\n")
        self.menu()
        
    def send_message(self):
        if self.loggedin == True:
            txt = input("Enter your message here ->")
            frnd = input("whom to send the msg? ->")
            print(f"Your message has been sent to {frnd} -> {txt}")
        else:
            print("Please log in to send a message...")
        print("\n")
        self.menu()

user1 = chatbook()