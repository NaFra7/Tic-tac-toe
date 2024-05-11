class GameManager:
    def __init__(self):
        self.game_board = [
            ["1", "|", "2", "|", "3"],
            ["----------"],
            ["4", "|", "5", "|", "6"],
            ["----------"],
            ["7", "|", "8", "|", "9"]
        ]
        self.winning_combos = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"],
            ["1", "5", "9"],
            ["1", "4", "7"],
            ["2", "5", "8"],
            ["3", "6", "9"],
            ["3", "5", "7"],
        ]
        self.choice_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def show_board(self):
        """ Converts the game board from lists to a cleaner format """
        for row in range(len(self.game_board)):
            print(" ".join(self.game_board[row]))

    def update_board(self, choice, player):
        """Takes player entry and updates the game board,
        then prints the updated board to the console"""
        for board_row in self.game_board:
            for i in range(len(board_row)):
                if board_row[i] == choice:
                    board_row[i] = player["Symbol"]
                    self.show_board()

    def check_for_winner(self, player):
        """Checks the current player's list of moves against the winning combo list and if there is a match,
        declares the player the winner"""
        for combo in self.winning_combos:
            check_player = all(moves in player["Moves"] for moves in combo)
            if check_player:
                return True

