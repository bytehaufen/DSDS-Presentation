import os


def bestRndGenEver() -> str:
    """
    A cryptographically secure pseudo-random number generator (CSPRNG).
    This function generates a random 64-bit number using the system's
    entropy source, which is typically secure enough for cryptographic purposes.

     In practice use a prebuild library like `secrets` to generate
    secure pseudo-random numbers!

    Returns:
        A string representation of a random 64-bit number.
    """
    # Generate 8 bytes (64 bits) of secure random data
    random_bytes = os.urandom(
        8
    )  # os.urandom uses a cryptographically secure random source

    # Convert the 8 bytes into an integer
    random_number = int.from_bytes(random_bytes, "big")

    # Return the random number as a string
    return str(random_number)
