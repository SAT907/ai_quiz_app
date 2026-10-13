import json

questions = [
    # --- UNIT I: FOUNDATIONS, ENVIRONMENTS & RATIONAL AGENTS (1–10) ---
    {
        "id": 1,
        "question": "Assertion (A): The Winograd Schema Challenge is considered a more robust alternative to the standard Turing Test.\nReason (R): It relies on resolving pronoun disambiguation requiring deep commonsense reasoning.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A.",
            "Both A and R are true, but R is NOT the correct explanation.",
            "A is true, but R is false.",
            "A is false, but R is true."
        ],
        "answer": "Both A and R are true, and R is the correct explanation of A.",
        "explanation": "Winograd schemas test pronoun resolution requiring world knowledge rather than superficial chatbot conversational tricks."
    },
    {
        "id": 2,
        "question": "An agent playing stochastic poker chooses a move with a 10% chance of winning $1000 and 90% chance of losing $100, instead of a guaranteed $0 fold. Assuming risk neutrality, is it acting rationally?",
        "options": [
            "Yes, because Expected Value ($100 - $90 = $10) exceeds $0 fold.",
            "No, because the probability of losing (90%) is too high.",
            "Yes, because risk-neutral agents ignore probabilities.",
            "No, poker agents cannot be evaluated by rationality."
        ],
        "answer": "Yes, because Expected Value ($100 - $90 = $10) exceeds $0 fold.",
        "explanation": "Rationality maximizes expected utility ($10), which is superior to folding ($0)."
    },
    {
        "id": 3,
        "question": "Match environment classifications: (1) Robotic soccer, (2) Medical diagnosis, (3) Image classification with (p) Episodic/Static/Fully Observable, (q) Multi-agent/Continuous/Dynamic, (r) Single-agent/Stochastic/Sequential.",
        "options": [
            "1-q, 2-r, 3-p",
            "1-p, 2-r, 3-q",
            "1-r, 2-q, 3-p",
            "1-q, 2-p, 3-r"
        ],
        "answer": "1-q, 2-r, 3-p",
        "explanation": "Robotic soccer is multi-agent dynamic; medical diagnosis is sequential stochastic; image classification is episodic static."
    },
    {
        "id": 4,
        "question": "In a utility-based agent, if the environment is partially observable, how does the agent make decisions?",
        "options": [
            "Calculates expected utility by averaging over possible state outcomes weighted by belief probabilities.",
            "Ignores unobservable variables and uses simple reflex rules.",
            "Executes random actions until full observability is restored.",
            "Constructs an infinite lookup table of all historical percepts."
        ],
        "answer": "Calculates expected utility by averaging over possible state outcomes weighted by belief probabilities.",
        "explanation": "Partially observable decisions require weighing expected utility across probabilistic belief states."
    },
    {
        "id": 5,
        "question": "In a learning agent, which element suggests actions that lead to new experiences even if sub-optimal in the short term (exploration)?",
        "options": [
            "Problem Generator",
            "Learning Element",
            "Performance Element",
            "Critic"
        ],
        "answer": "Problem Generator",
        "explanation": "The Problem Generator proposes exploratory actions to discover new knowledge."
    },
    {
        "id": 6,
        "question": "For an algorithmic trading agent, if Performance is 'ROI', what constitutes its Actuators?",
        "options": [
            "Network API calls executing buy/sell/hold orders",
            "Stock exchange market feed data",
            "Historical price database tables",
            "CPU arithmetic execution units"
        ],
        "answer": "Network API calls executing buy/sell/hold orders",
        "explanation": "Actuators are the mechanisms through which the agent performs actions on its environment."
    },
    {
        "id": 7,
        "question": "True or False: In a fully unobservable environment, the agent's belief state space is smaller than the physical state space.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "The belief state space is the power set of all physical states, making it exponentially larger ($2^N$)."
    },
    {
        "id": 8,
        "question": "The Physical Symbol System Hypothesis (Newell and Simon) posits that:",
        "options": [
            "A physical symbol system has necessary and sufficient means for general intelligent action.",
            "Intelligence can only exist within biological neural architectures.",
            "Symbolic processing is incapable of solving NP-hard search problems.",
            "Sub-symbolic neural networks replace predicate logic entirely."
        ],
        "answer": "A physical symbol system has necessary and sufficient means for general intelligent action.",
        "explanation": "Newell & Simon hypothesized that manipulating physical symbols is sufficient for general intelligence."
    },
    {
        "id": 9,
        "question": "Assertion (A): Episodic environments do not require an agent to plan ahead.\nReason (R): In episodic environments, current decisions do not affect future episodes.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A.",
            "Both A and R are true, but R is NOT the correct explanation.",
            "A is true, but R is false.",
            "A is false, but R is true."
        ],
        "answer": "Both A and R are true, and R is the correct explanation of A.",
        "explanation": "In episodic environments, actions are isolated; decisions do not impact future percepts or states."
    },
    {
        "id": 10,
        "question": "If multiple goals conflict (e.g., speed vs. safety), a simple goal-based agent fails to resolve the trade-off. What is required?",
        "options": [
            "A Utility Function mapping states to real numbers",
            "A larger lookup table",
            "An unobservability sensor array",
            "An iterative search tree"
        ],
        "answer": "A Utility Function mapping states to real numbers",
        "explanation": "Utility functions quantify trade-offs when conflicting goals exist."
    },

    # --- UNIT I: PROBLEM FORMULATION & PRODUCTION SYSTEMS (11–20) ---
    {
        "id": 11,
        "question": "If a state-space problem allows negative step costs (non-monotonic path costs), which issue arises during search?",
        "options": [
            "Algorithms like Uniform Cost Search fail due to infinite decreasing cost cycles.",
            "The branching factor becomes negative.",
            "Heuristics automatically become admissible.",
            "DFS executes faster than BFS."
        ],
        "answer": "Algorithms like Uniform Cost Search fail due to infinite decreasing cost cycles.",
        "explanation": "Non-monotonic path costs allow infinite loops where total path cost decreases continuously."
    },
    {
        "id": 12,
        "question": "A problem where a larger task can be broken down into independent smaller tasks (represented by AND/OR graphs) is called a ________ problem.",
        "options": ["Decomposable", "Ignorable", "Irrecoverable", "Constraint-Free"],
        "answer": "Decomposable",
        "explanation": "Decomposable problems split into independent sub-problems that can be solved separately."
    },
    {
        "id": 13,
        "question": "In the 15-puzzle, the physical space has 16! states. Based on parity rules, how many disjoint reachable state-space graphs exist?",
        "options": ["Two", "Sixteen", "One", "15!"],
        "answer": "Two",
        "explanation": "Permutation inversion parity splits the 15-puzzle state space into exactly two unreachable components."
    },
    {
        "id": 14,
        "question": "In the context of the Rete Algorithm used in production systems, how is computational efficiency achieved?",
        "answer": "By storing partial rule match states across cycles, avoiding re-evaluating unchanged working memory.",
        "options": [
            "By storing partial rule match states across cycles, avoiding re-evaluating unchanged working memory.",
            "By converting all production rules into First-Order Predicate Logic clauses.",
            "By running parallel DFS threads on working memory elements.",
            "By disabling conflict resolution mechanisms entirely."
        ],
        "explanation": "Rete constructs a network of nodes saving match states to avoid redundant rule processing."
    },
    {
        "id": 15,
        "question": "True or False: Lexicographic ordering in production systems resolves conflicts by firing the most recently added rule in working memory.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "Lexicographic ordering resolves based on rule priority/specificity; Recency-based resolves by data age."
    },
    {
        "id": 16,
        "question": "Assertion (A): Tree-search algorithms fail in loopy (cyclic) state graphs.\nReason (R): Without an explored set (closed list), tree search repeatedly expands cycles infinitely.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A.",
            "Both A and R are true, but R is NOT the correct explanation.",
            "A is true, but R is false.",
            "A is false, but R is true."
        ],
        "answer": "Both A and R are true, and R is the correct explanation of A.",
        "explanation": "Without maintaining visited states, tree search descends into infinite loops."
    },
    {
        "id": 17,
        "question": "In stochastic environments, the transition model P(s' | s, a) replaces deterministic RESULT(s, a). This structure forms the basis of:",
        "options": [
            "Markov Decision Processes (MDPs)",
            "Constraint Satisfaction Problems (CSPs)",
            "Means-End Analysis tables",
            "First-Order Horn Clause resolution"
        ],
        "answer": "Markov Decision Processes (MDPs)",
        "explanation": "MDPs formally model decision making in discrete, stochastic transition environments."
    },
    {
        "id": 18,
        "question": "Playing chess is an irrecoverable problem. How does search program design handle this before executing physical moves?",
        "options": [
            "Utilizes a simulated internal state space to plan moves before committing actuator actions.",
            "Relies on simple reflex condition-action lookup tables.",
            "Applies arc consistency to physical chess pieces.",
            "Ignores opponent moves until checkmate occurs."
        ],
        "answer": "Utilizes a simulated internal state space to plan moves before committing actuator actions.",
        "explanation": "Simulated state space planning prevents making un-retractable bad physical moves."
    },
    {
        "id": 19,
        "question": "The process of removing irrelevant details from a state representation to reduce state space size is called ________.",
        "options": ["Abstraction", "Quantification", "Resolution", "Backjumping"],
        "answer": "Abstraction",
        "explanation": "Abstraction removes domain details to build manageable search representations."
    },
    {
        "id": 20,
        "question": "In the N-Queens problem, the goal test is usually defined by checking a ________.",
        "options": [
            "Property (No queen attacks any other queen)",
            "Pre-calculated lookup state table",
            "Heuristic score of zero in memory",
            "Reconstructive parent path dictionary"
        ],
        "answer": "Property (No queen attacks any other queen)",
        "explanation": "Goal states in N-Queens satisfy implicit constraint properties rather than explicit target states."
    },

    # --- LAB 1: PYTHON LIBRARIES FOR MACHINE LEARNING (21–25) ---
    {
        "id": 21,
        "question": "When manipulating a state-space dataset in Pandas, why is `df['cost'] = df['cost'] * 2` preferred over `for index, row in df.iterrows():`?",
        "options": [
            "Vectorized operations run in highly optimized C underlying NumPy, reducing interpreter overhead.",
            "`list.pop(0)` causes recursive overflow errors.",
            "`deque` automatically removes duplicate states.",
            "Standard lists cannot hold graph node objects."
        ],
        "answer": "Vectorized operations run in highly optimized C underlying NumPy, reducing interpreter overhead.",
        "explanation": "Pandas vectorization executes in C/NumPy C-API, bypassing slow Python loop iteration."
    },
    {
        "id": 22,
        "question": "Applying `StandardScaler().fit_transform()` to an entire dataset before splitting into X_train and X_test causes:",
        "options": [
            "Data Leakage (test set parameters corrupt training normalization).",
            "Dummy Variable Trap.",
            "Recursion Limit Error.",
            "Non-monotonic heuristic evaluation."
        ],
        "answer": "Data Leakage (test set parameters corrupt training normalization).",
        "explanation": "Fitting scalers on full datasets leaks test set mean/variance into training data."
    },
    {
        "id": 23,
        "question": "You add a 1D NumPy array of shape (3,) to a 2D array of shape (4, 3). What is the shape of the resulting array?",
        "options": ["(4, 3)", "(3, 4)", "(7, 3)", "ValueError"],
        "answer": "(4, 3)",
        "explanation": "NumPy broadcasting expands the 1D array across the missing dimension to match (4, 3)."
    },
    {
        "id": 24,
        "question": "When converting categorical percepts into numeric vectors via One-Hot Encoding, dropping one dummy column prevents:",
        "options": [
            "Dummy Variable Trap (Multicollinearity)",
            "Overfitting on small sample sizes",
            "Data Leakage during cross-validation",
            "Gradient Vanishing in local search"
        ],
        "answer": "Dummy Variable Trap (Multicollinearity)",
        "explanation": "Dropping one indicator column eliminates perfect linear dependency among features."
    },
    {
        "id": 25,
        "question": "What is the primary architectural advantage of using `sklearn.pipeline.Pipeline`?",
        "options": [
            "Ensures transformations and model fitting occur safely inside CV folds without leakage.",
            "Accelerates BFS queue popping to O(1) time.",
            "Converts non-admissible heuristics into admissible ones.",
            "Overrides Python recursion limits automatically."
        ],
        "answer": "Ensures transformations and model fitting occur safely inside CV folds without leakage.",
        "explanation": "Pipelines encapsulate data preprocessing with estimators, preventing information leakage during cross-validation."
    },

    # --- UNIT II: UNINFORMED SEARCH & LOCAL SEARCH (26–35) ---
    {
        "id": 26,
        "question": "Depth-First Search (DFS) is incomplete in infinite state spaces. If applied to a finite state space with cycles, is it complete?",
        "options": [
            "Only if implemented as Graph-Search (maintaining an explored set).",
            "Yes, DFS is always complete in finite spaces regardless of cycles.",
            "No, DFS requires admissible heuristics to handle cycles.",
            "Only if branching factor b = 2."
        ],
        "answer": "Only if implemented as Graph-Search (maintaining an explored set).",
        "explanation": "Without visited state tracking, DFS gets trapped in infinite cyclic loops even in finite spaces."
    },
    {
        "id": 27,
        "question": "Assertion (A): Iterative Deepening (IDDFS) wastes massive amounts of computation by regenerating nodes.\nReason (R): For b >= 2, the bottom level dominates node count, bounding overhead to a small factor ~ b/(b-1).",
        "options": [
            "A is false (overhead is negligible), R is true.",
            "Both A and R are true, and R is the correct explanation.",
            "Both A and R are true, but R is NOT the correct explanation.",
            "A is true, but R is false."
        ],
        "answer": "A is false (overhead is negligible), R is true.",
        "explanation": "IDDFS node regeneration adds minimal overhead (~b/(b-1)) because leaf level nodes dominate total count."
    },
    {
        "id": 28,
        "question": "Uniform Cost Search expands the node with lowest path cost g(n). Which data structure implements its frontier?",
        "options": ["Priority Queue (Min-Heap)", "FIFO Queue", "LIFO Stack", "Disjoint Set"],
        "answer": "Priority Queue (Min-Heap)",
        "explanation": "Min-Heaps keep frontier nodes ordered by cumulative path cost g(n) in O(log N) time."
    },
    {
        "id": 29,
        "question": "Bidirectional search reduces time complexity from O(b^d) to ________ by running two simultaneous BFS operations.",
        "options": ["O(b^(d/2))", "O(b * d)", "O(b^2d)", "O(d * log b)"],
        "answer": "O(b^(d/2))",
        "explanation": "Searching from both start and goal meets in the middle at depth d/2."
    },
    {
        "id": 30,
        "question": "In a continuous delivery graph, if simple Hill Climbing reaches a location where all neighbors have identical travel costs, it is on a:",
        "options": ["Plateau", "Ridge", "Global Maximum", "Local Minimum"],
        "answer": "Plateau",
        "explanation": "A plateau is a flat region of the state space landscape with identical evaluation values."
    },
    {
        "id": 31,
        "question": "Why does simple Hill Climbing fail when navigating a 'Ridge' in the search landscape?",
        "options": [
            "Moves along primary axes yield downhill steps; progress requires diagonal moves.",
            "Ridges have infinite branching factors.",
            "The temperature parameter drops to zero.",
            "Heuristic evaluation returns zero."
        ],
        "answer": "Moves along primary axes yield downhill steps; progress requires diagonal moves.",
        "explanation": "Ridges force single-axis moves downward, causing simple hill climbing to halt."
    },
    {
        "id": 32,
        "question": "True or False: Stochastic Hill Climbing guarantees finding the global maximum faster than Steepest-Ascent Hill Climbing.",
        "options": ["True", "False"],
        "answer": "False",
        "explanation": "Stochastic hill climbing converges slower, though it has better chances of escaping local optima."
    },
    {
        "id": 33,
        "question": "Assertion (A): As Temperature T approaches 0, Simulated Annealing behaves like simple Hill Climbing.\nReason (R): When T=0, bad move acceptance probability e^(delta_E / T) approaches 0.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A.",
            "Both A and R are true, but R is NOT the correct explanation.",
            "A is true, but R is false.",
            "A is false, but R is true."
        ],
        "answer": "Both A and R are true, and R is the correct explanation of A.",
        "explanation": "As T drops to zero, bad move acceptance drops to zero, converting search to pure greedy hill climbing."
    },
    {
        "id": 34,
        "question": "How does Local Beam Search differ fundamentally from Random-Restart Hill Climbing running k threads?",
        "options": [
            "Local Beam Search threads share state information and pool successors; Random-Restart threads act independently.",
            "Local Beam Search uses linear memory O(bd) while Random-Restart uses O(b^d).",
            "Random-Restart threads use heuristics while Beam Search is uninformed.",
            "Beam Search only works in discrete CSP environments."
        ],
        "answer": "Local Beam Search threads share state information and pool successors; Random-Restart threads act independently.",
        "explanation": "Beam search passes information between k parallel states, selecting the best k overall successors."
    },
    {
        "id": 35,
        "question": "Uninformed search algorithms maintain paths to backtrack, whereas Local Search algorithms maintain only the ________ state using O(1) memory.",
        "options": ["Current", "Initial", "Goal", "Explored"],
        "answer": "Current",
        "explanation": "Local search retains only the current state evaluation, discarding historical search paths."
    },

    # --- UNIT II: HEURISTICS, CSP, & MEANS-END ANALYSIS (36–45) ---
    {
        "id": 36,
        "question": "A heuristic h(n) is consistent (monotonic) if for every node n and successor n' generated by action a:",
        "options": [
            "h(n) <= c(n, a, n') + h(n')",
            "h(n) >= c(n, a, n') + h(n')",
            "h(n) = g(n) + h(n')",
            "h(n) <= g(n)"
        ],
        "answer": "h(n) <= c(n, a, n') + h(n')",
        "explanation": "Consistency enforces triangle inequality: estimated cost from n is <= step cost to n' plus estimated cost from n'."
    },
    {
        "id": 37,
        "question": "Assertion (A): IDA* solves the exponential space complexity problem of A*.\nReason (R): IDA* uses f-cost limits to perform depth-first search, keeping memory linear O(bd).",
        "options": [
            "Both A and R are true, and R is the correct explanation of A.",
            "Both A and R are true, but R is NOT the correct explanation.",
            "A is true, but R is false.",
            "A is false, but R is true."
        ],
        "answer": "Both A and R are true, and R is the correct explanation of A.",
        "explanation": "IDA* runs depth-first search bounded by an f-cost threshold, reducing memory footprint from exponential to linear."
    },
    {
        "id": 38,
        "question": "Under what condition does Greedy Best-First Search (f(n) = h(n)) behave identically to pure DFS?",
        "options": [
            "When heuristic h(n) is defined as negative depth, i.e., h(n) = -depth(n).",
            "When h(n) = 0 for all nodes.",
            "When all edge costs are constant.",
            "When branching factor b = 1."
        ],
        "answer": "When heuristic h(n) is defined as negative depth, i.e., h(n) = -depth(n).",
        "explanation": "Setting h(n) = -depth forces Greedy Best-First Search to always expand the deepest node."
    },
    {
        "id": 39,
        "question": "To handle n-ary constraints (constraints among 3+ variables), CSPs can be converted to binary CSPs by creating a ________ graph.",
        "options": ["Dual", "Bipartite", "Directed Acyclic", "Complete"],
        "answer": "Dual",
        "explanation": "Dual graph transformations turn original constraints into variables to convert n-ary CSPs into binary CSPs."
    },
    {
        "id": 40,
        "question": "For a CSP with n variables, domain size d, and c binary constraints, what is the worst-case time complexity of AC-3?",
        "options": ["O(c * d^3)", "O(n^2 * d^2)", "O(c * d)", "O(d^n)"],
        "answer": "O(c * d^3)",
        "explanation": "AC-3 processes up to c constraints, where each arc can be inserted d times, and arc consistency testing takes O(d^2)."
    },
    {
        "id": 41,
        "question": "When Minimum Remaining Values (MRV) finds multiple variables with identical domain size, which heuristic acts as tie-breaker?",
        "options": ["Degree Heuristic", "Least Constraining Value", "Forward Checking", "Arc Consistency"],
        "answer": "Degree Heuristic",
        "explanation": "Degree Heuristic selects the variable involved in the most constraints with other unassigned variables."
    },
    {
        "id": 42,
        "question": "True or False: Conflict-directed backjumping jumps directly to the conflict set variable that caused failure rather than the immediate parent.",
        "options": ["True", "False"],
        "answer": "True",
        "explanation": "Conflict-directed backjumping bypasses non-relevant intermediate variables during search failure."
    },
    {
        "id": 43,
        "question": "In 1-million Queens problem, using Min-Conflicts local search, how is the next move determined?",
        "options": [
            "Selects a random conflicted queen and moves it to the row with minimal constraint violations.",
            "Runs AC-3 arc consistency across all 1 million rows.",
            "Executes complete A* search with Manhattan distance.",
            "Backtracks chronologically through queen placements."
        ],
        "answer": "Selects a random conflicted queen and moves it to the row with minimal constraint violations.",
        "explanation": "Min-conflicts iteratively reassigns values to randomly chosen conflicted variables to minimize conflicts."
    },
    {
        "id": 44,
        "question": "Assertion (A): Means-End Analysis (MEA) suffers from the 'Sussman Anomaly' in planning.\nReason (R): Solving one sub-goal in MEA can inadvertently undo preconditions needed for a previously solved sub-goal.",
        "options": [
            "Both A and R are true, and R is the correct explanation of A.",
            "Both A and R are true, but R is NOT the correct explanation.",
            "A is true, but R is false.",
            "A is false, but R is true."
        ],
        "answer": "Both A and R are true, and R is the correct explanation of A.",
        "explanation": "Sussman Anomaly highlights non-interleaved sub-goal planning failures where solving sub-goal B destroys sub-goal A."
    },
    {
        "id": 45,
        "question": "In MEA, a ________ table maps state differences to operators capable of reducing those differences.",
        "options": ["Difference", "Transition", "Heuristic", "Constraint"],
        "answer": "Difference",
        "explanation": "Operator-Difference tables store actions indexed by the state differences they eliminate."
    },

    # --- LAB 2: IMPLEMENTATION OF BFS AND DFS IN PYTHON (46–50) ---
    {
        "id": 46,
        "question": "When implementing BFS in Python, why is `collections.deque` preferred over standard `list.pop(0)`?",
        "options": [
            "`deque.popleft()` runs in O(1) time while `list.pop(0)` requires O(N) memory shifting.",
            "`list.pop(0)` causes recursive overflow errors.",
            "`deque` automatically removes duplicate states.",
            "Standard lists cannot hold graph node objects."
        ],
        "answer": "`deque.popleft()` runs in O(1) time while `list.pop(0)` requires O(N) memory shifting.",
        "explanation": "Python lists shift all elements left on `pop(0)`, making queue operations O(N)."
    },
    {
        "id": 47,
        "question": "When implementing recursive DFS on deeply nested graphs in Python, how do you bypass a `RecursionError`?",
        "options": [
            "`sys.setrecursionlimit(new_limit)`",
            "`collections.deque(maxlen=1000)`",
            "`tracemalloc.start()`",
            "`StandardScaler().fit_transform()`"
        ],
        "answer": "`sys.setrecursionlimit(new_limit)`",
        "explanation": "`sys.setrecursionlimit()` increases Python's maximum call stack depth."
    },
    {
        "id": 48,
        "question": "In Python search implementations, why is `explored = set()` vastly superior to `explored = []` for cycle checking?",
        "options": [
            "`set` hash lookups run in average O(1) time versus O(N) linear search in lists.",
            "Lists cannot store tuples.",
            "`set` automatically sorts search nodes by heuristic.",
            "Lists consume double the RAM."
        ],
        "answer": "`set` hash lookups run in average O(1) time versus O(N) linear search in lists.",
        "explanation": "Hash sets allow instant O(1) state membership verification."
    },
    {
        "id": 49,
        "question": "Instead of storing full paths in BFS queues, how do you reconstruct the path efficiently upon reaching the goal?",
        "options": [
            "Maintain a parent dictionary (`parent[child] = current`) and trace backward.",
            "Re-run DFS from the goal node.",
            "Export state transitions to Pandas DataFrames.",
            "Apply AC-3 domain reduction to visited nodes."
        ],
        "answer": "Maintain a parent dictionary (`parent[child] = current`) and trace backward.",
        "explanation": "Parent pointer mapping reconstructs optimal paths without clogging queue memory with complete state paths."
    },
    {
        "id": 50,
        "question": "To empirically measure peak memory consumption of search algorithms in Python, import the built-in module ________.",
        "options": ["tracemalloc", "sys", "timeit", "gc"],
        "answer": "tracemalloc",
        "explanation": "`tracemalloc` tracks memory allocations in Python scripts."
    }
]

with open('questions.json', 'w') as f:
    json.dump(questions, f, indent=2)

print("Successfully generated 'questions.json' with all 50 questions!")