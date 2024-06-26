# write code for rock paper and scissior game using python 
# rock beats scissor
# scissor beats paper
# paper beats rock
#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#By the end of each round, the player can choose whether to play again.
#Display the player's score at the end of the game.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
#The minigame should inform the player whether the player won, lost, or tied with the opponent.
#Choose to continue playing.
#At the prompt, type screen.
#the minigame should inform the player if the option entered by the player is invalid.
#Repeat steps 2 and 4 to play a few rounds and choose not to continue playing.
#Check if the minigame is terminated and if it displays your score, informing you of the number of wins and rounds.


import random  #import the random module to generate random numbers 
def rock_paper_scissors(): 
    player_score=0 #initialise the player score to 0
    computer_score=0    #initialise the computer score to 0
    while True: #while the condition is true  
        player=input("Enter rock, paper or scissors: ") #get the input from the player
        computer=random.choice(["rock","paper","scissors"]) #get the input from the computer
        print("Computer chose: ",computer) # print the choice of the computer  
        if player.lower() not in ["rock","paper","scissors"]: #if the player input is not in the list 
            print("Invalid option") #print invalid option
            continue #continue the loop  
        if player.lower()==computer: #if the player input is equal to the computer input  
            print("Tie")     #print tie  
        elif player.lower()=="rock": #if the player input is rock
            if computer=="scissors": #if the computer input is scissors     
                print("You win")    #print you win
                player_score+=1     #increment the player score by 1 
            else: #if the computer input is not scissors 
                print("You lose")  #print you lose
                computer_score+=1  #increment the computer score by 1
        elif player.lower()=="scissors": #if the player input is scissors  
            if computer=="paper": #if the computer input is paper 
                print("You win") #print you win 
                player_score+=1 #increment the player score by 1
            else: #if the computer input is not paper
                print("You lose") #print you lose
                computer_score+=1 #increment the computer score by 1 
        elif player.lower()=="paper":   #if the player input is paper 
            if computer=="rock":    #if the computer input is rock 
                print("You win")  #print you win
                player_score+=1     #increment the player score by 1
            else:   #if the computer input is not rock 
                print("You lose")   #print you lose
                computer_score+=1  #increment the computer score by 1 
        print("Player score: ",player_score)  #print the player score
        print("Computer score: ",computer_score) #print the computer score  
        play_again=input("Do you want to play again? ") #ask the player if they want to play again  
        if play_again.lower()!="yes": #if the player input is not yes
            break # break the loop 
rock_paper_scissors() #call the function rock_paper_scissors    

