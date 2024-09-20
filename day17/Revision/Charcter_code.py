import string

def create_rot13_dict():
    # Create a dictionary for ROT13
    key = {}
    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.punctuation

    for char in all_chars:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            key[char] = chr((ord(char) - shift_base + 13) % 26 + shift_base)
        else:
            key[char] = char  # Special characters remain the same

    return key

# Create the dictionary
rot13_dict = create_rot13_dict()

# Print the dictionary
for k, v in rot13_dict.items():
    print(f"'{k}': '{v}'")
