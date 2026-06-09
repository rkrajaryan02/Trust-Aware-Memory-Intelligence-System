def verify_claim(claim):

    source_reliability = claim["source_reliability"]

    verification_score = 0.5

    confidence = (
        0.7 * source_reliability
        +
        0.3 * verification_score
    )

    confidence = round(confidence, 2)

    return {
        "confidence": confidence
    }