class user:
    def get_input(self):
        name = input('enter your name: ')
        return name
    def greet_user(self):
        print(f'Hello {get_input()}')
        
user1= user()
user1.greet_user()
        