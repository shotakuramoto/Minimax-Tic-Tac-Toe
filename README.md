# Minimax-Tic-Tac-Toe
Created a tic tac toe game based in python. It will estimate the best possible route to win the game given the input. It uses Minimax algorithm to search the route to win the game. Moreover, it focuses on alpha beta pruning and early termination that makes the program more efficient and faster. 

This game has three versions of tic tac toe.
1. A game with minimax algorithm
2. A game with minimax and alphabeta pruning
3. A game with minimax, alphabeta pruning, and early termination.

This game will find the best possible place to put either o or x. Terminal output will show where to put o or x in given situation.
For example, given input oxxxo-ox-, the terminal output will be oxxxo-oxo

Moreover, this minimax function will record all the visited in text file.
With the same example, the text file will contain
oxxxooox- 0
oxxxoooxx 0
oxxxo-oxo -1

As you can see in this example text file output, 0, 1, -1 are the possible utlity values.
The Minimax algorithm will run based on this three possible values.

There ccan be upto four terminal input for this code.
1. string input. Input should be the state of the board in string.
2. string input. Path to let all the visited states to be stored.
3. string input. Third input can only be "prune". When there is "prune", alphabeta pruning or early temrination method will be used.
4. integer input. This integer determines the depth of the decision tree for early termination.
