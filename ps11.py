import random
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import time


def simulate_coupon_collector(n, num_trials=10):
   """Run num_trials simulations and return the average number of coupons needed"""
   trial_results = []
   for _ in range(num_trials):
       collected = set()
       coupons = 0
       while len(collected) < n:
           coupon = random.randint(1, n)
           collected.add(coupon)
           coupons += 1
       trial_results.append(coupons)
   return np.mean(trial_results)


# Test k values from 8 to 16 (or higher if possible)
max_k = 16  # Reduced from 20 for reasonable runtime
k_values = list(range(8, max_k + 1))
results = []
for k in k_values:
   n = 2 ** k
   avg = simulate_coupon_collector(n, num_trials=10)
   results.append((k, n, avg))
   print(f"Completed k={k}, n={n}: average coupons needed = {avg:.1f}")


# Create table
headers = ["k", "n=2^k", "Average Coupons Needed"]
table = tabulate(results, headers=headers, floatfmt=".1f")
print("\nResults Table:")
print(table)


# Create plot with n on x-axis
plt.figure(figsize=(12, 6))
n_vals = [r[1] for r in results]
avg_vals = [r[2] for r in results]


plt.plot(n_vals, avg_vals, 'bo-', label='Simulated Average')
plt.xlabel('Number of Coupon Types (n=2^k)')
plt.ylabel('Average Coupons Needed')
plt.title('Coupon Collector Problem: Average Coupons Needed vs Number of Coupon Types')


plt.legend()
plt.grid(True)
plt.xscale('log')  # Log scale for x-axis since n grows exponentially
plt.yscale('log')  # Keep y-axis log scale for better visualization


# Annotate points with k values
for k, n, avg in results:
   plt.annotate(f'k={k}', (n, avg), textcoords="offset points", xytext=(0,10), ha='center')


plt.show()

# Speed test: 100 trials with 10000 coupons
start_time = time.time()
simulate_coupon_collector(10000, num_trials=100)
end_time = time.time()
print(f"\nTime taken for 100 trials with 10000 coupons: {end_time - start_time:.2f} seconds")

