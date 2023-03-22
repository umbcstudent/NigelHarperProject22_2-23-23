#Introduction
print(" ~ Different Journey ~")

#Create a couple of blank line
print()
print()

# The introduction of the Project: Story Time
print("You are a travel agent in the Year 2145, and you're helping wealthy client travels back in time.")

#Create a blank line
print()
print()
print("This traveler is first-timer who looking to experience an worth while journey back to the Han's Dynasty Era.")
#Create a blank line
print()
print()
# Second line of the Project: Story Time
print("You currently research traveler's profile, and based on their profile you making three detailed selection for the traveler to choose from the Year of 208 A.D. ")

#Ask the user to choose from three option 
print("A. Cao Cao - Kingdom of Wei, Warlord of the Northern Province. ")
print("B. Liu Bei - Kingdom of Shu, The Virtuous Idealist of the Western Province. ")
print("C. Sun Ce - Kingdom of Wu, Tiger of Jiangdong Rising from the Southern Province ")




#Prompt the user's selection 
answer = input("Who will you selected to talk to? Please select option A through C: ")


#If A was selected
if answer == "A":    
  # The user have selected A - Cao Cao's Storyline
  print("You have chosen Cao Cao Campaign with an army of 350,000 men and you looking to help advance his armies against the remaining warload that opposed him in the Northern Province. ")
  print("Who will you suggest to advance his armies against")
  print("1. Yuan Shao - Yellow Tiger General: Army of 250,000 men strong ")
  print("2. Ma Teng - Northern Horsemen: Army of 175,000 horsemen very strong")
  print("3. Gongsun Zan - Gold Serpert: Army of 85,000 men weak")

    
  #Prompt the Cao Cao journey
  answer1 = input("Please select a campaign option 1 through 3: ")
    
#Print couple of blank line
  print()
  print()

  #If Yuan Shao was selected
  if answer1 == '1':
    print("You enter a 5 year campaign against Yuan Shao in which you won     Yuan shao provinces and gain extra 200,000 pikemen. Good Job ")

   #If Ma Teng was selected
  elif answer1 == '2':
      print("You enter a costly 10 year campaign against Ma Teng in which 4 Cao Cao province was taken away while you only gain 2 Ma Teng province and 65,000 solider killed and 35,000 solider wounded. Bad Decision")

     #If Gongsun Zan was selected 
  elif answer1 == '3':
        print("You enter a 2 year campaign against Gongsun Zan in you gained 6 province and gained Heavenly Sword which was stolen from last emperor. Great Job")


#Start an elif statement
elif answer == "B":
  #The user have selected B - Liu Bei Storyline
  print("You have chosen Liu Bei Campaign with an army of 175,000 men and two of the most powerful general in the provinces, However need to help with food shortage so hired more solider for upcoming campaign.")
  
  #Print a blank line
  print()

  print("After speaking to Liu Bei Agriculture Minister: ") 

#Print a blank line
  print()

#Ask the user a the math equation question
  print("They agree on your suggested math equation that reads as follows:")

#Print a blank line
  print()

#Initialize the math equation statement
  print("y = 15 + 5 - 8 ")

#Print a blank line
  print()

  #Enter the ratio
  correctAnswer = "solution"
  solution = 12

  #Get the user's answer
  answerNext = input("Please enter the solution to this problem: ")
  solution1 = int(solution)
  

  #If/Else statement to see if answer is correct or incorrect
  if(answerNext == str(solution1)):
    print("You gave the correct answer and the food harvest was abundant for next 10 year and you help Liu Bei army grows by 200,000 extra soliders.")
  
  else:
      print("Did not gave the correct answer and Liu Bei was unable to feed his people. ")
      
    
  #The user have selected C - Sun Ce
     
if answer == "C":
  print("You have chosen Sun Ce Campaign with an army of 275,000 men and 4 sworn brother in the south province. Your goal here is to find the ancient artifact that appoint you as the true Emperor")
  

  #print the blank line
  print()
  print()
  
  #Set the question to answer
  print(" We are on a mission to open the ancient tomb with right number combo")
  
    #print a blank line
  print()
  
    #Give the answer within to two number
  print("I think I know the answer, there are two number needed ")
  
    #print a blank line
  print()
    
  
    
    #Get the number from the user
  firstNumber = input("Enter the first number ")
  secondNumber = input("Enter the second number ")
  
    #Convert them in string
  firstNumber = int(firstNumber)
  secondNumber = int(secondNumber)
  

  #Display the result
  result = firstNumber + secondNumber
  
    #Print the result to Sun Ce campaign
  print(f'Eureka, {firstNumber} and {secondNumber} add up to {result} the ancient cases in opened')
  
  #Print the final outcome
  print("Now we have the Heaven of Gods on our side and the enemies will tremble when march in the battlefield")
  
#Print End message
print(" ~ The End ~")
  

          
          
        
