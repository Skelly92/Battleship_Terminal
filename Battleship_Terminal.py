class Battleship():
    def name(self):
        self = input("What is your name? ")
        return self
    
    def grid(self):
        print("""
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
        
        
    def ship_placement(self):
      
      one_list = {"A1": "B","B1": None,"C1":None,"D1":None,"E1":None,"F1": None,"G1":None,"H1":None,"I1":None,"J1":None}
      two_list = {"A2": None,"B2": None,"C2":None,"D2":None,"E2":None,"F2": None,"G2":None,"H2":None,"I2":None,"J2":None}
      three_list = {"A3": None,"B3": None,"C3":None,"D3":None,"E3":None,"F3": None,"G3":None,"H3":None,"I3":None,"J3":None}
      four_list = {"A4": None,"B4": None,"C4":None,"D4":None,"E4":None,"F4": None,"G4":None,"H4":None,"I4":None,"J4":None}
      five_list = {"A5": None,"B5": None,"C5":None,"D5":None,"E5":None,"F5": None,"G5":None,"H5":None,"I5":None,"J5":None}
      six_list = {"A6": None,"B6": None,"C6":None,"D6":None,"E6":None,"F6": None,"G6":None,"H6":None,"I6":None,"J6":None}
      seven_list = {"A7": None,"B7": None,"C7":None,"D7":None,"E7":None,"F7": None,"G7":None,"H7":None,"I7":None,"J7":None}
      eight_list = {"A8": None,"B8": None,"C8":None,"D8":None,"E8":None,"F8": None,"G8":None,"H8":None,"I8":None,"J8":None}
      nine_list = {"A9": None,"B9": None,"C9":None,"D9":None,"E9":None,"F9": None,"G9":None,"H9":None,"I9":None,"J9":None}
      ten_list = {"A10": None,"B10": None,"C10":None,"D10":None,"E10":None,"F10": None,"G10":None,"H10":None,"I10":None,"J10":None}
      battleship_grid = {**one_list, **two_list, **three_list, **four_list, **five_list, **six_list, **seven_list, **eight_list, **nine_list, **ten_list}

      carrier_ship_one = "A1" #input("Please type in the grid number where you would like to place the Carrier ship: ")
      carrier_ship_two = input("Please type in the grid number where you would like to place the Carrier ship: ")
      carrier_ship_three = input("Please type in the grid number where you would like to place the Carrier ship: ")
      carrier_ship_four = input("Please type in the grid number where you would like to place the Carrier ship: ")
      carrier_ship_five = input("Please type in the grid number where you would like to place the Carrier ship: ")
      battleship_carrier = {}

      battleship_one = input("Please type in the grid number where you would like to place the Battleship: ")
      battleship_two = input("Please type in the grid number where you would like to place the Battleship: ")
      battleship_three = input("Please type in the grid number where you would like to place the Battleship: ")
      battleship_four = input("Please type in the grid number where you would like to place the Battleship: ")
      battleship_BS = {}

      cruiser_one = input("Please type in the grid number where you would like to place the Cruiser ship: ")
      cruiser_two = input("Please type in the grid number where you would like to place the Cruiser ship: ")
      cruiser_three = input("Please type in the grid number where you would like to place the Cruiser ship: ")
      battleship_cruiser = {}

      submarine_one = input("Please type in the grid number where you would like to place the Submarine: ")
      submarine_two = input("Please type in the grid number where you would like to place the Submarine: ")
      submarine_three = input("Please type in the grid number where you would like to place the Submarine: ")
      battleship_submarine = {}

      destroyer_one = input("Please type in the grid number where you would like to place the Destroyer: ")
      destroyer_two = input("Please type in the grid number where you would like to place the Destroyer: ")
      battleship_destroyer = {}
      
      for key in battleship_grid.keys():
        if key == carrier_ship_one:
            battleship_grid[key] = "C"
            battleship_carrier = {key:"C"}
        if key == carrier_ship_two:
          battleship_grid[key] = "C"
          battleship_carrier = {key:"C"}
        if key == carrier_ship_three:
          battleship_grid[key] = "C"
          battleship_carrier = {key:"C"}
        if key == carrier_ship_four:
          battleship_grid[key] = "C"
          battleship_carrier = {key:"C"}
        if key == carrier_ship_five:
          battleship_grid[key] = "C"
          battleship_carrier = {key:"C"}
        if key == battleship_one:
          battleship_grid[key] = "B"
          battleship_BS = {key:"B"}
        if key == battleship_two:
          battleship_grid[key] = "B"
          battleship_BS = {key:"B"}
        if key == battleship_three:
          battleship_grid[key] = "B"
          battleship_BS = {key:"B"}
        if key == battleship_four:
          battleship_grid[key] = "B"
          battleship_BS = {key:"B"}
        if key == cruiser_one:
          battleship_grid[key] = "Cr"
          battleship_cruiser = {key:"Cr"}
        if key == cruiser_two:
          battleship_grid[key] = "Cr"
          battleship_cruiser = {key:"Cr"}
        if key == cruiser_three:
          battleship_grid[key] = "Cr"
          battleship_cruiser = {key:"Cr"}
        if key == submarine_one:
          battleship_grid[key] = "S"
          battleship_submarine = {key:"S"}
        if key == submarine_two:
          battleship_grid[key] = "S"
          battleship_submarine = {key:"S"}
        if key == submarine_three:
          battleship_grid[key] = "S"
          battleship_submarine = {key:"S"}
        if key == destroyer_one:
          battleship_grid[key] = "D"
          battleship_destroyer = {key:"D"}
        if key == destroyer_two:
          battleship_grid[key] = "D"
          battleship_destroyer = {key:"D"}
      
      print (battleship_carrier)
      return battleship_grid

     
    def battleship_attack(self):
      grid = Battleship.ship_placement(self)
      while True:
        attack = input("Please enter the coordinates for where you wish to attack: ")
        for key in grid.keys(): 
          for value in grid.values():
            if key == attack and value == "B":
              grid[key] = "X"
              print("Boom")
              break
            elif key == attack and value == None:
              grid[key] = "O"
              print("Splosh")
              break
            elif attack == "End":
              return False


            
x = Battleship()
x.grid()
x.battleship_attack()
