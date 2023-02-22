class Vertex:
    """
    This class represents a Vertex object to be used with the
    Graph class.

    Attributes
        data_class (str): the class of data that a vertex could be
        data_enum (str): data individualizing each vertex
    """
    
    def __init__(self, data_class, data_enum, weights=[]):
        """
        Initializes the Vertex class.

        Parameters
            weights (Tuple(float, Vertex)): weights defining edges
            data_class (str): the class of data that a vertex could be
            data_enum (str): data individualizing each vertex
        """
        self.weights = weights
        self.data_class = data_class
        self.data_enum = data_enum

    def emplace(self, weight, vertex):
        """
        Adds a new edge to the weight graph.

        Parameters
            weight (float): the weight to set for the edge
            vertex (Vertex): the vertex directed to
        """
        
        self.weights.append((weight, vertex))

        
class Graph:
    """
    This class repsents a directed graph object where two vertices
    exist of each type and each direction of edge between each
    vertex is present. Each vertex of the same type should have a
    weight of 1.

    Data should be of format:

    data = [
        {
            'exchange': 'curve',
            'currencies': [
                'dai',
                'usdc'
            ],
            'pairs': [
                {
                    'a': 'dai',
                    'b': 'usdc',
                    'rate': 1
                }
            ]
        }
    ]

    Attributes
        vertices (Vertex[]): vertices in this graph
    """
    

    def __init__(self, data):
        """
        Initializes the Graph class.
        """

        self.vertices = []


    def add_vertex(self, data_class, data_enum):
        """
        Adds a vertex to vertices.
        """

        _vertex = Vertex(data_class, data_enum)
        
        self.vertices.append(_vertex)


    def get_vertex(self, data_class, data_enum):
        """
        Gets a vertex from this Graph object.
        """

        for _vertex in self.vertices:
            if _vertex.data_class == data_class and _vertex.data_enum == data_enum:
                return _vertex

        return None


    def remove_vertex(self, data_class, data_enum):
        """
        Removes a vertex from this Graph object.
        """

        _vertex = self.get_vertex(data_class, data_enum)

        self.vertices.remove(_vertex)

        
    def _initialize_vertices(self, data):
        """
        Initializes the vertices for this graph.
        """

        for _exchange in data:
            for _currency in _exchange['currencies']:
                self.graph.add_vertex(_currency, _exchange['exchange'])


    def _initialize_edges(self, data):
        """
        Initializes the edges for this graph based on the data pattern.
        """

        pass
    
        
    def _initialize_graph(self, data):
        """
        Initializes the graph with data.
        """

        self._initialize_vertices(data)
        self._initialize_edges(data)


data = [
    {
        'exchange': 'curve',
        'currencies': [
            'dai',
            'usdc'
        ],
        'pairs': [
            {
                'a': 'dai',
                'b': 'usdc'
            }
        ]
    }
]

        


