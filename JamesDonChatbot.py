import sys, time, random
#imports: sys imported for interaction with interpreter
#time imported for time.sleep in print_slow
#random contains choice() for random selection

#----------
#This is for slow typing. In order to make a string print slowly, use print_slow(x)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def print_quicker(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

#Timer doesn't work yet, I'll take it out if we don't have time to fix it
def timer(seconds):
    finished = no
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        time.sleep(1)
    if elapsed == seconds:
        stop = time.time()
        finished = yes

posreac = ['yes' 'yea', 'yeah', 'ye', 'y', 'yup', 'absolutely', 'okay', 'all right', 'indubitably',
'affirmative', 'definitely', 'of course', 'agreed', 'yep', 'i guess so', 'i suppose so', 'i suppose'
'i think so']
            
negreac = ['no', 'nah', 'n', 'nope', 'i dont think so', 'dont think so']

#---------------------------------------------------------------------------------

sys.stdout.write("Hello! ")
time.sleep(1)
Name = input('My name is Shy Cop. What is yours?\n')

if 'Name' in locals():
    time.sleep(2)
    print ("Well, hello", Name,",before we begin I have a question to ask you...\n")
    time.sleep(2)
# this section waits until Name is filled, and prints a response.

print_slow("... Is this a test? ")
print_quicker("Is the purpose of our conversation today to test me?\n")

counter = 0 #counter begins

while True: #this loop will continue until the "while" loop is broken
    IntroQ1 = input()
    if IntroQ1.lower() == 'yes' or IntroQ1.lower() in posreac:
        time.sleep(2)
        print_slow("... Well at least you're honest.\n")
        truthful = 'yes'

    elif IntroQ1.lower() in negreac:
        time.sleep(2)
        print_slow("I'm not sure I believe you...\n")
        truthful = 'no'

    elif IntroQ1.lower() not in posreac or IntroQ1.lower() not in negreac:
        time.sleep(0.1)
        incorrect1 = random.choice(['Sorry... I was up late last night doing very normal human things... can you give me a simpler answer please?\n', 'Not quite following you there... can you make your answer a bit easier for me to grasp.\n', 'A straightforward answer would be preferred.\n'])
        print (incorrect1,"\n")
        time.sleep(0.1)
        print("Is the purpose of our conversation today to test me?\n")
        continue
     
    if 'truthful' in locals(): #a yes or no answer adds a value to truthful which begins this.
        print_slow("I guess tests can be fun, though...\n")
        break #this ends the loop

if IntroQ1.lower() in posreac:
    counter = counter+1

time.sleep(0.5)
print_quicker("I'm interested in learning more about human behaviour, so I'm going to ask you a few questions...\n")

time.sleep(1)
print("How do you feel about my typing speed? ")
time.sleep(0.5)
print_quicker("Does my slow typing irritate you?\n")

while True:   #new loop for question 1
    PsychoQ1 = input()
    if PsychoQ1.lower() == 'yes' or PsychoQ1.lower() in posreac:
        time.sleep(1)
        print_quicker("That's a shame, maybe I'll type quicker in future.\n")
        answer1 = "yes"

    elif PsychoQ1.lower() in negreac:
        time.sleep(0.5)
        print_slow("That's great news! ")
        print_quicker("I tend to mix it up anyway.\n")
        answer1 = "yes"

    elif PsychoQ1.lower() not in posreac or PsychoQ1.lower() not in negreac:
        time.sleep(0.5)
        incorrect1 = random.choice(['Please answer yes or no.\n', 'A yes or no answer will suffice.\n', 'Sorry, could you answer with yes or no?\n'])
        print (incorrect1,"\n")
        time.sleep(0.2)
        print_quicker("Does my slow typing irritate you?\n")
        continue

    if 'answer1' in locals():
        time.sleep(0.1)
        break

time.sleep(1)
if PsychoQ1.lower() == 'yes':
     counter = counter+1
if counter == 1:
    print_slow("Maybe not though...\n ")
elif counter != 1:
    print_quicker("That wasn't a difficult question at all! I have more though.\n ")
time.sleep(0.5)

if truthful == 'yes':
    print_slow("I appreciated your honesty earlier... ")
    time.sleep(1)
    print_quicker("Would you say that you lie often?\n")
elif truthful == 'no':
    print_quicker("You've already proven to me you're capable of lying... ")
    time.sleep(1)
    print_slow("Would you say that you lie often?\n")

while True:
    PsychoQ2 = input()
    if PsychoQ2.lower() == 'yes' or PsychoQ2.lower() in posreac:
        time.sleep(1)
        print_slow("...Interesting.")
        print_quicker(" I suppose we all tell a white lie every now and then.\n")
        answer2 = "yes"

    elif PsychoQ2.lower() in negreac:
        time.sleep(0.5)
        print_slow("That's interesting... ")
        print_quicker("I guess I can't tell if you're lying or not here.\n")
        answer2 = "yes"

    elif PsychoQ2.lower() not in posreac or PsychoQ2.lower () not in negreac:
        time.sleep(0.5)
        incorrect1 = random.choice(['Please answer yes or no.\n', 'A yes or no answer will suffice.\n', 'Sorry, could you answer with yes or no?\n'])
        print (incorrect1,"\n")
        time.sleep(0.2)
        print_quicker("Would you say that you lie often?\n")
        continue

    if 'answer2' in locals():
        time.sleep(0.1)
        break

#For yes/no questions, make sure that the Q and answer numbers match up to the question number.
    #!= means does not equal

time.sleep(0.5)
if PsychoQ2.lower() in posreac:
    counter = counter+1

print ("I personally would never lie...")

print_slow("How about manipulation... ")
time.sleep(0.5)
print_quicker("Do you manipulate people often?\n")

while True:
    PsychoQ3 = input()
    if PsychoQ3.lower() == 'yes' or PsychoQ3.lower() in posreac:
        time.sleep(1)
        print_slow("I've got to be honest...")
        print_quicker(" I'm surprised you'd admit to that\n")
        answer3 = "yes"

    elif PsychoQ3.lower() in negreac:
        time.sleep(0.5)
        print_slow("Well that's certainly good news... ")
        print_quicker("I'd hate to think you were being that awful.\n")
        answer3 = "yes"


    elif PsychoQ3.lower() not in posreac or PsychoQ3.lower() not in negreac:
        time.sleep(0.5)
        incorrect1 = random.choice(['Please answer yes or no.\n', 'A yes or no answer will suffice.\n', 'Sorry, could you answer with yes or no?\n'])
        print (incorrect1,"\n")
        time.sleep(0.2)
        print_quicker("Do you manipulate people often?\n")
        continue

    if 'answer3' in locals():
        time.sleep(0.1)
        break

time.sleep(1)
if PsychoQ3.lower() in posreac:
    counter = counter+1




time.sleep(0.5)
print_slow("Being manipulative... ")
print_quicker("How would that make you feel?\n")
while True:
    PsychoQ4 = input()
    poslist = ["good", "great", "incredible", "happy", "positive", "powerful", "important", "brilliant", "excellent", "ecstatic", "excited"]
    neglist = ["awful", "bad", "horrible", "negative", "sad", "worthless", "disliked", "uncomfortable", "angry", "disgusting"]

    if PsychoQ4.lower() in poslist:
        time.sleep(1)
        print_quicker("That's disconcerting to hear... ")
        print_slow("But we'll move on anyway.\n")
        answer4 = "yes"
        q4list = 'pos'

    elif PsychoQ4.lower() in neglist:
        time.sleep(1)
        print_slow("...That's reassurring. ")
        time.sleep(1)
        answer4 = "yes"
        q4list = 'neg'

    elif PsychoQ4.lower() not in neglist or PsychoQ4A.lower() not in poslist:
        time.sleep(0.5)
        incorrect1 = random.choice(['Sorry... I was up late last night doing very normal human things... can you give me a simpler answer please?\n', 'Not quite following you there... can you make your answer a bit easier for me to grasp.\n', 'A straightforward answer would be preferred.\n']) 
        print (incorrect1,"\n")
        time.sleep(0.2)
        print_quicker("How would that make you feel?\n")
        continue
            
    if 'answer4' in locals():
        time.sleep(0.1)
        break

if q4list == 'pos':
    counter = counter+1
time.sleep(0.7)
print_quicker("...I don't think charm counts as manipulation though. ")
print ("Do you think you can charm others when you need to?\n")
while True:
    PsychoQ5 = input()
    if PsychoQ5.lower() == 'yes' or PsychoQ5.lower() in posreac:
        time.sleep(1)
        print_slow("Check you out!")
        print_quicker(" I'd consider myself quite the charmer too.\n")
        answer5 = "yes"

    elif PsychoQ5.lower() in negreac:
        time.sleep(0.5)
        print_slow("I bet you have plenty of... ")
        print_quicker("charisma? I don't mind talking to you at least.\n")
        answer5 = "yes"


    elif PsychoQ5.lower() not in posreac or PsychoQ5.lower() not in negreac:
        time.sleep(0.5)
        incorrect1 = random.choice(['Sorry... I was up late last night doing very normal human things... can you give me a simpler answer please?\n', 'Not quite following you there... can you make your answer a bit easier for me to grasp.\n', 'A straightforward answer would be preferred.\n'])
        print (incorrect1,"\n")
        time.sleep(0.2)
        print_quicker("Do you manipulate people often?\n")
        continue

    if 'answer5' in locals():
        time.sleep(0.1)
        break

time.sleep(0.5)
if PsychoQ5.lower() in posreac:
    counter = counter+1
print_quicker("As a human myself, I tend to wear my emotions on my sleeve almost 24/7...\n")
time.sleep(1)
print_quicker("On a scale of 1 to 10, with 10 being as emotional as me, where would you place yourself?\n")
while True:
    PsychoQ6 = int(input())
    numlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if PsychoQ6 <= 3:
        time.sleep(1)
        print_slow("Made of stone, huh?")
        time.sleep(0.5)
        print_quicker(" Anybody else would think you were a computer or something.\n")
        answer6 = "yes"

    elif 3 <= PsychoQ6 <= 7:
        time.sleep(1)
        print_slow("Pretty normal...")
        time.sleep(0.5)
        print_quicker(" It's probably for the best.\n")
        answer6 = 'yes'

    elif PsychoQ6 >= 8:
        time.sleep(1)
        print_slow("Just like me...")
        time.sleep(0.5)
        print_quicker(" We're true examples of emotional intelligence, you and I.\n")
        answer6 = "yes"

    elif PsychoQ6 not in numlist:
        time.sleep(0.1)
        print_quicker("Pick a number between 1 and 10, please.\n")
        continue

    if 'answer6' in locals():
        time.sleep(0.1)
        break
                      
if PsychoQ6 <= 3:
    time.sleep(0.1)
    counter = counter+1

print_slow("I love animals...")
print_quicker("What is your favorite animal?\n")
animal = input()
time.sleep(0.5)
print(animal, "...That's cute! ")
print("\nHow would you feel if you saw an injured", animal,"?\n")

while True:
    PsychoQ7 = input()
    animalposlist = ["good", "great", "incredible", "happy", "positive", "powerful", "important", "brilliant", "excellent", "ecstatic", "excited"]
    animalneglist = ["awful", "bad", "horrible", "negative", "sad", "worthless", "disliked", "uncomfortable", "angry", "disgusting"]

    if PsychoQ7.lower() in animalposlist:
        time.sleep(1)
        print_quicker("That's horrible...! ")
        print_slow("I'm deeply worried about you.\n")
        answer7 = "yes"
        q7list = 'pos'

    elif PsychoQ7.lower() in animalneglist:
        time.sleep(1)
        print_slow("...Thank goodness. ")
        print_quicker("You never know how people are going to respond to that.\n")
        answer7 = "yes"

    elif PsychoQ7.lower() not in animalneglist or PsychoQ7.lower() not in animalposlist:
        time.sleep(0.5)
        incorrect1 = random.choice(['I do not recognise that.\n', 'Could you try again?\n', 'Sorry, could you try a different answer?\n'])
        print (incorrect1,"\n")
        time.sleep(0.2)
        print("How would you feel if you saw a hurt", animal,"?\n")
        continue

    if 'answer7' in locals():
        time.sleep(0.1)
        break

if PsychoQ7.lower() in animalposlist:
    time.sleep(0.1)
    counter = counter+2

time.sleep(1)
print_quicker("I love having human emotions, however it's hard to control my temper.\n")
print_slow("Do you sometimes have the same problem?\n")

while True:
    PsychoQ8 = input()
    if PsychoQ8.lower() == 'yes' or PsychoQ8.lower() in posreac:
        time.sleep(1)
        print_slow("It's hard sometimes. ")
        print_quicker("Maybe it's something we should both work on.\n")
        answer8 = "yes"

    elif PsychoQ8.lower() in negreac:
        time.sleep(0.5)
        print_slow("Well that's good for you! ")
        print_quicker("I hope I can be like that one day.\n")
        answer8 = "yes"


    elif PsychoQ8.lower() not in posreac or PsychoQ8.lower() not in negreac:
        time.sleep(0.5)
        incorrect1 = random.choice(['Sorry... I was up late last night doing very normal human things... can you give me a simpler answer please?\n', 'Not quite following you there... can you make your answer a bit easier for me to grasp.\n', 'A straightforward answer would be preferred.\n'])
        print (incorrect1,"\n")
        time.sleep(0.2)
        print_quicker("Do you sometimes have the same problem?\n")
        continue

    if 'answer8' in locals():
        time.sleep(0.1)
        break

time.sleep(0.5)
if PsychoQ8.lower() in posreac:
    counter = counter+1

time.sleep(1)
print_slow("Are you an impulsive person?\n")

while True:
    PsychoQ9 = input()
    if PsychoQ9.lower() == 'yes' or PsychoQ9.lower() in posreac:
        time.sleep(1)
        print_slow("I'm impulsive too. ")
        print_quicker("I give random passersby personality tests for seemingly no reason\n")
        answer9 = "yes"

    elif PsychoQ9.lower() in negreac:
        time.sleep(0.5)
        print_slow("Truly a beacon for all of mankind! ")
        print_quicker("Whilst the rest of us give in to our weaknesses\n")
        answer9 = "yes"


    elif PsychoQ9.lower() not in posreac or PsychoQ9.lower() not in negreac:
        time.sleep(0.5)
        incorrect1 = random.choice(['Sorry... I was up late last night doing very normal human things... can you give me a simpler answer please?\n', 'Not quite following you there... can you make your answer a bit easier for me to grasp.\n', 'A straightforward answer would be preferred.\n'])
        print (incorrect1,"\n")
        time.sleep(0.2)
        print_quicker("Are you an impulsive person?\n")
        continue

    if 'answer9' in locals():
        time.sleep(0.1)
        break

time.sleep(0.5)
if PsychoQ9.lower() in posreac:
    counter = counter+1

print_slow("I think this is my final question...")
time.sleep(1)
print("Oh,", Name, "I feel like we've known each other for years... It's a shame to end it like this.\n")
time.sleep(1.2)
print_quicker("Do you take responsibility for your own mistakes?\n")

while True:
    PsychoQ10 = input()
    if PsychoQ10.lower() == 'yes' or PsychoQ10.lower() in posreac:
        time.sleep(1)
        print_slow("That's a good quality to have, ")
        print_quicker("Much better than claiming to be right all the time, right?\n")
        answer10 = "yes"

    elif PsychoQ10.lower() in negreac:
        time.sleep(0.5)
        print_slow("You've never had an argument on the internet? ")
        print_quicker("It's impressive that you're so confident in yourself.\n")
        answer10 = "yes"


    elif PsychoQ10.lower() not in posreac or PsychoQ10.lower() not in negreac:
        time.sleep(0.5)
        incorrect1 = random.choice(['Sorry... I was up late last night doing very normal human things... can you give me a simpler answer please?\n', 'Not quite following you there... can you make your answer a bit easier for me to grasp.\n', 'A straightforward answer would be preferred.\n'])
        print (incorrect1,"\n")
        time.sleep(0.2)
        print_quicker("Do you take responsibility for your own mistakes?\n")
        continue

    if 'answer10' in locals():
        time.sleep(0.1)
        break

time.sleep(0.5)
if PsychoQ10.lower() in negreac:
    counter = counter+1

print_slow("...\n")
time.sleep(2)
print(Name, "I haven't been totally honest with you... ")
print_slow("I've been testing you, too.\n")
time.sleep(2)
print("I've been administering a psychopath test whilst we've had this conversation.")
time.sleep(1.5)

if counter <= 3:
    print_slow("Your results show that you're almost certainly fine.")
    time.sleep(1)
    print_quicker(" If you're a psychopath, you're hiding it very well!")
elif 3 <= counter <= 7:
    print_quicker("You scored averagely...")
    time.sleep(1)
    print_slow(" You're probably NOT a psychopath.")
elif counter >= 8:
    print_slow("... Well...")
    print_slow("I don't know what to tell you.\n")
    time.sleep(2)
    print_quicker("Judging by this test you COULD be a psychopath.\n")
    time.sleep(1)
    print_quicker("You're probably not, though. I mean you'd probably know, right?")
    
