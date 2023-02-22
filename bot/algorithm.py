class Node:
    """
    This class represents a Node object to be used with the
    Graph class.

    Attributes
        data_class (str): the class of data that a node could be
        data_enum (str): data individualizing each node
    """
    
    def __init__(self, data_class, data_enum):
        """
        Initializes the Node class.

        Parameters
            data_class (str): the class of data that a node could be
            data_enum (str): data individualizing each node
        """
        self.weights = []
        self.data_class = data_class
        self.data_enum = data_enum

    def emplace(self, weight, node):
        """
        Adds a new node to the weight graph.

        Parameters
            weight (float): the weight to set for the edge
            node (Node): the next node in succession
        """
        
        self.weights.append((weight, node))

        
class Graph:
    """
    This class repsents a graph object where two nodes exist
    of each type and each direction of edge between each node is
    present. Each node of the same type should have a weight of
    1. The graph is directed.
    """
    
    def __init__(self, data):
        """
        Initializes the Graph class.
        """
        
        self.head = None


    def initialize(self, data):
        """
        Initializes the data representation of the graph with
        data of a digestible data structure.
        """

        


