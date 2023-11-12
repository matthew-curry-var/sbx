# Welcome to the SBX Chess Engine remote repository!


#### This is a personal project by Matthew Curry as an exercise in object-oriented programming, efficient algorithmic design, and feature extraction to update a reinforcement learning model. SBX is an ongoing project that will use a mixture of standard tree search and RL feedback to play chess versus humans and other AIs, learned on games played by professional players. cd into **./sbx** and run **"python3 main.py"**

![Chess2](./chess-transparent/sbx1.png)

![Chess1](./chess-transparent/sbx2.png)


## Current status:

### Board and Piece Representation :white_check_mark:
#### The board state is an 8x8 matrix where each piece is represented by a hexadecimal number class in *bitmap.txt*, which encodes **white pieces &#8773; 0 (mod 2)** and **black pieces &#8773; 1 (mod 2)**. This was done to allow quick comparisons between pieces on the board without the use of explicit piece classes.

### Chess Rules and Logic :white_check_mark:
#### The Chess class in *Chess.py* is a wrapper for our board state which implements sequential turn based inputs for the legal moves of standard chess. Input is accepted as (x0, y0, x1, y1) and will only apply the move if it is a legal move for the piece @ (x0, y0). After a move is taken, determine if the chess board is in a state of check or checkmate and filter the legal moves based on those conditions.

### Opponent AI (Minimax/ab-pruning) :black_small_square: :black_small_square: :black_small_square:
#### Currently implementing this step of the engine where the opponent in **LenaAI.py** will apply depth-first search to a depth = 4 and apply Minimax decision algorithm to return the move that maximizes our utility function. Additionally, opponent will utilize alpha-beta pruning paradigm to improve computational efficiency in cases where the decision tree will not yield a higher utility at some depth (i.e. pruning).

### SBX GUI :x:
#### Future step will represent the board state and a playable version of the engine within a GUI using tkinter and other supporting libraries. User can play versus the opponent in **LenaAI.py** or versus another user in a 1v1 fashion. Additional options presented to allow user to highlight possible moves, draw arrows, and avoid blunders with the "movetip" option.

### Feature Extraction of Professional Games :x:
#### Future step will read algebraic strings of chess matches from professional players and evaluate pre-defined features on those matches to update a linear regression model. Learning will become relevant when our minimax approach yields any number of future states > 1 within some epsilon max_utility_score &#x00B1; &#x03B5;. Possible features include pawn structure, defense score, board domination zones, attack threat ability, true piece value.

### Test Phase :x:
#### Run SBX engine in head-to-head competition with suite of different chess engines (StockFish, Leela, Komodo) to evaluate engine performance. This phase will allow iterative improvements to efficiency and feature selection on our training set.

