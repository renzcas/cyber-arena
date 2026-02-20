import random
import string

def generate_fuzz_payloads(seed: str, count: int = 10):
    payloads = []

    for _ in range(count):
        noise = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        payloads.append(f"{seed}_{noise}")

    return payloads
