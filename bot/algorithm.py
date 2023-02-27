class Vertex:
    """
    This class represents a Vertex object to be used with the
    Graph class.

    Attributes
        weights (Tuple(float, Vertex)[])
        data_class (str): the class of data that a vertex could be
        data_enum (str): data individualizing each vertex
    """
    
    def __init__(self, data_class, data_enum):
        """
        Initializes the Vertex class.

        Parameters
            data_class (str): the class of data that a vertex could be
            data_enum (str): data individualizing each vertex
        """
        
        self.edges = []
        self.data_class = data_class
        self.data_enum = data_enum

        
    def __eq__(self, other):
        """
        Equality operator.
        """
        _class_eq = self.data_class == other.data_class
        _enum_eq = self.data_enum == other.data_enum
        
        if _class_eq and _enum_eq:
            return True

        return False
              

    def emplace(self, weight, vertex):
        """
        Adds a new edge to the weight graph.

        Parameters
            weight (float): the weight to set for the edge
            vertex (Vertex): the vertex directed to
        """

        self.edges.insert(len(self.edges), [weight, vertex])
        
        
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
        self._initialize_graph(data)


    def __str__(self):
        """
        String representation of the Graph class.
        """

        _output = ''

        for _vertex in self.vertices:
            _output += f'{_vertex.data_class} ({_vertex.data_enum})\n'

            for _weight in _vertex.weights:
                _output += f'-> {_weight[0]} -> {_weight[1].data_class} ({_weight[1].data_enum})\n'
    
        return _output
    
        
    def add_vertex(self, data_class, data_enum):
        """
        Adds a vertex to vertices.
        """

        _vertex = Vertex(data_class, data_enum)
        
        self.vertices.append(_vertex)


    def _initialize_vertices(self, data):
        """
        Initializes the vertices for this graph.
        """

        for _data in data:
            _exchange = _data['exchange']
            
            for _currency in _data['currencies']:
                self.add_vertex(_currency, _exchange)


    def _initialize_edges_on_pairs(self, data):
        """
        Initializes the edges for this graph based on currency pairs.
        """
        for _data in data:
            for i in range(0, len(self.vertices)):
                for j in range(0, len(self.vertices)):
            
                    _exchange = _data['exchange']

                    for _pair in _data['pairs']:
                        _a = _pair['a']
                        _b = _pair['b']
                        _rate = _pair['rate']

                        _pair_match = self.vertices[i].data_class == _a and self.vertices[j].data_class == _b
                        _exchange_match = self.vertices[j].data_enum == _exchange

                        if _pair_match and _exchange_match:
                            self.vertices[i].emplace(_rate, self.vertices[j])


    def _initialize_edges_on_currency(self):
        """
        Initializes connector edges on same currencies.
        """

        for i in range(0, len(self.vertices)):
            for j in range(0, len(self.vertices)):
                _data_class_eq = self.vertices[i].data_class == self.vertices[j].data_class
                _data_enum_neq = self.vertices[i].data_enum != self.vertices[j].data_enum
                
                if _data_class_eq and _data_enum_neq:
                    self.vertices[i].emplace(1, self.vertices[j])
        

    def _initialize_edges(self, data):
        """
        Initializes the edges for this graph based on the data pattern.
        """

        self._initialize_edges_on_pairs(data)
        self._initialize_edges_on_currency()
                    
        
    def _initialize_graph(self, data):
        """
        Initializes the graph with data.
        """

        self._initialize_vertices(data)
        self._initialize_edges(data)


    def _r_compute_optimal_path_for_vertex(self, start_vertex, vertex, paths, previous_path_history):
        """
        Recursive step for algorithm to find all circuits in this Graph object.
        """

        for i in range(0, len(vertex.edges)):
            # copy path history
            _path_history = []
            
            for j in range(0, len(previous_path_history)):
                _path_history.append(previous_path_history[j])
                
            # get weight and prospective next vertex
            _weight = vertex.edges[i][0]
            _next_vertex = vertex.edges[i][1]

            # determine if the edge has already been traversed
            _edge_traversed = False

            if len(_path_history) > 1:
                for k in range(0, len(_path_history) - 1):
                    _vertex_a_eq = _path_history[k]['vertex'] == vertex
                    _vertex_b_eq = _path_history[k + 1]['vertex'] == _next_vertex

                    if _vertex_a_eq and _vertex_b_eq:
                        _edge_traversed = True

            # execute if edge hasn't been traversed
            if not _edge_traversed:
                if _next_vertex == start_vertex:
                    _path_history.append({
                        'weight': _weight,
                        'vertex': _next_vertex
                    })

                    paths.insert(len(paths), _path_history)

                else:
                    _path_history.append({
                        'weight': _weight,
                        'vertex': _next_vertex
                    })

                    self._r_compute_optimal_path_for_vertex(
                        start_vertex,
                        _next_vertex,
                        paths,
                        _path_history
                    )
                    
    
    def _compute_optimal_path_for_vertex(self, vertex):
        """
        Finds each circuit in the graph where the first and last vertices
        are of the same data class. The algorithm then computes the maximum
        product of each trail and returns the maximum. The circuit must begin
        and end on a vertex with the same data class and data enumerator and
        each edge and vertex may only be traversed once.
        """

        _paths = []
        _path_history = [
            {
                'weight': 1,
                'vertex': vertex
            }
        ]

        self._r_compute_optimal_path_for_vertex(
            vertex,
            vertex,
            _paths,
            _path_history
        )

        _max_total_edge_weight = 0
        _optimal_path = []
        
        for _path in _paths:
            _total_edge_weight = 1
            
            for _edge in _path:
                _total_edge_weight *= _edge['weight']

            if _total_edge_weight > _max_total_edge_weight:
                _max_total_edge_weight = _total_edge_weight
                _optimal_path = _path

        return [
            _max_total_edge_weight,
            _optimal_path
        ]
        
    
    def _compute_optimal_path_for_vertices(self):
        """
        Computes the maximum weight path cycle for each vertex in this
        Graph.
        """

        _data = []

        for _vertex in self.vertices:
            _path_data = self._compute_optimal_path_for_vertex(_vertex)

            _data.append(_path_data)
    
        return _data


    def _compute_optimal_path(self):
        """
        Computes the maximum weight path cycle for each optimized
        circuit.
        """

        _data = self._compute_optimal_path_for_vertices()

        _max_weight = 0
        _optimal_path = []

        for _path in _data:
            _weight = _path[0]

            if _weight > _max_weight:
                _max_weight = _weight
                _optimal_path = _path

        return _optimal_path


    def find_arbitrage(self):
        """
        Returns the optimal arbitrage opportunity based on a set
        of exchanges and exchange rates.
        """

        return self._compute_optimal_path()
    

data = [
    {
        'exchange': 'curve',
        'currencies': [
            'dai',
            'usdc',
            'usdt'
        ],
        'pairs': [
            {
                'a': 'dai',
                'b': 'usdc',
                'rate': 1.5
            },
            {
                'a': 'dai',
                'b': 'usdt',
                'rate': 2.5
            },
            {
                'a': 'usdc',
                'b': 'dai',
                'rate': 3.5
            },
            {
                'a': 'usdc',
                'b': 'usdt',
                'rate': 4.5
            },
            {
                'a': 'usdt',
                'b': 'dai',
                'rate': 5.5
            },
            {
                'a': 'usdt',
                'b': 'usdc',
                'rate': 6.5
            }
        ]
    }
]

g = Graph(data)
optimal_path = g.find_arbitrage()
print(optimal_path)
        


