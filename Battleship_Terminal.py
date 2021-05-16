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

        one_num = [1]
        two_num = [2]
        three_num = [3]
        four_num = [4]
        five_num = [5]
        six_num = [6]
        seven_num = [7]
        eight_num = [8]
        nine_num = [9]
        ten_num = [10]

        while len(two_num) < 10:
          one_num.append (one_num[0])
          two_num.append (two_num[0])
          three_num.append (three_num[0])
          four_num.append (four_num[0])
          five_num.append (five_num[0])
          six_num.append (six_num[0])
          seven_num.append (seven_num[0])
          eight_num.append (eight_num[0])
          nine_num.append (nine_num[0])
          ten_num.append (ten_num[0])
        
        one_list = dict(zip(["a","b","c","d","e","f","g","h","i","j"],one_num))
        two_list = dict(zip(["a","b","c","d","e","f","g","h","i","j"],two_num))
        three_list = dict(zip(["a","b","c","d","e","f","g","h","i","j"],three_num))
        four_list = dict(zip(["a","b","c","d","e","f","g","h","i","j"],four_num))
        five_list = dict(zip(["a","b","c","d","e","f","g","h","i","j"],five_num))
        six_list = dict(zip(["a","b","c","d","e","f","g","h","i","j"],six_num))
        seven_list = dict(zip(["a","b","c","d","e","f","g","h","i","j"],seven_num))
        eight_list = dict(zip(["a","b","c","d","e","f","g","h","i","j"],eight_num))
        nine_list = dict(zip(["a","b","c","d","e","f","g","h","i","j"],nine_num))
        ten_list = dict(zip(["a","b","c","d","e","f","g","h","i","j"],ten_num))

        #print (ten_list)
        #print(ten_num)
     
       
x = Battleship()
x.grid()