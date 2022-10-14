import random

# Personal preference. I always like to have functions declared globally before entering the loop. Its more organised
def getAnswer(answerNumber):
  if answerNumber == 1:
    return 'It is certain.'
  elif answerNumber == 2:
    return 'It is decidedly so.'
  elif answerNumber == 3:
    return 'Yes.'
  elif answerNumber == 4:
    return 'Reply hazy try again.'
  elif answerNumber == 5:
    return 'Ask again later.'
  elif answerNumber == 6:
    return 'Concentrate and ask again.'
  elif answerNumber == 7:
    return 'My reply is no.'
  elif answerNumber == 8:
    return 'Outlook not so good.'
  elif answerNumber == 9:
    return 'Very doubtful.'

#Your program starts here
# An infinate loop
while True:
  
  #I'm going to change the variable r to something more meaningful and less confusing. Lets say.... choices
  #Here is another variable that generates a number from 1 to 9
  choices = random.randint(1,9)

  #Message. Instructions to show up on screen
  print('Press "r" for an answer.')
  
  #Player enters an answer. The answer is then stored in the userMove variable
  userMove = input()



  #Conditions, this is the part where you tell the program what to do
  
  #If userMove equals r, run the function getAnswer
  if userMove == 'r':
    #Run the function getAnswer as 'fortune' and pass a random number generated from the choices variable then call the getAnswer function from above
    #The word fortune can be anything. It just saves you from typing something like print(getAnswer(choices) + '\n\n')
    fortune = getAnswer(choices)
    #Print out the answer from the getAnswer
    print(fortune + '\n\n')

  #If userMove equals exit, leave the loop and exit program
  elif userMove == 'exit':
    break

  #If the input is not r or exit. Throw a tandrum and repeat loop
  else:
    print('I will listen if you enter "r"')
