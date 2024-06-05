from user import User

user = User()
user.register("Hadiza","09065218424","dizza@gmail.com","123")
email=input("Enter your Email:")
password=input("Enter your paassword:")
print(user.login(email, password))

