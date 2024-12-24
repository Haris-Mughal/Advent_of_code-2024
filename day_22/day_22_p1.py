def next_secret_number(secret):
    # Step 1: Multiply by 64, mix and prune
    secret = (secret ^ (secret * 64)) % 16777216
    # Step 2: Divide by 32, mix and prune
    secret = (secret ^ (secret // 32)) % 16777216
    # Step 3: Multiply by 2048, mix and prune
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

def simulate_secrets(initial_secret, iterations):
    secret = initial_secret
    for _ in range(iterations):
        secret = next_secret_number(secret)
    return secret

def main():
    # Read the input file
    with open('day_22.in') as file:
        initial_secrets = [int(line.strip()) for line in file]

    # Simulate 2000 iterations for each initial secret
    iterations = 2000
    total_sum = 0
    for initial_secret in initial_secrets:
        final_secret = simulate_secrets(initial_secret, iterations)
        total_sum += final_secret

    # Print the result
    print(total_sum)

if __name__ == "__main__":
    main()