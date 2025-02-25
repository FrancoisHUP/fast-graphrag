from fast_graphrag._utils import TOKEN_TO_CHAR_RATIO
from fast_graphrag import QueryParam
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


# Query the graph with references enabled so that we get the relevant context
query_result = grag.query(
    "Does this GitHub repository contain a backend and frontend application?",
    params=QueryParam(with_references=True)
)

# Print the generated answer
print("Response:")
print(query_result.response)

# Convert the retrieved context (Consulted documents) into a human-readable string.
# Here we specify the token-to-character limits for the entities, relationships, and chunks.
context_str = query_result.context.to_str({
    "entities": 4000 * TOKEN_TO_CHAR_RATIO,
    "relationships": 3000 * TOKEN_TO_CHAR_RATIO,
    "chunks": 9000 * TOKEN_TO_CHAR_RATIO,
})

print("\nRetrieved/Consulted Documents (Context):")
print(context_str)