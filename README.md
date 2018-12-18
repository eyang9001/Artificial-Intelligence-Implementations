# MSAI Projects and Assignments
This is a compilation of the projects and implementations of models I have developed as a part of the MSAI program

## 1. Knowledge Base
###### This was an assignment in the class MSAI 348 'Intro to AI' taught by Professor Jason (Willie) Wilson 
This is my implementation of a knowledge base to hold facts and rules. When new facts or rules are added to the knowledge base with `student_code.kb_add`, forward chaining is applied to infer new facts and rules. The knowledge base also handles retracting of facts and rules with `student_code.kb_retract`. Truth maintenance is employed to keep the knowledge base up to date, and make sure all inferred facts and rules are grounded. The knowledge base can also be queried with `student_code.kb_ask` to see if facts or rules exist in the knowledge base.

## 2. A* Search
###### This was an assignment in the class MSAI 348 'Intro to AI' taught by Professor Jason (Willie) Wilson 
This is my implementation of A* search for pathing. The example used for this code is to find the fastest path around Northwestern's campus given travel times and direct distance measurements as the heuristic.
<img src="2_A Star Search/map.png" width="60%">

`student_code.a_star_search` can be called, providing the start and end locations to return the optimal path.

## 3. Minimax and Alpha Beta Pruning
###### This was an assignment in the class MSAI 348 'Intro to AI' taught by Professor Jason (Willie) Wilson 
This is my implementation of Minimax adversarial search to play the game: **Konane** 
<img src="3_Minimax and Alpha Beta/pictures/board.jpg" width=70%>

The program is built with varying levels of AI to play against. There is one version that only uses the minimax algorithm to choose the optimal move, and another version that builds upon the minimax algorithm and epmloys alpha-beta pruning to increase efficiency. The game to can be played by running 
```bash
python main.py $P1 $P2
```

## 4. PDDL Planning
###### This was an assignment in the class MSAI 348 'Intro to AI' taught by Professor Jason (Willie) Wilson 
Included are domain and problem files I created to be used with the online .pddl editor [here](http://editor.planning.domains/#) to simulate robot pathing within Amazon warehouses. The PDDL domain includes `actions {}` with necessary precondition and effects that can be carried out to fulfill the goal in the chosen problem file.

## 5. Bayes Net
###### This was an assignment in the class MSAI 348 'Intro to AI' taught by Professor Jason (Willie) Wilson 
This is my implementation of the infamous Earthquake or Burglary Baysian Network: 
![bayes-net](https://d2vlcm61l7u1fs.cloudfront.net/media%2F50a%2F50af1ba0-f8c3-4079-a7ac-f4ad6daa91a1%2Fphp9Te9am.png)

Given the joint probabilities for each individual event, the chain rule is propagated through the network to calculate conditional probabilities `P(A|B)`.

## 6. Naïve Bayes Classifier
###### This was an assignment in the class MSAI 348 'Intro to AI' taught by Professor Jason (Willie) Wilson 
This is my NBC implementation used to classify movie reviews as positive or negative. The implementation uses add-one smoothing, removal of stop words, removal of numerical and symbol characters, and removal of capitalization. 

My model reaches 0.934 and 0.755 f-scores for positive and negative classes, respectively after 10-fold cross-validation on the data set.

## ML- Decision Tree
###### This was an assignment in the class MSAI 349 'Machine Learning' taught by Professor Doug Downey 
`ID3.py` is my implementation of the ID3 decision tree algorithm using the calculation of info-gain to determine branches. Pruning is implemented to combat over-fitting during training. Nodes are only pruned if the training accuracy at that node does not decrease after pruning.

A decision tree can be created by calling:
```bash
ID3.ID3(data, default)
```
where `data` is an array of examples where each example is a dictionary of attribute:value pairs, and the target class variable is a special attribute with the name "Class". Any missing attributes are denoted with a value of "?" and `default` is the default value. The tree object is returned.

The tree can then be tested by calling:
```bash
ID3.test(node, examples)
```
where `node` is the trained tree object, and `examples` is a test set of examples. This returns an accuracy % of the test set that was classified correctly with the trained tree.

