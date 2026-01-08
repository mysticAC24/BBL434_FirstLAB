import sys

def read_fasta_sequence(fasta_file):
    seq = []
    with open(fasta_file, 'r') as f:
        for line in f:
            if not line.startswith('>'):
                seq.append(line.strip().upper())
    return ''.join(seq)

def unique_kmer_count(sequence, k=3):
    kmers = set()
    for i in range(len(sequence) - k + 1):
        kmers.add(sequence[i:i+k])
    return len(kmers)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python unique_3mer.py <seq.fa>")
        sys.exit(1)

    fasta_path = sys.argv[1]
    sequence = read_fasta_sequence(fasta_path)

    count = unique_kmer_count(sequence, k=3)
    print(f"Unique 3-mer count: {count}")
