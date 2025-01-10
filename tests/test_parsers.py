# write tests for parsers
import pytest

from seqparser import (
        FastaParser,
        FastqParser)

def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2
        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/blank.fa
    """
    fasta = FastaParser('data/test.fa')
    seqs = [item for item in fasta]  # Collect parsed sequences

    # Assert that the first record's header is 'seq0'
    assert seqs[0][0] == "seq0", "Incorrect sequence label"

    # Assert that the first record's sequence matches the expected value
    expected_sequence = "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"
    assert seqs[0][1] == expected_sequence, "Incorrect sequence"

    # Test: Blank FASTA file (should raise ValueError due to no sequences)
    blank_fasta = FastaParser('tests/blank.fa')
    with pytest.raises(ValueError, match=r"File (.*) had 0 lines."):
        list(blank_fasta)

    # Test: Bad FASTA file (should raise ValueError due to empty line or invalid format)
    bad_fasta = FastaParser('tests/bad.fa')
    with pytest.raises(ValueError, match=r"File (.*) had 0 lines."):
        list(bad_fasta)

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # Test with a valid FASTA file
    fasta = FastaParser('data/test.fa')
    seqs = [item for item in fasta]  # Collect parsed sequences

    # Ensure the first record has a valid header
    assert seqs[0][0] is not None, "Fasta format error: first header is None"

    # Test with a FASTQ file
    fastq = FastaParser('data/test.fq')
    seqs = [item for item in fastq]

    # Ensure the first record's header is None for a FASTQ file
    assert seqs[0][0] is None, "Fasta format error: FASTQ file was not correctly identified"

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    fastq = FastqParser('data/test.fq')  # Create an instance of the parser
    seqs = [item for item in fastq]  # Collect parsed sequences and qualities

    # Assert that the first record's header is 'seq0'
    assert seqs[0][0] == "seq0", "Incorrect sequence label"

    # Assert that the first record's sequence matches the expected value
    expected_sequence = "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG"
    assert seqs[0][1] == expected_sequence, "Incorrect sequence"

    # Assert that the first record's quality matches the expected value
    expected_quality = """*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7"94(>7='(!5"2/!%"4#32="""
    assert seqs[0][2] == expected_quality, "Incorrect quality score"

    # Test: Blank FASTQ file (should raise ValueError due to no sequences)
    blank_fastq = FastqParser('tests/blank.fq')
    with pytest.raises(ValueError, match=r"File (.*) had 0 lines."):
        list(blank_fastq)

    # Test: Bad FASTQ file (should raise ValueError due to empty line or invalid format)
    bad_fastq = FastqParser('tests/bad.fq')
    with pytest.raises(ValueError, match=r"File (.*) had 0 lines."):
        list(bad_fastq)

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # Test with a valid FASTQ file
    fastq = FastqParser('data/test.fq')
    seqs = [item for item in fastq]  # Collect parsed sequences

    # Ensure the first record has a valid header
    assert seqs[0][0] is not None, "Fastq format error: first header is None"

    # Test with a FASTA file
    fasta = FastqParser('data/test.fa')
    seqs = [item for item in fasta]

    # Ensure the first record's header is None for a FASTA file
    assert seqs[0][0] is None, "Fastq format error: FASTA file was not correctly identified"