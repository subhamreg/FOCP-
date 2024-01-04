# One approach to analysing some encrypted data where a substitution is suspected
# is frequency analysis. A count of the different symbols in the message can be used
# to identify the language used, and sometimes some of the letters. In English, the
# most common letter is "e", and so the symbol representing "e" should appear most
# in the encrypted text.
# Write a program that processes a string representing a message and reports the six
# most common letters, along with the number of times they appear. Case should
# not matter, so "E" and "e" are considered the same.
# Hint: There are many ways to do this. It is obviously a dictionary, but we will want
# zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
# best to ignore that initially, and then check the usual resources for the runes

def frequency_analysis(message):
    # Convert the message to lowercase to make it case-insensitive
    message = message.lower()

    # Initialize a dictionary to store the frequency of each letter
    letter_count = {}

    # Count the frequency of each letter in the message
    for char in message:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1

    # Sort the dictionary by values in descending order
    sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

    # Display the six most common letters and their frequencies
    print("Six most common letters and their frequencies:")
    for i in range(min(6, len(sorted_letter_count))):
        print(f"{sorted_letter_count[i][0]}: {sorted_letter_count[i][1]}")

if __name__ == "__main__":
    # Example usage
    encrypted_message = "Hello, this is an example of an encrypted message. EeeEeEe."
    print(frequency_analysis(encrypted_message))
