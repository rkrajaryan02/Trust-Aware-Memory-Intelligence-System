import json

from agents.claim_extractor import extract_claim
from agents.verifier import verify_claim
from agents.memory_curator import check_memory

from storage.memory_manager import (
    load_memory,
    save_memory
)

from storage.change_log_manager import (
    load_logs,
    save_logs
)

# Load claims dataset
claims = []

with open("data/claims.jsonl", "r", encoding="utf-8") as file:
    for line in file:
        claims.append(json.loads(line))

# Load existing memory and logs
memory = load_memory()
logs = load_logs()

# Process all claims
for claim in claims:

    extracted = extract_claim(claim)

    verification = verify_claim(claim)

    memory_entry = {
        "subject": extracted["subject"],
        "predicate": extracted["predicate"],
        "object": extracted["object"],
        "confidence": verification["confidence"],
        "status": "active",
        "sources": [extracted["source_id"]],
        "first_seen": extracted["timestamp"],
        "last_updated": extracted["timestamp"],
        "corroboration_count": 1,

        # Belief History
        "belief_history": [
            {
                "event": "ACCEPTED",
                "claim_id": extracted["claim_id"],
                "timestamp": extracted["timestamp"]
            }
        ]
    }

    result, existing = check_memory(
        memory,
        memory_entry
    )

    # NEW FACT
    if result == "NEW":

        memory.append(memory_entry)

        logs.append({
            "claim_id": extracted["claim_id"],
            "action": "ACCEPTED",
            "reason": "New fact added to memory"
        })

    # DUPLICATE FACT
    elif result == "DUPLICATE":

        existing["corroboration_count"] += 1

        existing["confidence"] = round(
            min(
                existing["confidence"] + 0.03,
                1.0
            ),
            2
        )

        existing["belief_history"].append({
            "event": "MERGED",
            "claim_id": extracted["claim_id"],
            "timestamp": extracted["timestamp"]
        })

        logs.append({
            "claim_id": extracted["claim_id"],
            "action": "MERGED",
            "reason": "Duplicate fact found"
        })

    # CONTRADICTION
    elif result == "CONTRADICTION":

        existing["confidence"] = round(
            max(
                existing["confidence"] - 0.03,
                0
            ),
            2
        )

        # Under Review Logic
        if existing["confidence"] < 0.30:
            existing["status"] = "under_review"

        # Forgetting Logic
        if existing["confidence"] < 0.20:

            existing["status"] = "forgotten"

            logs.append({
                "claim_id": extracted["claim_id"],
                "action": "FORGOTTEN",
                "reason": "Confidence dropped below threshold"
            })

        existing["belief_history"].append({
            "event": "CONTRADICTION",
            "claim_id": extracted["claim_id"],
            "timestamp": extracted["timestamp"],
            "old_value": existing["object"],
            "new_value": memory_entry["object"]
        })

        logs.append({
            "claim_id": extracted["claim_id"],
            "action": "DOWNGRADED",
            "reason": "Contradiction detected",
            "old_value": existing["object"],
            "new_value": memory_entry["object"]
        })

# Save results
save_memory(memory)
save_logs(logs)

print("\nProcessing Complete")
print("Total Claims:", len(claims))
print("Total Memories:", len(memory))
print("Total Log Entries:", len(logs))