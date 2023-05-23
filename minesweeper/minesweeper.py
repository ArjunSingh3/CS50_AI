import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"
    
    def get_count(self):
        return self.count

    def get_set(self):
        return self.cells

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        known_mines_list = set()
        if self.count == list(self.cells):
            return self.cells
        else:
            return known_mines_list.clear()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        known_safe_list = set()
        if self.count == 0:
            return self.cells
        else:
            return known_safe_list.clear()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # raise NotImplementedError
        if cell in self.cells:
            self.cells.discard(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # raise NotImplementedError
        if cell in self.cells:
            self.cells.discard(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # raise NotImplementedError
        # Mark the Cell as a move that has been made
        self.moves_made.add(cell)
        # Mark the Cell as a safe cell
        self.mark_safe(cell)
        # Add a new sentence to the AI's knowledge base based on the value of 'cell' and 'count'
        set_of_cells = set()
        i,j = cell
        for row in range(3):
            for column in range(3):
                neighbor_cell = (row+i-1,column+j-1)
                """
                Double check the if statement as I might be checking more things than I need to
                """
                if neighbor_cell not in self.moves_made and neighbor_cell not in self.safes and neighbor_cell not in self.mines:
                    set_of_cells.add(neighbor_cell)
        new_Sentence = Sentence(set_of_cells,count)
        
        # Add any new sentences to the AI's knowledge base if they can be infered fom any existing knowledge
        """
        THis will be done by manupilating sets in the nowledge base and being able 
        to create new sets based on the existing knowledge
        """
        # Double Check The getter methods for getting the count and the set of a sentence
        for sentence in self.knowledge:

            inferred_sentence_count = abs(sentence.get_Count() - count)
            inferred_sentence_set = (sentence.get_Set()- set_of_cells)

            inferred_setence = Sentence(inferred_sentence_set,inferred_sentence_count)

            if inferred_setence not in self.knowledge:
                self.add_knowledge(inferred_setence)
            else:
                continue

        # Mark any additional cells as safe or as mines if it can be concluded based on the AI's knowledge base
        for sentence in self.knowledge:
            if(sentence.get_Count == len[sentence.get_Set()]):
                for cell in sentence.get_Set():
                    sentence.mark_mine(cell)
            elif sentence.get_Count is 0:
                for cell in sentence.get_Set():
                    sentence.mark_safe(cell)


    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # raise NotImplementedError
        if len(self.safes) == 0:
            return None
        else:
            for move in self.safes:
                if move not in self.moves_made:
                    return move
            return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        # raise NotImplementedError
        random_moves = set()
        for i in range(self.height):
            for j in range(self.width):
                move = (i,j)
                if move not in self.mines and move not in self.moves_made:
                    random_moves.add(move)

        if len(random_moves) == 0:
            return None
        else:
            return random.choice(random_moves)