import java.util.Arrays;

public class Graph {
        // represents an edge in the graph
	protected class Edge {
        	public int in, out; 		// Indices of the vertices
        	public int weight;		// Weight of the edge
        } 
	
	protected MyVertex vertices[]; 	// vertex array
    	protected MyEdge edges[]; 	// edge array
    

	// increase the size of edge and vertex arrays
    	private void doubleArraySize() {
		int arraySize = vertices.length;
		vertices = Arrays.copyOf(vertices, arraySize*2);
		edges = Arrays.copyOf(edges, arraySize*2 * (arraySize*2-1));
	}
    
	// Creates an empty graph.	
	public Graph() {
		vertices = new MyVertex[1];
		edges = new MyEdge[0];
		
		...
	}

	// Returns the number of vertices in the graph.
	public int getNumberOfVertices() { 
		...
	}

	// Returns the number of edges in the graph.
	public int getNumberOfEdges() {
		...
	}

        // Returns an array of length getNumberOfVertices() with the inserted vertices.
	public MyVertex[] getVertices() { 
		...
	}

	// Returns an array of length getNumberOfEdges() with the inserted edges.
	public MyEdge[] getEdges() {
		...
	}

	// Insert a new vertex v into the graph and return its index in the vertex array.
	// If the vertex array is already full, then the method doubleArraySize() shall be called 
	// before inserting. 
        // Null elements are not allowed (IllegalArgumentException).
	public int insertVertex(MyVertex v) throws IllegalArgumentException {
		...
	}

	// Returns the edge weight if there is an edge between index v1 and v2, otherwise -1.
	// In case of unknown or identical vertex indices throw an IllegalArgumentException.
	public int hasEdge(int v1, int v2) throws IllegalArgumentException {
		...
	}

	// Inserts an edge between vertices with v1 and v2. False is returned if the edge already exists,
	// true otherwise. An IllegalArgumentException shall be thrown if the vertex indices are unknown or
	// if v1 == v2 (loop).
	public boolean insertEdge (int v1, int v2, int weight)  throws IllegalArgumentException { 
		...
	}

	// Returns an NxN adjacency matrix for the graph, where N = getNumVertices().
        // The matrix contains 1 if there is an edge at the index position, otherwise 0.
	public int[][] getAdjacencyMatrix() {
		...
	}

	// Returns an array of vertices which are adjacent to the vertex with index v.
	// If the vertex index v is unknown an IllegalArgumentException shall be thrown.
	public MyVertex[] getAdjacentVertices(int v) throws IllegalArgumentException {
		...
	}


	//-------------------------------------------------------------------
	//--------- Example 2 Methods
	
    
        // Returns true if the graph is connected, otherwise false. 
        // For the duration of the calculation temporarily convert the directed graph to an undirected graph.
	public boolean isConnected() {
		...
	}

	// Returns the number of all (weak) components 
	// For the duration of the calculation temporarily convert the directed graph to an undirected graph.
	public int getNumberOfComponents() { 
		...
	}

	// Prints the vertices of all components (one line per component).
	// For the duration of the calculation temporarily convert the directed graph to an undirected graph.
	public void printComponents() {
		...
	}

	// Returns true if the graphs contains cycles, otherwise false. 
	// For the duration of the calculation temporarily convert the directed graph to an undirected graph. 
	public boolean isCyclic() {
		...
	}
}
