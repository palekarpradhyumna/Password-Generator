import random

def passwordgenerator(length=8):
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    specialchars = ['!', '@', '#', '$', '%', '^', '&', '*']
    numericchar = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Ensure the password contains at least one of each type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(specialchars),
        random.choice(numericchar)
    ]
    
    # Fill the rest of the password length with random characters from all categories
    all_chars = uppercase + lowercase + specialchars + numericchar
    for _ in range(length - 4):  # Subtract 4 because we've already added 4 characters
        password.append(random.choice(all_chars))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
print(passwordgenerator(12))  # Generates a 12-character long password