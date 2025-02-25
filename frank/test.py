import os
from fast_graphrag import GraphRAG

# Define variables for GitHub projects analysis
DOMAIN = (
    "Analyze these GitHub projects to understand their architecture, key functionalities, and code structure. Focus on how modules interact, which design patterns are used, and how the project is organized."
)

EXAMPLE_QUERIES = [
    "What is the main functionality of this project?",
    "How is the project structured in terms of modules and files?",
    "Which programming languages and frameworks are predominantly used?",
    "Describe the relationships and interactions between different components.",
    "What are the key dependencies and how are they managed?"
]

ENTITY_TYPES = ["Repository", "File", "Module", "Function", "Class", "Dependency", "Framework", "Programming language"]

# Initialize the GraphRAG instance with the updated configuration
grag = GraphRAG(
    working_dir="./frank/github",
    domain=DOMAIN,
    example_queries="\n".join(EXAMPLE_QUERIES),
    entity_types=ENTITY_TYPES
)

# Loop over every .txt file in the dataset directory and insert its content into the GraphRAG database
DATASET_DIR = "./frank/dataset"

for filename in os.listdir(DATASET_DIR):
    if filename.endswith(".txt"):
        file_path = os.path.join(DATASET_DIR, filename)
        print(f"Inserting content from: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            grag.insert(content)

# New example query tuned to code analysis instead of literary analysis
print(grag.query("What is the main functionality of this project?").response)
