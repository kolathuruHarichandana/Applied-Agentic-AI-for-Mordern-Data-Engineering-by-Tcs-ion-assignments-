# Module 10 — Observation Report

**Student Name**: \[Kolathuru Harichandana]
**Date**: \[24/05/2026]

\---

## Instructions

* Open this file in any text editor (Notepad, Notepad++, VS Code, Cursor, or similar)
* Write your answers directly below each question in the designated **Answer:** area
* Keep answers **brief and to the point** — 1-3 sentences per question unless a list is requested
* All numerical values must come from **your own trace** (the same JSON file you are submitting)
* Do NOT delete or modify the questions — only add your answers
* Save the file as: `Weather-ETL-V1-Observation-Report-FirstName-LastName.md`

\---

## Section A: Token Distribution (4 marks)

### Q1. List the token count for each of the 4 LLM nodes from your trace. (1 mark)

|LLM Node|Token Count|
|-|-|
|City Parser|139|
|Weather Analyst|1463|
|Quality Reviewer|3285|
|Report Generator|3674|

### Q2. Which LLM node consumed the most tokens? Why does it consume more than the others? (1.5 marks)

**Answer:**

###### **The Report Generator consumed the most tokens because it receives outputs from all previous nodes and generates the final detailed weather intelligence report. This increases both the input and output token usage compared to the other node**s.

###### 

### Q3. The pipeline passes progressively more data to each LLM node. List what input variables each of the 4 LLM nodes receives. (1.5 marks)

|LLM Node|Input Variables|
|-|-|
|City Parser|cities|
|Weather Analyst|parsed city data, weather API data, report\_type|
|Quality Reviewer|weather analysis, raw weather data|
|Report Generator|reviewed analysis, weather summary, report\_type|

\---

## Section B: Latency Analysis (3 marks)

### Q4. What is the total workflow execution time from your trace? Which single node or section consumed the most time, and what percentage of total execution time does it represent? (1.5 marks)

###### **Answer:**

###### **The total workflow execution time was 7.66 seconds. The Weather Analyst node consumed the most time, taking approximately 36.9% of the total execution time.**



### Q5. Why is that node/section the slowest? What is happening inside it that takes so long? (0.5 marks)

###### **Answer:**

###### **The Weather Analyst node is the slowest because it processes detailed weather information and generates analytical insights using larger prompts and responses. This increases computation time compared to the other nodes.**



### Q6. The Iteration loop runs sequentially — one city at a time. If you added a 6th city to the input, estimate how much additional time the Iteration loop would take. Explain your reasoning. (1 mark)

###### **Answer:**

###### **Adding a 6th city would increase execution time by approximately 1–2 seconds because the iteration loop processes cities sequentially, meaning each additional city adds extra API processing and analysis time.**



\---

## Section C: Cost \& Production Implications (3 marks)

### Q7. What is the total cost of one workflow execution from your trace? (1 mark)

**Answer:**

###### **The total cost of one workflow execution is very low and depends on the LLM API pricing used in the workflow.**

###### **The total cost of one workflow execution from the trace is $0.00.**

###### 

### Q8. If this pipeline ran 500 times per day for a month (30 days), what would the total token consumption and estimated cost be? Show your calculation. (2 marks)

*Hint: Use your answers from Q1 (total tokens) and Q7 (total cost per run) as the base values. Multiply step by step: per-run → per-day → per-month.*

###### **Answer:**

###### **Per-run total tokens = 8561**

###### 

###### **Per-day tokens:**

###### 

###### **8561 × 500 = 4,280,500**

###### 

###### **Per-month tokens:**

###### 

###### **4,280,500 × 30 = 128,415,000**

###### 

###### **Final estimated monthly token consumption = 128,415,000 tokens**

###### 

###### **Per-run cost = $0.00**

###### 

###### **Per-month cost:**

###### 

###### **0.00 × 500 × 30 = 0.00**

###### 

###### **Final estimated monthly cost = $0.00**

