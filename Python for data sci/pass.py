import random
import string

class user:
    def __init__(self,user_id,name,password):
        self.user_id=user_id
        self.name=name
        self.password=password

    def display_user(self):
        print(f"User ID : {self.user_id}")
        print(f"Name : {self.name}")
        print(f"Password : {self.password}")

def generator_password(user_input):
    if not user_input:
        raise ValueError("Input cannot be empty")
    
    words=user_input.split()
    if len(words)==0:
        raise ValueError("Please enter at least one word ")
    
    choose_word=random.sample(words,min(2,len(words)))

    password = ''.join([word.capitalize() for word in choose_word])

    numbers=''.join(random.choices(string.digits,k=2))
    special=''.join(random.choices(string.punctuation,k=2))

    password += numbers + special

    password=list(password)
    random.shuffle(password)
    password=''.join(password)  

    while(password<8):
        password+=random.choice(string.ascii_letters+string.digits+string.punctuation)

    return password

try:
    user_id = input("Enter User ID: ")
    name = input("Enter Name: ")
    user_input = input("Enter some words to generate password: ")
    
    password = generator_password(user_input)
    
    # Store info in a tuple
    user_info = (user_id, name, password)
    
    print("\nUser created successfully!\n")
    print("User Info Tuple:", user_info)

except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)