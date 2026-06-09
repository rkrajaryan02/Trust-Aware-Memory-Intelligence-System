import streamlit as st
import pandas as pd
import json

st.set_page_config(
    page_title="Trust-Aware Memory Intelligence System",
    layout="wide"
)

# ==========================
# LOAD DATA
# ==========================

with open("storage/memory_store.json", "r") as file:
    memory = json.load(file)

with open("storage/change_log.json", "r") as file:
    logs = json.load(file)

# ==========================
# TITLE
# ==========================

st.title("🧠 Trust-Aware Memory Intelligence System")

st.markdown("""
### AI-Powered Trust Memory Framework

Tracks:

- Memory Evolution
- Contradictions
- Confidence Changes
- Explainable Decisions
- Trust-Aware Reasoning
""")

# ==========================
# KPI SECTION
# ==========================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Claims Processed",
    49
)

col2.metric(
    "Memories Stored",
    len(memory)
)

col3.metric(
    "Log Entries",
    len(logs)
)

# ==========================
# STATUS OVERVIEW
# ==========================

active = sum(
    1 for m in memory
    if m["status"] == "active"
)

under_review = sum(
    1 for m in memory
    if m["status"] == "under_review"
)

forgotten = sum(
    1 for m in memory
    if m["status"] == "forgotten"
)

c1, c2, c3 = st.columns(3)

c1.metric("🟢 Active", active)
c2.metric("🟡 Under Review", under_review)
c3.metric("🔴 Forgotten", forgotten)

st.divider()

# ==========================
# DEMO FLOW
# ==========================

st.info("""
### Demo Flow

1. Claims enter the system
2. Claim Extraction Agent extracts facts
3. Verification Agent assigns confidence
4. Memory Curator detects duplicates and contradictions
5. Memory Store updates belief history
6. Change Log records actions
7. Explainer Agent provides reasoning
""")

st.divider()

# ==========================
# CONFIDENCE CHART
# ==========================

st.subheader("📊 Confidence Distribution")

chart_data = pd.DataFrame(memory)

if not chart_data.empty:

    st.bar_chart(
        chart_data.set_index("subject")["confidence"],
        height=250
    )

st.divider()

# ==========================
# SEARCH
# ==========================

search = st.text_input(
    "🔍 Search Memory",
    placeholder="Enter subject name..."
)

filtered_memory = memory

if search:

    filtered_memory = [
        m for m in memory
        if search.lower()
        in m["subject"].lower()
    ]

# ==========================
# TABS
# ==========================

tab1, tab2 = st.tabs([
    "Memory Store",
    "Change Log"
])

# ==========================
# MEMORY STORE
# ==========================

with tab1:

    st.header("Memory Store")

    st.write(
        f"Showing {len(filtered_memory)} memories"
    )

    for mem in filtered_memory:

        with st.expander(
            f"{mem['subject']} | Confidence: {mem['confidence']}"
        ):

            st.subheader("Fact")

            st.write(
                f"{mem['subject']} "
                f"{mem['predicate']} "
                f"{mem['object']}"
            )

            st.write(
                f"**Status:** {mem['status']}"
            )

            st.write(
                f"**Confidence:** {mem['confidence']}"
            )

            st.write(
                f"**Corroboration Count:** "
                f"{mem['corroboration_count']}"
            )

            st.write(
                f"**Sources:** "
                f"{', '.join(mem['sources'])}"
            )

            st.subheader("Belief History")

            for event in mem["belief_history"]:

                if event["event"] == "CONTRADICTION":

                    st.warning(
                        f"""
Claim: {event['claim_id']}

Old Value: {event['old_value']}

New Value: {event['new_value']}
"""
                    )

                else:

                    st.success(
                        f"{event['claim_id']} | "
                        f"{event['event']}"
                    )

# ==========================
# CHANGE LOG
# ==========================

with tab2:

    st.header("Change Log")

    st.json(logs)

# ==========================
# ARCHITECTURE
# ==========================

st.divider()

st.header("🏗 System Architecture")

st.markdown("""
### Workflow

Claims Dataset

⬇️

Claim Extraction Agent

⬇️

Verification Agent

⬇️

Memory Curator Agent

⬇️

Memory Store + Change Log

⬇️

Explainer Agent
""")

st.success(
    """
System supports:

✅ Stateful Memory

✅ Contradiction Detection

✅ Duplicate Detection

✅ Confidence Evolution

✅ Explainability

✅ Trust-Aware Memory Management
"""
)
