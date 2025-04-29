import random
import collections
import matplotlib.pyplot as plt

# Define the three distributions
D = {
    'D1': [(0, 0.50), (1, 0.25), (2, 0.25)],
    'D2': [(0, 0.25), (1, 0.25), (2, 0.50)],
    'D3': [(0, 1/3), (1, 1/3), (2, 1/3)]
}

def draw(dist):
    r = random.random()
    s = 0
    for v, p in dist:
        s += p
        if r <= s:
            return v

def one_trial(dist, gens=20):
    pop = 1
    for _ in range(gens):
        pop = sum(draw(dist) for _ in range(pop))
        if pop == 0:
            break
    return pop

def simulate(dist, trials=1000):
    averages = []
    for gen in range(1, 13):
        pops = []
        for _ in range(trials):
            pop = 1
            for _ in range(gen):
                pop = sum(draw(dist) for _ in range(pop))
                if pop == 0:
                    break
            pops.append(pop)
        averages.append(sum(pops) / trials)
    return averages

if __name__ == "__main__":
    random.seed(42)

    plt.figure(figsize=(8,6))

    for name, dist in D.items():
        avg_per_gen = simulate(dist)
        plt.plot(range(1, 13), avg_per_gen, label=name, marker='o')

    plt.xlabel('Generation $n$')
    plt.ylabel('Average number of nodes $\widehat{E}[X_n]$')
    plt.title('Branching Process: Average Number of Nodes per Generation')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('Figure_1.png')
    plt.show()

