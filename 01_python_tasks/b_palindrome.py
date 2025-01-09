# Palindrome Checker

string = input("Enter your string: ")

cleaned_str = ''.join(filter(str.isalnum, string))  # Punctuation, Whitespace, Special & Mathematical Symbols, Brackets are non-alphanumeric characters, so they are filtered out.
                                                    # ||| ''.join() ||| is a way to take a list of things (like letters or words) and stick them together into one single string, without adding anything between them (since '' means no space or separator).

lower_str = cleaned_str.lower()         # Case-insensitive
                                        
reverse_str = lower_str[::-1]

if(lower_str == reverse_str):
    print(f"The given string '{string}' is a Palindrome")
else:
    print(f"The given string '{string}' is not a Palindrome")



'''

Output:

Enter your string: Do geese see God?
The given string 'Do geese see God?' is a Palindrome

Enter your string: The sky is Blue !!!
The given string 'The sky is Blue !!!' is not a Palindrome

'''