# Author: Sanjeev Krishnan
#
# Source of algorithms
# 1) http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/
# 2) https://github.com/lillif/stella/blob/master/stella.py
# 3) https://stackoverflow.com/questions/20872945/playfair-hillclimbing-crack

import random 
import math

# Get cipher text from the text file
def get_cipher_text(file):
    with open(file) as f:
        cipher_text = f.readline()
    return cipher_text.strip()

# Get quad-words from the text file
def get_quadgrams(file):
    quadgrams = {}
    lines = []
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        key, count = line.split(' ')
        quadgrams[key] = int(count)
    return quadgrams

# Probablitity of quadgram occuring
def probability_quadgrams(quad_counts):
    num = sum(quad_counts.values())
    quad_probabilities = {}
    for quad, freq in quad_counts.items():
        quad_probabilities[quad] = math.log10(
            float(freq)/num)  # log probabilities
    return quad_probabilities

# Score the decrypted text based on number of quads
def score_text(text, quad_probability):
    text_length = len(text)
    lowest_probability = min(quad_probability.values()) - 1
    score = 0
    for i in range(text_length - 4):
        quad = text[i:i+4]
        if quad in quad_probability:
            score += quad_probability[quad]
        else:
            score += lowest_probability
    return score

# Generate a random key 
def generate_random_key():
    key = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(key, len(key)))

# Modify a key by swapping
def modify_key(old_key):
    i = random.randrange(25)
    j = random.randrange(25)
    key_list = list(old_key)
    temp = key_list[i]
    key_list[i] = key_list[j]
    key_list[j] = temp
    new_key = ''.join(key_list)
    return new_key

# Decrypt the play-fair cipher
def decrypt_play_fair(cipher_text, key):
    l = []
    order = {}
    for k in range(25):
        order[key[k]] = k
    for i in range(0, len(cipher_text), 2):
        ord1 = order[cipher_text[i]]
        raw1 = ord1//5
        col1 = ord1 % 5
        ord2 = order[cipher_text[i+1]]
        raw2 = ord2//5
        col2 = ord2 % 5
        if raw1 == raw2:
            l.append(key[5*raw1 + (col1 + 4) % 5])
            l.append(key[5*raw2 + (col2 + 4) % 5])
        elif col1 == col2:
            l.append(key[col1 + 5*((raw1 + 4) % 5)])
            l.append(key[col2 + 5*((raw2 + 4) % 5)])
        else:
            l.append(key[5*raw1 + col2])
            l.append(key[5*raw2 + col1])
    return ''.join(l)

# Print the results
def print_results(score, i, key, text):
    print('best score so far: ' + str(score) + ', on iteration ' + str(i))
    print('Key: ' + key)
    print('plaintext: ' + text)

# Simulated annelaing decryption
def decrpyt(cipher_text, old_key=None):
    quad_counts = get_quadgrams('english_quadgrams.txt')
    quad_probability = probability_quadgrams(quad_counts)

    if(old_key != None):
        key = old_key
    else: 
        key = generate_random_key()

    plain_text = decrypt_play_fair(cipher_text, key)

    score = score_text(plain_text, quad_probability)
    best_score = score
    #print_results(score, 1, key, plain_text)

    temp = 20
    count = 10000
    step = 0.2
    while temp >= 0:
        while count > 0:
            new_key = modify_key(key)
            new_plain_text = decrypt_play_fair(cipher_text, new_key)
            new_score = score_text(new_plain_text, quad_probability)
            d_score = new_score - score
            if d_score > 0:
                key = new_key
                score = new_score
                plain_text = new_plain_text
                #print_results(score, 1, key, plain_text)
            elif temp > 0:
                probability = math.exp(d_score/temp)
                r = random.uniform(0, 1)
                if r < probability:
                    key = new_key
                    score = new_score
                    plain_text = new_plain_text
            if score >= best_score:
                best_score = score
                global best_key
                best_key = key
            count -= 1
        temp -= step
    return best_score, best_key

# main program
def main():
    cipher_text = get_cipher_text('cipher2.txt')
    random.seed()
    i = 0
    max_score = -99999
    best_key = None
    while True:
        i = i+1
        score, max_key = decrpyt(cipher_text, best_key)
        if score > max_score:
            max_score = score
            best_key = max_key
            print("current max: ", max_score)
            print("iteration: ", i)
            print("key : ", max_key)
            plainText = decrypt_play_fair(cipher_text, best_key)
            print("plainText: ", plainText)
        print("iteration : ", i)


if __name__ == '__main__':
    main()
