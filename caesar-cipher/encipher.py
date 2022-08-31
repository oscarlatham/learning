phrase = input("Enter the phrase to encipher: ")
key = int(input("Enter the encipher key: "))
result = ""

for i, char in enumerate(phrase):
    result += chr((ord(char) + key - 97) % 26 + 97)

print(phrase + " = " + result)