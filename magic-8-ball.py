import random

name = ""
question = "Will you be my Valentine?"
answer = ""

random_number = random.randint(1, 15)
print(random_number)

if random_number == 1:
  answer = "Yes - definately"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Without a doubt, i will be there for you"
elif random_number == 11:
  answer = "Don't Worry, i have plans for you"
elif random_number == 12:
  answer = "Ask again later, maybe it will be your luck"
elif random_number == 13:
  answer = "You mean you will be with me, awwwh"
elif random_number == 14:
  answer = "I can't remember the last time i had something with you"
elif random_number == 15:
  answer = "Maybe we should give it a try this time round"
else:
  answer = "Error"


if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

if question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
else:
  #print(name + " asks: " + question)
  print("Magic 8-Ball's answer is: " + answer)
#print("Magic 8-Ball's answer is: " + answer)
  
