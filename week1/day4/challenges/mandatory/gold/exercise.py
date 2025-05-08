import random

class Gene:
    def __init__(self, value=None):
        self.value = value if value is not None else random.choice([0, 1])

    def mutate(self):
        if random.random() < 0.5:
            self.value = 1 - self.value  # Flip 0 to 1 or 1 to 0

    def __repr__(self):
        return str(self.value)

class Chromosome:
    def __init__(self, genes=None, gene_length=10):
        self.genes = genes if genes else [Gene() for _ in range(gene_length)]

    def mutate(self):
        for gene in self.genes:
            gene.mutate()

    def is_all_ones(self):
        return all(gene.value == 1 for gene in self.genes)

    def __repr__(self):
        return ''.join(str(g) for g in self.genes)

class DNA:
    def __init__(self, chromosomes=None, chromosome_count=10, gene_length=10):
        self.chromosomes = chromosomes if chromosomes else [Chromosome(gene_length=gene_length) for _ in range(chromosome_count)]

    def mutate(self):
        for chromosome in self.chromosomes:
            chromosome.mutate()

    def is_all_ones(self):
        return all(chromosome.is_all_ones() for chromosome in self.chromosomes)

    def __repr__(self):
        return '\n'.join(str(c) for c in self.chromosomes)

class Organism:
    def __init__(self, dna=None, environment=0.01):
        self.dna = dna if dna else DNA()
        self.environment = environment  # Controls how often mutation happens

    def mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()

    def is_perfect(self):
        return self.dna.is_all_ones()

# Simulation
def simulate(max_generations=10000, print_every=100, mutation_rate=0.05):
    generation = 0
    org = Organism(environment=mutation_rate)

    while not org.is_perfect() and generation < max_generations:
        org.mutate()
        generation += 1
        if generation % print_every == 0:
            print(f"Generation {generation}...")

    if org.is_perfect():
        print(f"\n✅ Perfect DNA reached in {generation} generations.")
        print("Final DNA:")
        print(org.dna)
    else:
        print(f"\n Reached {max_generations} generations without perfect DNA.")

    print("Simulation complete.")

simulate()
