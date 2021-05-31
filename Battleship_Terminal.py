import random
class Battleship():
    def name(self):
        self = input("What is your name? ")
        return self
    
    def grid(self):
        print("""


        
        ██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗░██████╗██╗░░██╗██╗██████╗░
        ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝██╔════╝██║░░██║██║██╔══██╗ 
        ██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░╚█████╗░███████║██║██████╔╝
        ██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░░╚═══██╗██╔══██║██║██╔═══╝░
        ██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗██████╔╝██║░░██║██║██║░░░░░
        ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░
        ----------------------------------------------------------------------------
        Welcome to the battleship terminal game!
        ----------------------------------------------------------------------------

        The rules for battleship are the following:

        -You select where you are going to attack based on the 10x10 grid

        -There are 5 battleships and there sizes are the following:

        |Class of ship | Size |
        |Carrier       |  5   |
        |Battleship    |  4   |
        |Cruiser       |  3   |
        |Submarine     |  3   |
        |Destroyer     |  2   |

        -Once you have successfully destroyed all of them, you have won and the game will end.


          |A  |B  |C  |D  |E  |F  |G  |H  |I  |J  |
        1 |A1 |B1 |C1 |D1 |E1 |F1 |G1 |H1 |I1 |J1 |
        2 |A2 |B2 |C2 |D2 |E2 |F2 |G2 |H2 |I2 |J2 |
        3 |A3 |B3 |C3 |D3 |E3 |F3 |G3 |H3 |I3 |J3 |
        4 |A4 |B4 |C4 |D4 |E4 |F4 |G4 |H4 |I4 |J4 |
        5 |A5 |B5 |C5 |D5 |E5 |F5 |G5 |H5 |I5 |J5 |
        6 |A6 |B6 |C6 |D6 |E6 |F6 |G6 |H6 |I6 |J6 |
        7 |A7 |B7 |C7 |D7 |E7 |F7 |G7 |H7 |I7 |J7 |
        8 |A8 |B8 |C8 |D8 |E8 |F8 |G8 |H8 |I8 |J8 |
        9 |A9 |B9 |C9 |D9 |E9 |F9 |G9 |H9 |I9 |J9 |
        10|A10|B10|C10|D10|E10|F10|G10|H10|I10|J10|
        """)
        one_list = {"A1": "A" ,"B1": "A","C1":"A","D1":"A","E1":"A","F1": "A","G1":"A","H1":"A","I1":"A","J1":"A"}
        two_list = {"A2": "A","B2": "A","C2":"A","D2":"A","E2":"A","F2": "A","G2":"A","H2":"A","I2":"A","J2":"A"}
        three_list = {"A3": "A","B3": "A","C3":"A","D3":"A","E3":"A","F3": "A","G3":"A","H3":"A","I3":"A","J3":"A"}
        four_list = {"A4": "A","B4": "A","C4":"A","D4":"A","E4":"A","F4": "A","G4":"A","H4":"A","I4":"A","J4":"A"}
        five_list = {"A5": "A","B5": "A","C5":"A","D5":"A","E5":"A","F5": "A","G5":"A","H5":"A","I5":"A","J5":"A"}
        six_list = {"A6": "A","B6": "A","C6":"A","D6":"A","E6":"A","F6": "A","G6":"A","H6":"A","I6":"A","J6":"A"}
        seven_list = {"A7": "A","B7": "A","C7":"A","D7":"A","E7":"A","F7": "A","G7":"A","H7":"A","I7":"A","J7":"A"}
        eight_list = {"A8": "A","B8": "A","C8":"A","D8":"A","E8":"A","F8": "A","G8":"A","H8":"A","I8":"A","J8":"A"}
        nine_list = {"A9": "A","B9": "A","C9":"A","D9":"A","E9":"A","F9": "A","G9":"A","H9":"A","I9":"A","J9":"A"}
        ten_list = {"A10": "A","B10": "A","C10":"A","D10":"A","E10":"A","F10": "A","G10":"A","H10":"A","I10":"A","J10":"A"}
        battleship_grid = {**one_list, **two_list, **three_list, **four_list, **five_list, **six_list, **seven_list, **eight_list, **nine_list, **ten_list}
        return battleship_grid
    
    def ship_placement(self):
      grid = Battleship.grid(self)
      
      carrier_ship_one = "A1" #random.choices(a) #input("Please type in the grid number where you would like to place the Carrier ship: ")
      carrier_ship_two = "A2" #input("Please type in the grid number where you would like to place the Carrier ship: ")
      carrier_ship_three = "A3" #input("Please type in the grid number where you would like to place the Carrier ship: ")
      carrier_ship_four = "A4" #input("Please type in the grid number where you would like to place the Carrier ship: ")
      carrier_ship_five = "A5" #input("Please type in the grid number where you would like to place the Carrier ship: ")
      battleship_carrier = {}

      battleship_one = "B1" #input("Please type in the grid number where you would like to place the Battleship: ")
      battleship_two = "B2" #input("Please type in the grid number where you would like to place the Battleship: ")
      battleship_three = "B3" #input("Please type in the grid number where you would like to place the Battleship: ")
      battleship_four = "B4" #input("Please type in the grid number where you would like to place the Battleship: ")
      battleship_BS = {}

      cruiser_one = "C1" #input("Please type in the grid number where you would like to place the Cruiser ship: ")
      cruiser_two = "C2" #input("Please type in the grid number where you would like to place the Cruiser ship: ")
      cruiser_three = "C3" #input("Please type in the grid number where you would like to place the Cruiser ship: ")
      battleship_cruiser = {}

      submarine_one = "D1" #input("Please type in the grid number where you would like to place the Submarine: ")
      submarine_two = "D2" #input("Please type in the grid number where you would like to place the Submarine: ")
      submarine_three = "D3" #input("Please type in the grid number where you would like to place the Submarine: ")
      battleship_submarine = {}

      destroyer_one = "E1" #input("Please type in the grid number where you would like to place the Destroyer: ")
      destroyer_two = "E2" #input("Please type in the grid number where you would like to place the Destroyer: ")
      battleship_destroyer = {}
      
      for key in grid.keys():
        if key == carrier_ship_one:
          grid.update({key:"C"})
          battleship_carrier[key] = "C"
        if key == carrier_ship_two:
          grid.update({key:"C"})
          battleship_carrier[key] = "C"
        if key == carrier_ship_three:
          grid.update({key:"C"})
          battleship_carrier[key] = "C"
        if key == carrier_ship_four:
          grid.update({key:"C"})
          battleship_carrier[key] = "C"
        if key == carrier_ship_five:
          grid.update({key:"C"})
          battleship_carrier[key] = "C"
        if key == battleship_one:
          grid.update({key:"B"})
          battleship_BS[key] = "B"
        if key == battleship_two:
          grid.update({key:"B"})
          battleship_BS[key] = "B"
        if key == battleship_three:
          grid.update({key:"B"})
          battleship_BS[key] = "B"
        if key == battleship_four:
          grid.update({key:"B"})
          battleship_BS[key] = "B"
        if key == cruiser_one:
          grid.update({key:"CR"})
          battleship_cruiser[key] = "CR"
        if key == cruiser_two:
          grid.update({key:"CR"})
          battleship_cruiser[key] = "CR"
        if key == cruiser_three:
          grid.update({key:"CR"})
          battleship_cruiser[key] = "CR"
        if key == submarine_one:
          grid.update({key:"S"})
          battleship_submarine[key] = "S"
        if key == submarine_two:
          grid.update({key:"S"})
          battleship_submarine[key] = "S"
        if key == submarine_three:
          grid.update({key:"S"})
          battleship_submarine[key] = "S"
        if key == destroyer_one:
          grid.update({key:"D"})
          battleship_destroyer[key] = "D"
        if key == destroyer_two:
          grid.update({key:"D"})
          battleship_destroyer[key] = "D"

      return battleship_carrier, battleship_BS, battleship_cruiser, battleship_submarine, battleship_destroyer, grid
      

     
    def battleship_attack(self):
      battleship_carrier, battleship_BS, battleship_cruiser, battleship_submarine, battleship_destroyer, grid  = Battleship.ship_placement(self)
      
      while True:
        attack = input("Please enter the coordinates for where you wish to attack: ")
        for key in grid.keys(): 
          if key == attack and grid[key] == "C":
            grid[key] = "X"
            battleship_carrier.pop(key)
            print("Boom")
            if battleship_carrier == {}:
              print("You have sunk the carrier ship!")
            if battleship_carrier == {} and battleship_BS == {} and battleship_cruiser == {} and battleship_submarine == {} and battleship_destroyer == {}:
              print("You have sunk all of the Battleships! You have won the game!!!")
              return False
            break
          elif key == attack and grid[key] == "B":
            grid[key] = "X"
            battleship_BS.pop(key)
            print("Boom")
            if battleship_BS == {}:
              print("You have sunk the Battleship!")
            if battleship_carrier == {} and battleship_BS == {} and battleship_cruiser == {} and battleship_submarine == {} and battleship_destroyer == {}:
              print("You have sunk all of the Battleships! You have won the game!!!")
              return False
            break
          elif key == attack and grid[key] == "CR":
            grid[key] = "X"
            battleship_cruiser.pop(key)
            print("Boom")
            if battleship_cruiser == {}:
              print("You have sunk the Cruiser Ship!")
            if battleship_carrier == {} and battleship_BS == {} and battleship_cruiser == {} and battleship_submarine == {} and battleship_destroyer == {}:
              print("You have sunk all of the Battleships! You have won the game!!!")
              return False
            break
          elif key == attack and grid[key] == "S":
            grid[key] = "X"
            battleship_submarine.pop(key)
            print("Boom")
            if battleship_submarine == {}:
              print("You have sunk the Submarine!")
            if battleship_carrier == {} and battleship_BS == {} and battleship_cruiser == {} and battleship_submarine == {} and battleship_destroyer == {}:
              print("You have sunk all of the Battleships! You have won the game!!!")
              return False
            break
          elif key == attack and grid[key] == "D":
            grid[key] = "X"
            battleship_destroyer.pop(key)
            print("Boom")
            if battleship_destroyer == {}:
              print("You have sunk the Destroyer!")
            if battleship_carrier == {} and battleship_BS == {} and battleship_cruiser == {} and battleship_submarine == {} and battleship_destroyer == {}:
              print("You have sunk all of the Battleships! You have won the game!!!")
              return False
            break
          elif key == attack and grid[key] == "A":
            grid[key] = "O"
            print("Splosh")
            break
          elif attack == "End":
            return False
       
           
battleship = Battleship()
battleship.battleship_attack()
