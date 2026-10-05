VALID_PREFERENCES = [
    "chicken",
    "mutton",
    "fish",
    "prawns",
    "eggs",
    "all"
]


def validate_inputs(
    people,
    days,
    budget,
    preference
):

    if people <= 0:
        return (
            False,
            "Number of people must be greater than 0."
        )

    if people > 100:
        return (
            False,
            "Maximum supported number of people is 100."
        )

    if days <= 0:
        return (
            False,
            "Number of days must be greater than 0."
        )

    if days > 7:
        return (
            False,
            "Maximum supported duration is 7 days."
        )

    if budget <= 0:
        return (
            False,
            "Budget must be greater than 0."
        )

    if preference.lower() not in VALID_PREFERENCES:
        return (
            False,
            "Preference must be Chicken, Mutton, Fish, "
            "Prawns, Eggs or All."
        )

    return (
        True,
        "All inputs are valid."
    )