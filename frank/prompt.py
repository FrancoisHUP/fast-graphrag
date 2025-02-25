import os
from fast_graphrag import GraphRAG

# Updated configuration for analyzing GitHub projects
DOMAIN = (
    "Analyze these GitHub projects to understand their architecture, key functionalities, and code structure. "
    "Focus on how different modules interact, and determine if the repository contains separate backend and frontend components."
)

EXAMPLE_QUERIES = [
    "What is the main functionality of this project?",
    "How is the project structured in terms of modules and files?",
    "Does the repository contain separate backend and frontend components?",
    "Which technologies and frameworks are used in the backend?",
    "Which libraries or frameworks are used in the frontend?"
]

ENTITY_TYPES = ["Repository", "File", "Module", "Function", "Class", "Dependency", "Framework", "Backend", "Frontend"]

# Initialize the GraphRAG instance
grag = GraphRAG(
    working_dir="./frank/github",
    domain=DOMAIN,
    example_queries="\n".join(EXAMPLE_QUERIES),
    entity_types=ENTITY_TYPES
)

# (Assuming that you've already inserted all your GitHub project files into the GraphRAG database)
# Now, issue a new query asking about the repository's backend and frontend components

query_question = "Does this GitHub repository contain a backend and frontend application?"
result = grag.query(query_question)

print("Query:", query_question)
print("Response:", result.response)
