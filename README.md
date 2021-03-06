# Modern Art ## V1.1
 Personal project based on the Modern-Art question in IMCxCSESoc 2022 competition 


# The problem
 To solve the problem of creating the highest mask for a given map of values. 
 Each grid of values needs to be able to generate the largest selection of values in which all values are interconnected. 
 Each grid will be a 2d grid consisting of different weights.

# Goals
 The goals of this challenge is the explore specific algorithms related to heat mapping and selection of values in a efficient manner. 
 It will also be a learning project to explore the use of full stack programming, including the use of API, frontend and backend implementations.

# Usage
```
python3 main.py {Map Name} {Algorithm Name} {Output Style}
```

# Current technologies planned
- [ ] Backend - Python
- [ ] Frontend - Undecided 
- [ ] API - Undecided
- [ ] Other

# Future Plans
 Solving this challenging problem by itself will be a challenge by itself, especially making it efficient. 
 However in the future it would be amazing for the program as a whole to have feature including

- 3D graphs
- Animated states
- Weight output
- Multi dimensionality graphs 
- Optimizer for input system and solving runner

## Algorithm planed

- [X] Brute force 1.0 - combinatorics
  - Contains: 
    - Basic map checker 

- [X] Brute force 2.0 - combinatorics, mem efficient 
  - Contains: 
    - Basic map checker 
    - Generates only one comb case per loop
    - Basic time based auto stop (3 mins)

- [ ] Brute force - Combinatorics, max value based
  - Contains

- [X] Randomized Combinatorics - Combinatorics random based
  - Contains
    - Basic map checker 
    - Generates only one comb case per loop
    - Randomized combinatorics generator
    - Error output, 10000 combinatorics max

- [X] Max based Local Search - local search algorithm
  - Contains
    - PQ system based
    - Start on a max value 
    - Complete, Not optimal

- [X] Max based Local Search 2.0 - local search algorithm
  - Contains
    - PQ system based
    - Start on a max value 
    - Complete, Not optimal
    - Runs multiple times for every max start node 
  
- [ ] Bidirectional - max value based 

# Sample Outputs 

Inputted 5x5 grid with 10 select values will be 

```
5 5 10
03522
09468
52978
04416
23807
```

Result (Select values Sum = 70 and all select are interconnect)
```
.....
.##.#
..###
..#.#
..#.#
```

## Methodology
A brute force method may be used for these simplistic graphs, More complicated graphs like 100x100 will require radically more efficient algorithms.