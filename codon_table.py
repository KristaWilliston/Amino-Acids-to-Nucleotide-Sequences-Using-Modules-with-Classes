class codon_table:
    def __init__(self):
        self.codons = {}
        self.init_codons = {}

    def read(self, filename):
        f = open(filename, 'r')
        data = {}
        for line in f:
            sl = line.split()
            key = sl[0]
            value = sl[2]
            data[key] = value
        f.close()

        b1 = data['Base1']
        b2 = data['Base2']
        b3 = data['Base3']
        aa = data['AAs']
        st = data['Starts']

        self.codons = {}
        self.init = {}
        for i in range(len(aa)):
            codon = b1[i] + b2[i] + b3[i]
            self.codons[codon] = aa[i]
            self.init[codon] = (st[i] == 'M')

    def amino_acid(self, codon):
        if 'N' in codon:  # Handle ambiguous codons with 'N'
            return 'X'  # Use 'X' for any ambiguous codon
        return self.codons.get(codon,'X')

    def is_init(self, codon):
        return codon in self.init_codons

    def translate(self, seq, frame=1):
        start = frame - 1
        codons = [seq[i:i+3] for i in range(start, len(seq), 3) if len(seq[i:i+3]) == 3]
        return ''.join([self.amino_acid(codon) for codon in codons])

    def translate_all_frames(self, seq):
        translations = {}
        for frame in range(1, 4):
            translations[frame] = self.translate(seq, frame)
            reverse_seq = self.reverse_complement(seq)
            translations[-frame] = self.translate(reverse_seq, frame)
        return translations

    def reverse_complement(self, seq):
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N':'N'}
        return ''.join(complement.get(base, base) for base in reversed(seq))
