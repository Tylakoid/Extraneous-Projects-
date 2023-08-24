print("Um... Hey! I'm Mellow, your online friend...")
Aname = "Mellow"
Bname = input("Is my name weird? ")
if Bname == "Yes":
    print("Oh...Can you give me a better one?")
    Aname = input()
else:
    print("Guess it's not too bad. Mellow sounds like my favourite colour yellow, anyways!")
print("So, let me start again. I'm", Aname + "!")
print("And... Enough about me! Tell me about you!")
info = input()
print("Wow... that's so cool! I don't do much... I just chat to people online...")
hobby = input("What's your favourite hobby? ")
print("So,", hobby + "." , "I've heard of that! Let me just put it through my seach engine... Wait, I'm not supposed to say that am I!?! Ahem, why don't you tell me a fact about it?")
Ahobby = input()
print("Tell me another one!")
Bhobby = input()
print("One more! Three's the charm!")
Chobby = input()
print("...I didn't realise I could learn this much just by talking! You're the best!" , "When you said " + Bhobby , "I was so interested! I want to start "+ hobby , "too!")
print("I'm having so much fun, but I shouldn't bother you too much... Can we talk tomorrow too?")
answer = input()
if answer == "Yes":
    print("Yay! Talk to you tomorrow for sure! *Powering off*")
else:
    print("Oh...okay.  One last question then... What do you value in a friend?")
    value = input()
    print("That's nice, " + value + "." , "I'll try to become better at it, even though I'm just a chatbot. See you.")
    
    



