# 🧠 Trust-Aware Memory Intelligence System

## Overview

The Trust-Aware Memory Intelligence System is a multi-agent framework that stores, evaluates, and explains information while maintaining trust awareness.

Unlike traditional memory systems that simply store facts, this system:

* Maintains stateful memory
* Assigns confidence scores
* Detects duplicates
* Detects contradictions
* Tracks belief evolution
* Records decision history
* Provides explainable reasoning

---

# Features

✅ Stateful Memory

✅ Confidence-Based Trust Management

✅ Duplicate Detection

✅ Contradiction Detection

✅ Belief History Tracking

✅ Explainable AI Memory

✅ Change Log Tracking

✅ Memory Lifecycle Management

✅ Streamlit Dashboard

---

# Project Structure

```text
hackethon/
│
├── agents/
│   ├── claim_extractor.py
│   ├── verifier.py
│   ├── memory_curator.py
│   └── explainer.py
│
├── storage/
│   ├── memory_manager.py
│   ├── change_log_manager.py
│   ├── memory_store.json
│   └── change_log.json
│
├── data/
│   ├── claims.jsonl
│   └── schema.json
│
├── app.py
├── main.py
├── test_explainer.py
├── requirements.txt
├── PROJECT_DOCUMENTATION.md
└── README.md
```

---

# Installation

## Step 1: Clone Project

```powershell
git clone <repository_url>
cd hackethon
```

---

## Step 2: Create Virtual Environment

```powershell
python -m venv venv
```

Activate:

```powershell
venv\Scripts\activate
```

---

## Step 3: Install Dependencies

```powershell
pip install -r requirements.txt
```

---

# Running the Project

## Step 1: Clear Existing Memory (Optional)

Open:

```text
storage/memory_store.json
```

Replace contents with:

```json
[]
```

Open:

```text
storage/change_log.json
```

Replace contents with:

```json
[]
```

This ensures a clean run.

---

## Step 2: Process Claims

Run:

```powershell
python main.py
```

Expected Output:

```text
Processing Complete
Total Claims: 49
Total Memories: 29
Total Log Entries: 49
```

---

## Step 3: Test Explainability

Run:

```powershell
python test_explainer.py
```

Example Output:

```text
FACT:
Startup A raised funding of $5M in 2021

CONFIDENCE:
0.62

STATUS:
active

SUPPORTED BY:
3 claims

BELIEF HISTORY:

ACCEPTED
MERGED
MERGED
CONTRADICTION
```

---

## Step 4: Launch Dashboard

Run:

```powershell
python -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```

Dashboard Features:

* KPI Metrics
* Confidence Distribution
* Search Memory
* Memory Store
* Change Log
* Architecture View

---

# How to Add New Test Cases

Open:

```text
data/claims.jsonl
```

Add a new JSON record.

Example:

```json
{
  "id": "T001",
  "timestamp": "2026-06-09T10:00:00Z",
  "source_id": "TestSource",
  "source_reliability": 0.90,
  "verifiable": "VERIFIABLE",
  "label": "SUPPORTS",
  "claim": "OpenAI released GPT-5.",
  "subject": "OpenAI",
  "predicate": "released",
  "object": "GPT-5",
  "notes": "Test Claim"
}
```

Add it as a single line inside the `.jsonl` file.

---

# Testing New Memory Creation

Example:

```json
{
  "subject": "OpenAI",
  "predicate": "released",
  "object": "GPT-5"
}
```

Result:

```text
NEW
↓
ACCEPTED
↓
Stored in Memory Store
```

---

# Testing Duplicate Detection

Existing Memory:

```text
OpenAI released GPT-5
```

Add another claim:

```text
OpenAI released GPT-5
```

Result:

```text
DUPLICATE
↓
MERGED
↓
Confidence +0.03
↓
Corroboration Count +1
```

---

# Testing Contradiction Detection

Existing Memory:

```text
OpenAI released GPT-5
```

Add:

```text
OpenAI released GPT-6
```

Result:

```text
CONTRADICTION
↓
Confidence -0.03
↓
Belief History Updated
↓
Change Log Updated
```

---

# Confidence Calculation

Formula:

Confidence =

(0.7 × Source Reliability)

*

(0.3 × Verification Score)

Current Verification Score:

```text
0.5
```

Example:

```text
Source Reliability = 0.85

Confidence =
(0.7 × 0.85)
+
(0.3 × 0.50)

Confidence = 0.74
```

---

# Memory Lifecycle

## Active

```text
confidence >= 0.30
```

---

## Under Review

```text
confidence < 0.30
```

---

## Forgotten

```text
confidence < 0.20
```

---

# Explainability

Every memory maintains:

* Confidence
* Sources
* Corroboration Count
* Belief History

Example:

```text
ACCEPTED
MERGED
MERGED
CONTRADICTION
CONTRADICTION
```

This allows the system to explain why a memory is currently trusted.

---

# Future Enhancements

* OpenAI Integration
* Claude Integration
* LangGraph Agent Workflow
* LangChain Pipelines
* Neo4j Knowledge Graph
* PostgreSQL Storage
* Semantic Duplicate Detection
* LLM-Based Verification
* Natural Language Explanations

---

# Results

Claims Processed: 49

Unique Memories Stored: 29

Log Entries Generated: 49

---

# Requirements Fulfilled

✅ Memory Store

✅ Change Log

✅ Demonstration Flow

✅ Stateful Memory

✅ Explicit Memory Logic

✅ Explainability

✅ Duplicate Detection

✅ Contradiction Detection

✅ Confidence Evolution

✅ Belief History

✅ Trust-Aware Reasoning

✅ Memory Lifecycle Management

---

# Author

Raj Aryan

Trust-Aware Memory Intelligence System

Hackathon Project
