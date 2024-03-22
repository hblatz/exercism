def response(hey_bob: str) -> str:
    """ Bob only ever answers one of five things:
    * "Sure." Response to a question, ending in a ?.
    * "Calm down, I know what I'm doing!" Response to yell a question: e.g., "WHY ?"
    * "Whoa, chill out!" Response to YELL AT HIM. All caps.
    * "Fine. Be that way!" Response to silence: nothing or whitespaces.
    * "Whatever." This is what he answers to anything else. """

    hey_bob = hey_bob.strip()
    silence: bool = hey_bob == ""

    if silence:
        return "Fine. Be that way!"

    question: bool = hey_bob[-1] == '?'
    yell: bool = hey_bob.isupper()

    if question:
        if yell:
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    elif yell:
        return "Whoa, chill out!"
    else:
        return "Whatever."
