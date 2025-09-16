from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

with open("/media/simonray/data24/data/uio_dropbox_sr/myTeaching/IKCU/IKCU_1/data/GCtest.fa") as handle:
    seq_count = 0
    gc_sum = 0.0
    for record in SeqIO.parse(handle, "fasta"):
        print(record.id)
        print( gc_fraction(record))
        seq_count += 1
        gc_sum += gc_fraction(record)

    print(gc_sum/seq_count)

