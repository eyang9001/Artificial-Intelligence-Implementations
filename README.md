# MSAI Projects and Assignments
This is a compilation of the projects and implementations of models I have developed as a part of the MSAI program

## 1. Knowledge Base
A knowledge base is created to hold facts and rules. When new facts or rules are added to the knowledge base with `student_code.kb_add`, forward chaining is applied to infer new facts and rules. The knowledge base also handles retracting of facts and rules with `student_code.kb_retract`. Truth maintenance is employed to keep the knowledge base up to date, and make sure all inferred facts and rules are grounded. The knowledge base can also be queried with `student_code.kb_ask` to see if facts or rules exist in the knowledge base.

## 2. A* Search
This is an implementation of A* search for pathing. The example used for this code is to find the fastest path around Northwestern's campus given travel times and direct distance measurements as the heuristic. `student_code.a_star_search` can be called, providing the start and end locations to return the optimal path.

## 3. Minimax and Alpha Beta Pruning
This is an implementation of Minimax adversarial search to play the game: **Konane**. The program is built with varying levels of AI to play against. There is one version that only uses the minimax algorithm to choose the optimal move, and another version that builds upon the minimax algorithm and epmloys alpha-beta pruning to increase efficiency. The game to can be played by running 
```bash
python main.py $P1 $P2
```

## 4. PDDL Planning
Included are domain and problem files to be used with the online .pddl editor [here](http://editor.planning.domains/#) to simulate robot pathing within Amazon warehouses. The PDDL domain includes `actions {}` with necessary precondition and effects that can be carried out to fulfill the goal in the chosen problem file.

## 5. Bayes Net
This is an implementation of the infamous Earthquake or Burglary Baysian Network. Given the joint probabilities for each individual event, the chain rule is propagated through the network to calculate conditional probabilities `P(A|B)`.

## 6. Naïve Bayes Classifier
This is a NBC implementation used to classify movie reviews as positive or negative. The implementation uses add-one smoothing, removal of stop words, removal of numerical and symbol characters, and removal of capitalization. 

My model reaches 0.934 and 0.755 f-scores for positive and negative classes, respectively after 10-fold cross-validation on the data set.
