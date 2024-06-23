class User:
    user_count = 0

    def __init__(self, user_name: str = 'Jon Doe', user_age: int = 18, user_pass: str = "12345678") -> object:
        print(f'New user {user_name} applied')
        self.user_age = user_age
        self.user_name = user_name
        self.user_hash = hash(user_pass)
        self.adult = user_age >= 18
        User.user_count += 1

    def __del__(self):
        if User.user_count:
            print(f'User {self.user_name} was deleted')
            User.user_count -= 1

    def __str__(self):
        return (f'user: {self.user_name}\n'
                f'age: {self.user_age}\n'
                f'adult: {self.adult}\n'
                f'--------------------')

    def __eq__(self, other):
        return self.user_name == other.user_name

    def info(self):
        return {
            'user name': self.user_name,
            'user age': self.user_age
        }

    def get_hash(self):
        return self.user_hash





