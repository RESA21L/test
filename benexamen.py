import random
import time

choices = ["Ben va corriger les examens aujourdhui", "Ben ne va pas corriger les examens aujourdhui"]

answer = random.choice(choices)
print("Est-ce que Ben corrigera les examens aujourdhui?")
time.sleep(5)

print(answer)