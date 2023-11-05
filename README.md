# Welcome to the SBX Chess Engine remote repository!

### This is a personal project by Matthew Curry as an exercise in object-oriented programming, efficient algorithmic design, and feature extraction to update a reinforcement learning model.

### SBX is an ongoing project that will use a mixture of standard tree search algorithms and RL feedback to play chess learned on games played by professional players.

## Current status:

### Board and Piece Representation :white_check_mark:
#### The board state is an 8x8 matrix where each piece is represented by a hexadecimal number class in *bitmap.txt*, which encodes white pieces &#8773; 0 (mod 2) and black pieces &#8773; 1 (mod 2). This was done to allow quick comparisons between pieces on the board without the use of explicit piece classes.

