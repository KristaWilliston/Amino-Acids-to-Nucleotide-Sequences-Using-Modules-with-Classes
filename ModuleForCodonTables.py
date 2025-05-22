from MyDNAStuff import DNASeq
from codon_table import codon_table
import sys

if len(sys.argv) < 3:
    print("Require codon table and DNA sequence on command-line.")
    sys.exit(1)

# Create instances of DNASeq and codon_table
my_dna_instance = DNASeq()
codon_table_instance = codon_table()

# Read the codon table from file
codon_table_instance.read(sys.argv[1])

# Read the DNA sequence from file
my_dna_instance.read(sys.argv[2])

# Translate the sequence in all 6 reading frames
translations = codon_table_instance.translate_all_frames(my_dna_instance.seq)

for frame, seq in translations.items():
    print("Frame",frame,":",seq)
