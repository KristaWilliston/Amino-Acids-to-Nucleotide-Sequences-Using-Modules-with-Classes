class DNASeq:
    def __init__(self,seq="",name=""):
        self.seq = seq
        self.name = name
    def read(self,filename):
        self.seq = ''.join(open(filename).read().split())
    def reverse(self):
        return self.seq[::-1]
    def complement(self):
        d = {'A':'T','C':'G','G':'C','T':'A'}
        return ''.join(map(d.get,self.seq))
    def reverseComplement(self):
        return self.reverse().complement()
    def length(self):
        return len(self.seq)
    def freq(self,nuc):
        return self.seq.count(nuc)
    def percentGC(self):
        gccount = self.freq('C') + self.freq('G')
        return 100*float(gccount)/self.length()
    def __str__(self):
        asstr = ">"+self.name+"\n"+self.seq
        return asstr










