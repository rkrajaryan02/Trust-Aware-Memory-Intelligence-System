def explain(memory):

    explanation = f"""
FACT:
{memory['subject']} {memory['predicate']} {memory['object']}

CONFIDENCE:
{memory['confidence']}

STATUS:
{memory['status']}

SUPPORTED BY:
{memory['corroboration_count']} claims

SOURCES:
{', '.join(memory['sources'])}

BELIEF HISTORY:
"""

    for event in memory["belief_history"]:

        if event["event"] == "CONTRADICTION":

            explanation += (
                f"\n- CONTRADICTION ({event['claim_id']})"
                f"\n  Old Value: {event['old_value']}"
                f"\n  New Value: {event['new_value']}"
            )

        else:

            explanation += (
                f"\n- {event['event']} ({event['claim_id']})"
            )

    return explanation