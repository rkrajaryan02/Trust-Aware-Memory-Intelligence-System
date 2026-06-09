from utils.normalizer import normalize_text


def check_memory(memory, claim):

    claim_object = normalize_text(
        claim["object"]
    )

    for entry in memory:

        memory_object = normalize_text(
            entry["object"]
        )

        if (
            entry["subject"] == claim["subject"]
            and entry["predicate"] == claim["predicate"]
            and memory_object == claim_object
        ):
            return "DUPLICATE", entry

        if (
            entry["subject"] == claim["subject"]
            and entry["predicate"] == claim["predicate"]
            and memory_object != claim_object
        ):
            return "CONTRADICTION", entry

    return "NEW", None