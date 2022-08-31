phrase = input("Enter the phrase to decipher: ")
key = int(input("Enter the decipher key: "))
result = ""

for i, char in enumerate(phrase):
    result += chr((ord(char) - key - 97) % 26 + 97)

print(phrase + " = " + result)