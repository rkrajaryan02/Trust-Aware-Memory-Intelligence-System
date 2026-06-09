# 🚀 Quick Start

## 1. Clone Repository

```bash
git clone https://github.com/rkrajaryan02/Trust-Aware-Memory-Intelligence-System.git

cd Trust-Aware-Memory-Intelligence-System
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Process Claims Dataset

Run the memory pipeline:

```bash
python main.py
```

Expected Output:

```text
Processing Complete
Total Claims: 49
Total Memories: 29
Total Log Entries: 49
```

This step:

* Extracts claims
* Calculates confidence scores
* Detects duplicates
* Detects contradictions
* Updates memory store
* Updates change log

---

## 4. Run Explainability Module

To inspect a memory and understand why it is trusted:

```bash
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
- ACCEPTED (C001)
- MERGED (C002)
- CONTRADICTION (C004)
```

---

## 5. Launch Interactive Dashboard

Start Streamlit:

```bash
python -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```

Dashboard Features:

* Memory Store
* Confidence Distribution
* Search Functionality
* Change Log
* Belief History Visualization
* System Architecture View

---

# Adding New Test Cases

Open:

```text
data/claims.jsonl
```

Add a new claim in JSON format:

```json
{
  "id": "T001",
  "timestamp": "2026-06-09T10:00:00Z",
  "source_id": "TestSource",
  "source_reliability": 0.90,
  "subject": "OpenAI",
  "predicate": "released",
  "object": "GPT-5"
}
```

Save the file and rerun:

```bash
python main.py
```

The system will automatically classify the claim as:

* NEW
* DUPLICATE
* CONTRADICTION

and update the Memory Store and Change Log accordingly.

---

# Project Workflow

```text
Claims Dataset
      ↓
Claim Extraction Agent
      ↓
Verification Agent
      ↓
Memory Curator Agent
      ↓
Memory Store + Change Log
      ↓
Explainer Agent
      ↓
Streamlit Dashboard
```
