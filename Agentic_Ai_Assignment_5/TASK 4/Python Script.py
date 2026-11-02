import requests
import subprocess

# Step 1: Take user input
question = input("Enter your question: ")

# Step 2: Prepare prompt for LLM
prompt = f"""
Generate ONLY valid Trino SQL query. No explanation.

Table: iceberg.sales_schema.sales
Columns: order_id, product, category, price, quantity, order_date

Task: {question}
"""

# Step 3: Call Ollama
response = subprocess.run(
    ["docker", "exec", "-i", "ollama", "ollama", "run", "qwen2.5:3b"],
    input=prompt,
    text=True,
    capture_output=True
)

sql_query = response.stdout

print("\nGenerated SQL:\n", sql_query)

# Step 4: Execute query in Trino
trino_query = sql_query.strip()

exec_query = subprocess.run(
    ["docker", "exec", "-i", "trino-coordinator", "trino"],
    input=trino_query,
    text=True,
    capture_output=True
)

print("\nQuery Result:\n", exec_query.stdout)