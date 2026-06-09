def extract_claim(claim):

    extracted = {
        "claim_id": claim["id"],
        "subject": claim["subject"],
        "predicate": claim["predicate"],
        "object": claim["object"],
        "timestamp": claim["timestamp"],
        "source_id": claim["source_id"],
        "source_reliability": claim["source_reliability"]
    }

    return extracted