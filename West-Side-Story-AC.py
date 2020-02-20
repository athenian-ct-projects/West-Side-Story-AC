print("West Side Story trivia game \nOther materials needed: Game board with questions \nby AC '23")

def show_score(a, max):
    print("your score is: "+ str(a))
    print("maximum score is: " + str(max))

i = 1
for i in range (1,4):
    print(i)

print("Let's go!!!")

topic1 = "Finish that Lyric"
topic2 = "Name that Character"
topic3 = "The Fight"
topic4 = "General Trivia"
a = 0
print("In this game, 1 = Finish that Lyric, 2 = Name that Character, 3 = The Fight, and 4 = General Trivia")
max = 0
prompt = input("Choose a number between 1 and 4: ")

#ask question 1
while prompt == "1":
    print("look at the flap A1")
    answer = input("type your answer here: ")
    if answer == "Krup" or answer == "krup":
        print("That is correct!!!")
        print("Whoo Hooooooo!!!")
        a = a + 100
    else:
        print("That is incorrect...")
        print("Sorry")
        a = a - 50
           
#ask question 2
    print("look at flap A2")
    answer = input("type your answer here: ")
    if answer == "Witty and bright" or answer == "witty and bright":
        print("That is correct!!!")
        print("Why, aren't you witty and bright!!!")
        a = a + 150
    else:
        print("That is incorect...")
        print("Don't worry, you're still witty and bright!")
        a = a - 50
    
#ask question 3
    print("Look at flap A3")
    answer = input("type your answer here: ")
    if answer == "You've got brothers around" or answer == "you've got brothers around" or answer == "Youve got brothers around" or answer == "youve got brothers around":
        print("That is correct!!!")
        print("You're the top cat in town!")
        a = a + 200
    else: 
        print("That is incorrect...")
        print("Sorry!")
        a = a - 50
    
#ask question 4
    print("look at flap A4")

    answer = input("type your answer here: ")
    if answer == "And suddenly that name will never be the same to" or answer == "and suddenly that name will never be the same to":
        print("That is correct!!!")
        print("The most beautiful sound I ever heard...")
        a = a + 250
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 50

#ask question 5
    print("look at flap A5")
    answer = input("type your answer here: ")
    if answer =="Real cool" or answer == "real cool":
        print("That is correct!!!")
        print("Yay!")
        a = a + 300
    else:
       print("That is incorrect...")
       print("Sorry!")
       a = a - 100
    
#ask question 6
    print("look at flap A6")
    answer = input("type your answer here: ")
    if answer == "Somewhere" or answer == "somewhere":
        print("That is correct!!!")
        print("All the beautiful sounds of the world in those three words")
        a = a + 350
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 100

#ask question 7
    print("look at flap A7")
    answer = input("type your answer here: ")
    if answer == "There is no right or wrong" or answer == "there is no right or wrong":
        print("That is correct!!!")
        print("There is a right, actually, and you got it!")
        a = a + 400
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 100

#ask question 8
    print("look at flap A8")
    answer = input("type your answer here: ")
    if answer == "And what was just a world is a star" or answer == "and what was just a world is a star":
        print("That is correct!!!")
        print("I know now you were right!")
        a = a + 450
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 100

    max = max + 2200
    show_score(a, max)
 
    prompt = input("Choose another number: ")



while prompt == "2":
#ask question 1 
    print("look at flap B1")
    answer = input("type your answer here: ")
    if answer == "Tony" or answer == "tony":
        print("That is correct!!!")
        a = a + 50
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 50

#ask question 2
    print("look at flap B2")
    answer = input("type your answer here: ")
    if answer == "Chino" or answer == "chino":
        print("That is correct!!!")
        a = a + 100
    else:
        print("That is incorrect...")
        print("Sorry!")        
        a = a - 50

#ask question 3
    print("look at flap B3")
    answer = input("type your answer here: ")
    if answer == "Bernardo" or answer == "bernardo":
        print("That is correct!!!")
        a = a + 150
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 50
    
#ask question 4 
    print("look at flap B4")
    answer = input("type your answer here: ")
    if answer == "Riff" or answer == "riff":
        print("That is correct!!!")
        a = a + 200
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 50
    
#ask question 5 
    print("look at flap B5")
    answer = input("type your answer here: ")
    if answer == "Doc" or answer == "doc":
        print("That is correct!!!")
        a = a + 250
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 100

    max = max + 750
    show_score(a, max)
    prompt = input("Choose another number")
  

    


while prompt == "3":
#Start "The Fight"
#ask question 1
    print("look at flap C1")
    answer = input("type your answer here: ")
    if answer == "Under the highway" or answer == "under the highway":
        print("That is correct!!!")
        a = a + 50
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 50

#ask question 2
    print("look at flap C2")
    answer = input("type your answer here: ")
    if answer == "Bernardo" or answer == "bernardo":
        print("That is correct!!!")
        a = a + 100
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 50

#ask question 3
    print("look at flap C3")
    answer = input("type your answer here: ")
    if answer == "Bernardo" or answer == "bernardo":
        print("That is correct!!!")
        a = a + 150
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 50
    
#ask question 4
    print("look at flap C4")
    answer = input("type your answer here: ")
    if answer == "Chino" or answer == "chino":
        print("That is correct!!!")
        a = a + 200
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 50
    
#ask question 5
    print("look at flap C5")
    answer = input("type your answer here: ")
    if answer == "Maria" or answer == "maria":
        print("That is correct!!!")
        a = a + 250
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 100
    
    max = max + 750
    show_score(a, max)
    prompt = input("Choose another number")


while prompt == "4":
#start "General Trivia"
#ask question 1
    print("look at flap D1")
    answer = input("type your answer here: ")
    if answer == "Sharks" or answer == "sharks":
        print("That is correct!!!")
        a = a + 50
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 50

#ask question 2
    print("look at flap D2")
    answer = input("type your answer here: ")
    if answer == "Puerto Rico":
        print("That is correct!!!")
        a = a + 100
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 50

#ask question 3
    print("look at flap D3")
    answer = input("type your answer here: ")
    if answer == "Manhattan" or answer == "manhattan" == "New York City" or answer == "New york city" or answer == "new york city":
        print("That is correct!!!")
        a = a + 150
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 50

#ask question 4
    print("look at flap D4")
    answer = input("type your answer here: ")
    if answer == "dress" or answer == "Dress":
        print("That is correct!!!")
        a = a + 200
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 50

#ask question 5
    print("look at flap D5")
    answer = input("type you answer here: ")
    if answer == "Stephen Sondheim" or answer == "Stephen sondheim" or answer == "stephen sondheim" or answer == "stephen Sondheim":
        print("That is correct!!!")
        a = a + 250
    else:
        print("That is incorrect...")
        print("Sorry!")
        a = a - 100

    max = max + 750
    show_score(a, max)
    prompt = input("Choose another number: ")

if prompt != "1" and prompt != "2" and prompt != "3" and prompt != "4":
    print("Your score is:"+ str(a))
    print("Maximum score for the entire game is "+ str(max))
    print("well done!")
    print("Good luck with WSS!!")
    print("Enjoy the rest of your day!")
