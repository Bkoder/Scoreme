# Scoreme


The longest_path function is designed to find the longest path in a Directed Acyclic Graph (DAG) represented as an adjacency list. The function begins by determining the number of nodes n in the graph. It then defines an inner function topological_sort, which performs a topological sorting of the graph's nodes. This is achieved by first calculating the in-degrees of all nodes, identifying nodes with zero in-degrees, and processing them iteratively to build a topological order. Once the nodes are sorted topologically, the calculate_longest_path function is called. This function initializes a distance array dist with negative infinity values, representing the longest distance to each node, which are subsequently updated as the function iterates over each node in the topological order. For each node, if its distance is still negative infinity, it is set to zero, ensuring it can be considered a starting point. The function then updates the distances to each node's neighbors based on the edge weights. The longest path in the graph is determined by finding the maximum value in the distance array. Finally, the function returns this maximum value, which represents the length of the longest path in the DAG. This process ensures that all potential starting nodes are considered, and the longest path is accurately calculated.



# For testing
I completed this in windows version of pycharm. Hence, the testing part is according to that.

Running the Tests:
To run the tests using pytest in PyCharm:

Ensure pytest is installed:

Open a terminal and run pip install pytest.
Configure PyCharm to use pytest:

Open PyCharm.
Go to File > Settings.
Navigate to Tools > Python Integrated Tools.
In the Testing section, set the Default test runner to pytest.
Run tests using pytest:

Right-click on the test_main.py file in the Project Explorer.
Select Run 'pytest in test_main'.


![image](https://github.com/Bkoder/Scoreme/assets/73677076/960b8979-b22a-4967-885f-e7922cca6837)

![image](https://github.com/Bkoder/Scoreme/assets/73677076/f8698051-31c4-42f9-84ad-0d4c3a08d359)

