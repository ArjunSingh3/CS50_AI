import sys

from crossword import *
from collections import deque

class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """

        # Need to know all the lengths/unary constraints of all the variables to filter out the domains
        # For Testing:

        for variables, domain_set in self.domains.items():
            length_filter = variables.length
            domain_set_copy = domain_set.copy()
            for value in domain_set_copy:
                if len(value) != length_filter:
                    domain_set.remove(value)
        
        # raise NotImplementedError

    def constraint_checker(x,y,overlap_information):

        i,j = overlap_information

        if x[i] != y[j]:
            print("False")
            return False
        else:
            print("True")
            return True
        # raise NotImplementedError

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False
        a,b = self.crossword.overlaps[x,y]
        print("a: ",a,", b: ",b)
        overlap_information = (a,b)
        for little_x in self.domains[x]: 
            if not any(self.constraint_checker(little_x,little_y,overlap_information) for little_y in self.domains[y]):
                self.domains[x].remove(little_x)
                revised = True
        return True
        # raise NotImplementedError

    def generate_arcs(self):
        list_of_arcs = []
        for variable in self.crossword.variables:
            print("variable",variable)
            for neighbor in self.crossword.neighbors(variable):
                print("neighbor: ",neighbor)

                if self.crossword.overlaps[variable,neighbor] is not None:
                    list_of_arcs.append((variable,neighbor))
        
        return list_of_arcs
                   


    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # !!!!!!!!!!! PROBLEMMMMM !!!!!!!
        
        if arcs is None:
            # Make a generate arcs function
            queue_arcs = deque(self.generate_arcs())
            print(" FALSE IN AC3 ")
            print(queue_arcs)
        else:
            queue_arcs = deque(arcs)

        
        while not queue_arcs:
            print("Hello, World!")
            (x,y) = queue_arcs.popleft() 
            if self.revise(arcs,x,y):
                print("Hello, World")
                if len(self.domains[x]) == 0:
                    return False
                for z in self.crossword.neighbors(x)-{y}:
                    queue_arcs.append((z,x))
        return True
        # raise NotImplementedError

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        for variable, values in assignment.items():
            if values is None:
                return False
        return True

        # Will be Removed for Testing ONLY! Be Careful
        # raise NotImplementedError

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # Objectives: 
        # All values must be distinct : Make a set and if the length of the set is different than the length of the list of values in the assignment dict then one or more values is not distinct and return false
        # Every value should be the correct length : Not sure exactly where We will get the correct length from, but comparing lengths shouldn't be too bad
        # There should not be any conflicts between neighboring variables : Thinking....

        # Solution:
        distinct_set = set((assignment.values()))
        if len(distinct_set) != len(assignment.values()):
            return False

        for variable, value in assignment.items():

            if len(variable) != len(value):
                return False
            neigbor_words_set = self.crossword.neighbors(variable)
            if not any(self.overlap_DoWe(self.crossword.overlaps[variable,neighbor],value,assignment[neighbor])for neighbor in neigbor_words_set):
                return False
        return True
        # raise NotImplementedError
    def overlap_DoWe(self,cell,value1,value2):
        i,j = cell

        if value1[i] != value2[j]:
            return False
        else:
            return True

    
    def count_word_out(self,overlap_information, assignment,value, variable):
        i,j = overlap_information
        count = 0
        for value_list in self.domains[variable]:
            if value[i] != value_list[j]:
                count += 1
            # print("Hello, World!")
        
        return count

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # NOw we know all the neghboring variables
        lease_constraint_values_list = []
        for value in self.domains[var]:
            n = 0
            for variable in self.crossword.neighbors(var):
                a,b = self.crossword.overlaps[var,variable]
                overlap_information = (a,b)
                n += self.count_words_out(overlap_information,assignment,value, variable)
            lease_constraint_values_list.append(n)
            print("Hello, World!")
        
        lease_constraint_values_list.sort()
    
        return lease_constraint_values_list
        # raise NotImplementedError

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """

        for variable in self.domains(assignment):
            if variable not in assignment:
                return variable
        # raise NotImplementedError

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """

        # Check if assignment is complete:
        if self.assignment_complete(assignment):
            return assignment
        # Try a new variable:
        var = self.select_unassigned_variable(assignment)
        # For loop to go voer all values in DOMAIN-VALUES
        for value in self.order_domain_values(var,assignment):
            new_assignment = assignment.copy()
            new_assignment[var] = value
            if self.consistent(new_assignment):
                result = self.backtrack(new_assignment)
                if result is not None:
                    return result
        return None
        # raise NotImplementedError


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    print(assignment)

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
