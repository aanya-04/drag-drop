🔗 Pipeline Builder
A scalable, modern node-based pipeline builder built with React Flow and FastAPI. Features a reusable node abstraction system that reduces code duplication by 80% while maintaining flexibility and maintainability.
✨ Features
🎯 Core Features

Reusable Node Abstraction - Single BaseNode component eliminates code duplication
Dynamic Variables - Text nodes support {{ variableName }} syntax with automatic handle creation
Auto-Resize - Text nodes automatically adjust width and height based on content
DAG Detection - Backend validates pipeline structure using Kahn's algorithm
Beautiful UI - Modern design with Teal & Blue color scheme
Real-time Analysis - Instant feedback on node count, edge count, and DAG status

📦 Node Types

Input Node - Data input with configurable types (Text, File)
Output Node - Data output with multiple formats (Text, Image)
Text Node - Enhanced text processing with variable interpolation
LLM Node - Language model integration placeholder
Math Node - Mathematical operations (add, subtract, multiply, divide, power, modulo)
API Node - HTTP request node with method selection
Logger Node - Console logging with configurable levels
Condition Node - Conditional branching (true/false paths)
Delay Node - Time-based delays with multiple units

🚀 Quick Start
Prerequisites

Node.js 16+ and npm
Python 3.8+
Git

Installation
1. Clone the Repository
bashgit clone https://github.com/yourusername/pipeline-builder.git
cd pipeline-builder
2. Backend Setup
bashcd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn pydantic

# Start the server
uvicorn main:app --reload
The backend will be available at http://localhost:8000
3. Frontend Setup
bashcd frontend

# Install dependencies
npm install

# Start development server
npm start
The frontend will open at http://localhost:3000
📁 Project Structure
pipeline-builder/
├── frontend/
│   └── src/
│       ├── nodes/
│       │   ├── BaseNode.js          # Core node abstraction
│       │   ├── BaseNode.css         # Universal node styling
│       │   ├── nodeFactory.js       # Helper utilities
│       │   ├── nodeTypes.js         # Node registry
│       │   ├── inputNode.js         # Input node
│       │   ├── outputNode.js        # Output node
│       │   ├── llmNode.js           # LLM node
│       │   ├── textNode.js          # Enhanced text node
│       │   ├── MathNode.js          # Math operations
│       │   ├── APINode.js           # HTTP requests
│       │   ├── LoggerNode.js        # Console logging
│       │   ├── ConditionNode.js     # Conditional logic
│       │   └── DelayNode.js         # Time delays
│       ├── submit.js                # Pipeline submission
│       ├── index.css                # Global styles
│       ├── App.js                   # Main application
│       └── index.js                 # Entry point
├── backend/
│   └── main.py                      # FastAPI backend
├── README.md
└── .gitignore
🎨 Architecture
BaseNode Abstraction
The core of this project is the BaseNode component, which eliminates code duplication across all node types.
Configuration Interface
javascript{
  title: string,              // Node display title
  nodeType: string,           // Type for styling
  inputs: Array<Handle>,      // Input handle configurations
  outputs: Array<Handle>,     // Output handle configurations
  renderContent: Function,    // Custom content renderer
  contentProps: Object        // Props for content renderer
}
Handle Configuration
javascript{
  id: string,       // Unique identifier
  label: string,    // Display label
  color: string,    // Handle color
  top: string       // Vertical position (optional)
}
Creating a New Node
Creating a new node requires only ~20-30 lines of code:
javascriptimport { useState } from 'react';
import BaseNode from './BaseNode';

const MyNodeContent = ({ id, data }) => {
  const [value, setValue] = useState(data?.value || '');
  
  return (
    <input
      className="base-node__input"
      value={value}
      onChange={(e) => setValue(e.target.value)}
      placeholder="Enter value"
    />
  );
};

export const MyNode = (props) => {
  const nodeData = {
    title: '⚡ My Node',
    nodeType: 'mynode',
    inputs: [{ id: 'input', label: 'Input' }],
    outputs: [{ id: 'output', label: 'Output' }],
    renderContent: MyNodeContent,
    contentProps: props.data
  };

  return <BaseNode {...props} data={nodeData} />;
};
Then register it in nodeTypes.js:
javascriptimport { MyNode } from './MyNode';

export const nodeTypes = {
  // ... existing nodes
  mynode: MyNode,
};
🔧 Usage
Building a Pipeline

Drag nodes from the sidebar onto the canvas
Connect nodes by dragging from output handles to input handles
Configure nodes by interacting with their content
Submit pipeline to analyze structure

Text Node Variables
Use the special {{ variableName }} syntax in text nodes:
Hello {{ userName }}, you have {{ messageCount }} new messages!
This automatically creates two input handles: userName and messageCount.
API Endpoints
GET /
Health check endpoint
Response:
json{
  "status": "ok",
  "message": "Pipeline API is running"
}
POST /pipelines/parse
Analyze pipeline structure
Request:
json{
  "nodes": [
    {
      "id": "node_1",
      "type": "text",
      "data": {},
      "position": { "x": 100, "y": 100 }
    }
  ],
  "edges": [
    {
      "id": "edge_1",
      "source": "node_1",
      "target": "node_2"
    }
  ]
}
Response:
json{
  "num_nodes": 5,
  "num_edges": 4,
  "is_dag": true
}
📊 Performance & Metrics
Code Reduction
MetricBeforeAfterReductionLines per node~150~3080%Total code (4 nodes)60017071.7%New node development1-2 hours10-15 min87.5%
Algorithm Complexity

DAG Detection: O(V + E) using Kahn's algorithm
Node Rendering: O(n) where n is number of nodes
Handle Creation: O(h) where h is number of handles

