def next_secret_number(secret):
    
    secret = (secret ^ (secret * 64)) % 16777216
    
    secret = (secret ^ (secret // 32)) % 16777216

    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

def simulate_secrets(initial_secret, iterations):
    secret = initial_secret
    for _ in range(iterations):
        secret = next_secret_number(secret)
    return secret

def main():
    with open('day_22.in') as file:
        initial_secrets = [int(line.strip()) for line in file]

    iterations = 2000
    total_sum = 0
    for initial_secret in initial_secrets:
        final_secret = simulate_secrets(initial_secret, iterations)
        total_sum += final_secret

    print(total_sum)

if __name__ == "__main__":
    main()