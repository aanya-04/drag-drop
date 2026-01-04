# from fastapi import FastAPI, Form

# app = FastAPI()

# @app.get('/')
# def read_root():
#     return {'Ping': 'Pong'}

# @app.get('/pipelines/parse')
# def parse_pipeline(pipeline: str = Form(...)):
#     return {'status': 'parsed'}



# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from collections import defaultdict, deque

app = FastAPI(title="Pipeline API")

# CORS configuration for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response Models
class NodeData(BaseModel):
    """Node data structure"""
    id: str
    type: str
    data: Optional[Dict[str, Any]] = {}
    position: Optional[Dict[str, float]] = {}


class EdgeData(BaseModel):
    """Edge data structure"""
    id: str
    source: str
    target: str
    sourceHandle: Optional[str] = None
    targetHandle: Optional[str] = None


class PipelineRequest(BaseModel):
    """Pipeline submission payload"""
    nodes: List[NodeData]
    edges: List[EdgeData]


class PipelineResponse(BaseModel):
    """Pipeline analysis response"""
    num_nodes: int
    num_edges: int
    is_dag: bool


def is_dag(nodes: List[NodeData], edges: List[EdgeData]) -> bool:
    """
    Check if the graph is a Directed Acyclic Graph (DAG)
    
    Uses Kahn's algorithm (topological sort) to detect cycles:
    1. Calculate in-degree for each node
    2. Start with nodes that have 0 in-degree
    3. Remove nodes and edges, updating in-degrees
    4. If all nodes are processed, it's a DAG
    
    Args:
        nodes: List of node data
        edges: List of edge data
        
    Returns:
        bool: True if graph is a DAG, False if it contains cycles
    """
    if not nodes:
        return True
    
    # Build adjacency list and in-degree map
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Initialize all nodes with in-degree 0
    node_ids = {node.id for node in nodes}
    for node_id in node_ids:
        in_degree[node_id] = 0
    
    # Build graph from edges
    for edge in edges:
        source = edge.source
        target = edge.target
        
        # Only consider edges between existing nodes
        if source in node_ids and target in node_ids:
            graph[source].append(target)
            in_degree[target] += 1
    
    # Kahn's algorithm for topological sort
    queue = deque()
    
    # Start with nodes that have no incoming edges
    for node_id in node_ids:
        if in_degree[node_id] == 0:
            queue.append(node_id)
    
    processed_count = 0
    
    while queue:
        current = queue.popleft()
        processed_count += 1
        
        # For each neighbor, reduce in-degree
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            
            # If in-degree becomes 0, add to queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If we processed all nodes, it's a DAG
    # If some nodes remain, there's a cycle
    return processed_count == len(node_ids)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "ok", "message": "Pipeline API is running"}


@app.post("/pipelines/parse", response_model=PipelineResponse)
async def parse_pipeline(pipeline: PipelineRequest):
    """
    Parse and analyze pipeline
    
    Analyzes the submitted pipeline to:
    1. Count nodes
    2. Count edges
    3. Determine if the graph is a DAG (no cycles)
    
    Args:
        pipeline: Pipeline data containing nodes and edges
        
    Returns:
        PipelineResponse with analysis results
        
    Raises:
        HTTPException: If pipeline data is invalid
    """
    try:
        # Count nodes and edges
        num_nodes = len(pipeline.nodes)
        num_edges = len(pipeline.edges)
        
        # Check if graph is a DAG
        is_valid_dag = is_dag(pipeline.nodes, pipeline.edges)
        
        # Log for debugging
        print(f"Pipeline analysis:")
        print(f"  Nodes: {num_nodes}")
        print(f"  Edges: {num_edges}")
        print(f"  Is DAG: {is_valid_dag}")
        
        return PipelineResponse(
            num_nodes=num_nodes,
            num_edges=num_edges,
            is_dag=is_valid_dag
        )
        
    except Exception as e:
        print(f"Error analyzing pipeline: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing pipeline: {str(e)}"
        )


@app.get("/pipelines/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "endpoints": {
            "parse": "/pipelines/parse",
            "health": "/pipelines/health"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)