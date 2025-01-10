# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    # Strip and convert input sequence to uppercase
    seq = seq.strip().upper()

    # Edge Case: Empty sequence
    if not seq:
        raise ValueError("Sequence cannot be empty")

    # Edge Case: Validate input using set operations
    invalid_chars = set(seq) - ALLOWED_NUC
    if invalid_chars:
        raise ValueError(f"Invalid input characters: {', '.join(invalid_chars)}")

    # Edge Case: Sequence with spaces
    if " " in seq:
        raise ValueError("Sequence cannot contain spaces")

    # Transcribe sequence
    outseq = "".join(TRANSCRIPTION_MAPPING[bp] for bp in seq)

    # Reverse the sequence if required
    return outseq[::-1] if reverse else outseq

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # Hey this is my comment
    # Again!

    # Run transcribe function with reverse=True
    return transcribe(seq, reverse=True)
    pass

