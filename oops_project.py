class chatbook:
    def __init__(self):
        self.username=""
        self.password = ''
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""Welcome to Chatbook! How would you  like to proceed?
                           1.Press 1 to Sign Up
                           2.Press 2 to Log In
                           3.Press 3 to write post
                           4.Press 4 to message a friend
                           5.Press anyother key to exit """)

        if user_input == '1':
            pass
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            print("Exiting the application. Thank you for using Chatbook!")
            exit()
            
obj = chatbook()

        