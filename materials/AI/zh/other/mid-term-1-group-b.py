from mt_utils import *
from pprint import pprint


class WordGame(Problem):

    def __init__(self):
        # This will read the file containing all valid 5 letter english words and save all of them as lists
        # You can refer to it as self.W in any function inside this class
        with open('five-letter-words.txt', 'r') as word_file:
            self.W = [list(line.rstrip().upper()) for line in word_file]
        # You can check the contents of self.W by uncommenting this line and making an object of WordGame type in main
        # pprint(self.W)
        # You will find all letters of the alphabet in the self.alphabet variable
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        # Complete the implementation of initial function by calling
        # the parent constructor and initialize with the initial state and the goal state
        # Write your code below this line!

        # Write your code above this line!

    def actions(self, state):
        # Complete the implementation of possible operators.
        # The function should return all next possible actions from the input state.
        # Hint: 'if 5 in list:' will return True if 5 is in the list and False if it is not
        acts = []
        original_state = list(state)
        # Write your code below this line!

        # Write your code above this line!
        return acts

    def result(self, state, action):
        # Fill in the missing parts of the transition function
        i, l = action

        # Write your code below this line!

        # Write your code above this line!

    def goal_test(self, state):
        # Write a logic here to test if the state is a goal state. Return True if it is a goal state, False if not
        # Write your code below this line!
        pass
        # Write your code above this line! Delete the 'pass' keyword.


def breadth_first_graph_search(problem):
    # Write your code below this line!
    pass
    # Write your code above this line! Delete the 'pass' keyword.


def main():
    # 1. Exercise: Fill in the missing parts of init function and print out the initial state result (1 point)
    # Write your code below this line!
    pass
    # Write your code above this line! Delete the 'pass' keyword.

    # 2. Exercise: Fill out the goal_test function and test if it works correctly (1 point)
    # Write your code below this line!

    # Write your code above this line!

    # 3. Exercise: Fill out the actions function and test if it works correctly (3 points)
    # (test using the initial state)
    # expected output: [(1, 'D'), (1, 'H'), (1, 'L'), (1, 'R'), (1, 'S'), (1, 'Y'), (3, 'O'), (5, 'Y')]
    # Write your code below this line!

    # Write your code above this line!
    # 4. Exercise: Fill out the result function and test if it works correctly (2 points)
    # (use the initial state and (5, 'Y') as the action when testing)
    # Write your code below this line!

    # Write your code above this line!
    # 5. Fill out the breadth_first_graph_search function and solve the problem using it (2 points)
    # (this will take around 5-10 sec to calculate)
    # Write your code below this line!

    # Write your code above this line!


if __name__ == '__main__':
    main()
