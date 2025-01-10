# write tests for transcribe functions
import pytest

from seqparser import (
        transcribe,
        reverse_transcribe)

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    # Correct examples
    in_seq = "ACTGAACCC"
    out_seq = "UGACUUGGG"
    assert transcribe(in_seq) == out_seq

    # Edge Case: Empty sequence (should raise an error)
    with pytest.raises(ValueError):
        transcribe("")

    # Edge Case: Sequence with spaces (should raise an error)
    with pytest.raises(ValueError):
        transcribe("ACT GAACCC")

    # Edge Case: Sequence with an invalid character (should raise an error)
    with pytest.raises(ValueError):
        transcribe("HITASXOXO") # Invalid characters

def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    # Correct examples
    in_seq = "ACTGAACCC"
    out_seq = "GGGUUCAGU"
    assert reverse_transcribe(in_seq) == out_seq

    # Edge Case: Empty sequence (should raise an error)
    with pytest.raises(ValueError):
        reverse_transcribe("")

    # Edge Case: Sequence with spaces (should raise an error)
    with pytest.raises(ValueError):
        reverse_transcribe("ACT GAACCC")

    # Edge Case: Sequence with an invalid character (should raise an error)
    with pytest.raises(ValueError):
        reverse_transcribe("HITONY") # Invalid characters