class Player:
    def __init__(self):
        self.name = ""
        self.sympol = ""

    def Choose_name(self):
        while True:
            name = input("Enter your name (only letters)")
            if name.isalpha() == True:
                self.name = name
                break
            else:
                print("invalid name, please use letters only ")
        return self.name
    
    def Choose_sympol(self):
        while True:
            sympol = input(f"{self.name} , choose your sympol is a single letter ")
            if sympol.isalpha() and len(sympol) == 1:
                self.sympol = sympol
                break
            else:
                print("invalid sympol, please choose a single letter ")
        return self.sympol

class Menu:
    def desplay_main_menu (self):
        print("Welcome to my X-O game \n 1.Start Game \n 2.Quit Game")
        choice = input("enter your choice (1 , 2)")
        while choice !=1 or choice !=2:
            print("invalid choice please enter (1 or 2) only")
            choice = input("enter your choice (1 , 2)")
        return choice
    
    def End_Game_Menu (self):
        print("Game over! \n 1.Restart Game \n 2.Quit Game")
        choice = input("enter your choice (1 , 2)")
        while choice !=1 or choice !=2:
            print("invalid choice please enter (1 or 2) only")
            choice = input("enter your choice (1 , 2)")
        return choice
        
class Board:
    # @classmethod
    # def board(cls):
    #     print(" 1 | 2 | 3")
    #     print("-"*15)
    #     print(" 4 | 5 | 6")
    #     print("-"*15)
    #     print(" 7 | 8 | 9 ") 
        
    def __init__(self): 
        self.board = ["1","2","3","4","5","6","7","8","9"]

    def display_board(self):
        for x in range(0,10,3):
            print("|".join(self.board[x:x+3]))
            if x<6:
                print("-"*5) 

    def invalid_move(self, choice):
       return self.board[choice-1].isdigit()
    
    def update_board(self, choice, sympol):
        if Board.invalid_move(choice):
            self.board[choice-1] = sympol
            return True
        else:
            False

class game:
    def __init__(self):
        self.player = [Player(), Player()]
        self.menu = Menu()
        self.board = Board()
    
    def Start_Game(self):
        start = self.menu.desplay_main_menu()
        if start == 1:
            self.setup_players()
            self.play_game()


        else:
            self.Quit_game()
        
    
    def Quit_Game(self):
        print(" thanks, good bye ")
    
    def setup_players(self, name, sympol):
        for i in self.player:
            print(f"player {self.player.index(i+1)} Enter your details")
            Player.Choose_name()
            Player.Choose_sympol()
            print("-"*10)
        
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                end_game = self.menu.End_Game_Menu()
                if end_game == 1:
                    self.board

                else:
                    game.Quit_Game()
                    break
