print("what is your name?")

name = input()

print("hi "  + name + " let me guess how old you are")

if name == "Oscar":
    print("Oscar is aged 8")
elif name == "Ben":
    print("Ben is aged 6")
else:
    print("i'm not sure how old you are " + name)

print("what are you doing today " + name)

activity = input()

print("how many times are you " + activity + "?")

number = int(input())

for x in range(number):
  print(activity + " " + str(x))

print("good work " + name + " well done")
