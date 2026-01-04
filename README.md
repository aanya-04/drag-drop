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

