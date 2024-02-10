score = 0
score = int(score)


name = input("What is your name?: ")
name = name.title()
print("""Hello {}, welcome to Quiz night! 
You will be presented with 5 questions.
Enter the appropriate number to answer the question
Good luck!\n\n""".format(name))


print("""Which Indian city is the capital of Two states?
1. Chandhigarh 
2. Kolkata
3. Delhi 
4. Banglore""")

answer1 = "1"
response1 = input("Your answer is: ")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response1 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5\n\n")


print("""Which city is the capital of India?
1. Jaipur 
2. Chennai 
3. New Delhi
4. Mumbai""")

answer2 = "3"
response2 = input("Your answer is: ")

if (response2 != answer2):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response2 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5\n\n")


print("""Where is the Taj Mahal Located?
1. Bhopal
2. Agra 
3. Mumbai 
4. Lucknow""")

answer3 = "2"
response3 = input("Your answer is: ")

if (response3 != answer3):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response3 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5\n\n")


print("""Which is the smallest state of India?
1. Goa
2. Mumbai
3. Rajasthan
4. Bihar""")

answer4 = "1"
response4 = input("Your answer is: ")

if (response4 != answer4):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response4 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5\n\n")


print("""Which is the longest river in India ?
1. Godavari
2. Yamuna
3. Ganga
4. Kaveri""")

answer5 = "3"
response5 = input("Your answer is: ")

if (response5 != answer5):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response5 + " is correct!")
    score = score + 1

print("Your total score is " + str(score) + " out of 5\n\n")
print("Thank you for playing {}!!!".format(name))