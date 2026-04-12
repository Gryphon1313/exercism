def proteins(strand: str) -> list[str]:
    codon_to_protein = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
    }
    stop_codons = {'UAA', 'UAG', 'UGA'}

    proteins_list = []
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        if codon in stop_codons:
            break
        protein = codon_to_protein.get(codon)
        if protein:
            proteins_list.append(protein)

    return proteins_list
