##################################################################################
################################## MASTERIND #####################################
##################################################################################
#
# 1. This program draws the game board for Mastermind by drawing initial lines
#    that are then augmented with loops repeat the game boards drawn lines and
#    circles. After repetition, the game board is created.
#
# 2. Defines a random set of colors that the player will have to solve for
#
# 3. Allows the player to type a guess in using just the first letter of the color
#    they want to guess. ex. yygb.
#
# 4. Calculates whether the player guessed correct colors / positions, and then
#    displays these as:
#           Black = A guessed color is correct, and in the correct position.
#           White = A guess color is correct, but in the wrong position.
#           
# 5. Continues running the loop of steps 3/4 until either the player wins, or
#    runs out of guesses/loses. 
#
###################################################################################
###################################################################################
###################################################################################

from graphics import*
from random import*

def board_draw(game_choice):

    if game_choice == "Mastermind":
        win = GraphWin("Mastermind", 450, 710)
        win.setCoords(-5, -205, 455, 705)
        win.setBackground("Orange")

        # draw horizontal/vertical lines for Mastermind
        for i in range(0, 501, 50):
            hori_line = Line(Point(0, i), Point(300, i))
            hori_line.draw(win)

        for i in range(0, 350, 50): 
            vert_line = Line(Point(i, 0), Point(i, 500))
            vert_line.draw(win)

        for i in range(0, 475, 50):
            previous_guess = Rectangle(Point(300, 0+i), Point(450, 25+i))
            previous_guess.draw(win)

        for i in range(0, 500, 50):
            guess_text = Text(Point(350, 37+i), "Results")
            guess_text.draw(win)

        # draw box for color selection
        color_box = Rectangle(Point(0, -150), Point(450, -10))
        color_box.draw(win)

        # draw box for entry
        enter_box = Rectangle(Point(0, -160), Point(450, -200))
        enter_box.draw(win)

        # Entry text
        enter_text = Text(Point(325, -180), "Type guess, then click on board!")
        enter_text.draw(win)

        # color selection text
        color_select = Text(Point(200, -25), "Color selection Palate")
        color_select.setSize(16)
        color_select.draw(win)

        # Circles for Color
        red_circle = Circle(Point(40, -80), 30)
        red_circle.setFill("red")
        red_circle.draw(win)

        green_circle = Circle(Point(122, -80), 30)
        green_circle.setFill("green")
        green_circle.draw(win)

        yellow_circle = Circle(Point(194, -80), 30)
        yellow_circle.setFill("yellow")
        yellow_circle.draw(win)

        purple_circle = Circle(Point(266, -80), 30)
        purple_circle.setFill("purple")
        purple_circle.draw(win)

        purple_circle = Circle(Point(338, -80), 30)
        purple_circle.setFill("Teal")
        purple_circle.draw(win)

        purple_circle = Circle(Point(410, -80), 30)
        purple_circle.setFill("Silver")
        purple_circle.draw(win)
     
        # title text
        title_text = Text(Point(225, 600), "MASTERMIND")
        title_text.setSize(36)
        title_text.setFill("Cyan")
        title_text.draw(win)

        # draw main board circles
        for j in range(0, 500, 50):
            for i in range(0, 300, 50):
                board_circle = Circle(Point(i+25, j+25), 25)
                board_circle.draw(win)

        # draw results circles
        for j in range(0, 500, 50):
            for i in range(300, 450, 25):
                results_circle = Circle(Point(i+12, j+12), 12)
                results_circle.draw(win)

        guess_list = ["r", "g", "y", "p", "t", "s"]

        # Draw text selection
        red_text = Text(Point(40, -130), "r")
        red_text.setSize(16)
        red_text.draw(win)

        green_text = Text(Point(122, -130), "g")
        red_text.setSize(16)
        green_text.draw(win)

        yellow_text = Text(Point(194, -130), "y")
        red_text.setSize(16)
        yellow_text.draw(win)

        purple_text = Text(Point(266, -130), "p")
        red_text.setSize(16)
        purple_text.draw(win)

        teal_text = Text(Point(338, -130), "t")
        red_text.setSize(16)
        teal_text.draw(win)

        silver_text = Text(Point(410, -130), "s")
        red_text.setSize(16)
        silver_text.draw(win)
        
        
        
   
    else:
        print("Something has gone wrong with board_draw!")

    return win

    
def game_rules(game_choice):
    if game_choice == "Mastermind":

        guess_list = ["r", "g", "y", "p", "t", "s"]
        solution_list = []

        for i in range(6):
            solution_list.append((guess_list[randrange(0,6)]))

        return solution_list
    
    else:
        print("Something has gone wrong!")        
        
def mastermind(game_board, secret_code):
    print(
          "Welcome to Mastermind! \n"
          "\n"
          " --- To play, type the first letter of each color you whish to guess into \n"
          "the console. For example, the guess 'Red, Red, Red, Red' would be typed \n"
          "as 'rrrr' in the console, without the ''. \n"
          "\n"
          " --- The results of your guesses, as well as the guess itself will both be \n"
          "displayed in the console, as well as on the game board. \n"
          "\n"
          " --- To the right of your guesses will be your results! \n"
          "\n"
          " --- A Black circle indicates that you have guessed a color correctly, and in \n"
          "the correct position! \n"
          "\n"
          " --- A White circle indicates that you have guessed a color correctly, but \n"
          "NOT in the correct position! \n"
          "\n"
          "ARE YOU THE MASTERMIND? \n"
          "LETS FIND OUT! GOOD LUCK! \n"
          )

    win = game_board 
    turns = 0
    win_condition = []

    
    # While game is still running, play the game
    while win_condition != secret_code and turns != 11:

        # incriment the turn
        turns += 1
        if turns >= 11:
            break

        # incriment the y axis for circle drawing
        y = turns-1

        # get the player guess
        player_guess_enter = Entry(Point(100, -180), 20)
        player_guess_enter.setFill("White")
        player_guess_enter.draw(win)

        

        pause = win.getMouse()
        player_guess_input = player_guess_enter.getText()
        print(player_guess_input)

        # make sure the player typed something we can use
        for i in range(len(secret_code)):
            while (len(player_guess_input)) != 6 or ((player_guess_input[i] != "r") and (player_guess_input[i] != "g") and
                                                     (player_guess_input[i] != "y") and (player_guess_input[i] != "p") and
                                                     (player_guess_input[i] != "t") and (player_guess_input[i] != "s")):
                player_guess_enter.setText("Invalid Entry! Please try again!")
                pause = win.getMouse()
                player_guess_input = player_guess_enter.getText()                   
                    
        # Make the player_guess into lists for use later
        player_guess_raw_list = []
        player_guess_wht = []
        circles_colors = []

        for i in range(len(player_guess_input)):
            player_guess_raw_list.append(player_guess_input[i])
            player_guess_wht.append(player_guess_input[i])
            circles_colors.append(player_guess_input[i])

        # setup win condition
        win_condition = []

        # set up a list to reference our secret code, that is not the secret code
        blk_wht_list = [secret_code[0],secret_code[1],secret_code[2],secret_code[3], secret_code[4], secret_code[5]]


        # Create master blk/wht list off of player guesses
        for i in range(len(secret_code)):

            # win condition list
            win_condition.append(player_guess_input[i])

            # change blk_wht_list values to "blk" or "wht"         
            for j in range(len(secret_code)):
                if player_guess_raw_list[j] == blk_wht_list[j]:
                    blk_wht_list[j] = "blk"
                    player_guess_wht[j] = "blk"

                elif blk_wht_list[i] == player_guess_wht[j] and player_guess_wht[j] != "blk":
                    blk_wht_list[i] = "wht"
                    player_guess_wht[j] = ""
           
        # print the results                        
        for i in range(6):
            if blk_wht_list[i] == "blk":
                print(blk_wht_list[i])
                
        for i in range(6):
            if blk_wht_list[i] == "wht":
                print(blk_wht_list[i])

        # Draw the appropriate circles onto the game board
        # First, format circles_colors into colors we will draw on
        for i in range(len(circles_colors)):
            if circles_colors[i] == "r":
                circles_colors[i] = "Red"
            elif circles_colors[i] == "g":
                circles_colors[i] = "Green"
            elif circles_colors[i] == "y":
                circles_colors[i] = "Yellow"
            elif circles_colors[i] == "p":
                circles_colors[i] = "Purple"
            elif circles_colors[i] == "t":
                circles_colors[i] = "Teal"
            elif circles_colors[i] == "s":
                circles_colors[i] = "Silver"

        for i in range(len(blk_wht_list)):
            if blk_wht_list[i] == "blk":
                blk_wht_list[i] = "Black"
            elif blk_wht_list[i] == "wht":
                blk_wht_list[i] = "White"
            elif blk_wht_list[i] == "r":
                blk_wht_list[i] = "Orange"
            elif blk_wht_list[i] == "g":
                blk_wht_list[i] = "Orange"
            elif blk_wht_list[i] == "y":
                blk_wht_list[i] = "Orange"
            elif blk_wht_list[i] == "p":
                blk_wht_list[i] = "Orange"
            elif blk_wht_list[i] == "t":
                blk_wht_list[i] = "Orange"
            elif blk_wht_list[i] == "s":
                blk_wht_list[i] = "Orange"         

        # Create a new list we're going to append to - this is to
        # make blk/wht colors display not in their exact positions
        blk_wht_circle_hidden = []
        for i in range(len(blk_wht_list)):
            if blk_wht_list[i] == "Black":
                blk_wht_circle_hidden.append(blk_wht_list[i])
        for i in range(len(blk_wht_list)):
            if blk_wht_list[i] == "White":
                blk_wht_circle_hidden.append(blk_wht_list[i])
        for i in range(len(blk_wht_list)):
            if blk_wht_list[i] == "Orange":
                blk_wht_circle_hidden.append(blk_wht_list[i])

        # draw color circles
        color_counter = -1
        for j in range(0, 300, 50):
            color_counter += 1
            board_circle = Circle(Point(j+25, 25+(50*y)), 25)
            board_circle.draw(win)
            board_circle.setFill(circles_colors[color_counter])
        
        # draw results circles
        blk_wht_counter = -1
        for j in range(300, 450, 25):
            blk_wht_counter += 1
            results_circle = Circle(Point(j+12, 12+(50*y)), 12)
            results_circle.draw(win)
            results_circle.setFill(blk_wht_circle_hidden[blk_wht_counter])
    
    # When the game ends
    if turns == 11:
        player_guess_enter.setText("Out of turns! Again? (yes, no)")
        pause = win.getMouse()
        play_again = player_guess_enter.getText()
        if play_again == "yes":
            win.close()
            main()
        elif play_again == "no":
            print("Thanks for playing!")
            win.close()
        else:
            print("Sorry, I didn't understand that entry. Please run this program \n"
                  "again to play again! Bye!")
            win.close()
        
    elif win_condition == secret_code:
        
        print(
              "############################################################# \n"
              "############################################################# \n" 
              "####                                                   ###### \n" 
              "####   YOU ARE THE MASTERMIND!!!!  CONGRADULATIONS!!!  ###### \n"
              "####                                                   ###### \n"
              "############################################################# \n" 
              "############################################################# \n"
              "\n"
              "Your guess was:", player_guess_raw_list, "and the correct awnser was", secret_code)

        # Would you like to play again?
        player_guess_enter.setText("YOU WON!! Again? (yes, no)")
        pause = win.getMouse()
        play_again = player_guess_enter.getText()
        if play_again == "yes":
            win.close()
            main()
        elif play_again == "no":
            print("Thanks for playing!")
            win.close()
        else:
            print("Sorry, I didn't understand that entry. Please run this program \n"
                  "again to play again! Bye!")
            win.close()
    else:
        print("Something has gone horribly wrong! AHHHHHH!!!!!")
        
def main():
    
    # User input which game they want to play (for game selction later)
    game_choice = "Mastermind"

    if game_choice == "Mastermind":

        # Draw the board for a game via what the player input
        game_board = board_draw(game_choice)

        # Generate the win condition
        secret_code = game_rules(game_choice)

        # Play the game
        mastermind(game_board, secret_code)

    elif game_choice == "Exit":
        print("Thanks for playing!")

    else:
        print("Sorry, wrong entry. Please try again.")
        main()

main()


