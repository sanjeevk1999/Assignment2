def decrypt(key, ciphertext):
    plain_text = ""
    for i in range(len(ciphertext)):
        plain_text += key[ciphertext[i]]
    return plain_text


text = "YOAXLAQKQGPTVWQCQXXSRXJGTQYORCRNAKQKGVNWUQRTXOQBGYVLACBTQRYWAXBVXYKGJJRRCWSRNFQWGPPYOQWGTJGVXQPQNNRXNQQLACXYRCYNDKGJJRRCWCQAYOQTGPYOQGYOQTXYGGFYOQNQRXYCGYAKQGPOQTBGACBKGJJRYOGVBOXOQNGGFQWURKFGCKQGTYSAKQKGJJRORNPOGLACBYORYYOQDSGVNWKRNNRPYQTOQTYOQNRXYYAJQXOQXRSYOQJKGJJRYOQDSQTQYTDACBYGLVYYOQWGTJGVXQACYGYOQYQRLGYWGYRYRCDTRYQANNCQMQTBGYOQTQRBRACXRAWRNAKQRXXOQLAKFQWOQTSRDYOTGVBOYOQSGGWWGYAYXYOQXYVLAWQXYYQRLRTYDAQMQTSRXRYACRNNJDNAPQHVXYRXXOQXRAWYOAXKGJJRXOQCGYAKQWYORYGCQGPYOQYTQQXORWRWGGTNQRWACBTABOYACYGAY"

key = {
    "Q": "E",  
    "Y": "T",  
    "R": "A",   
    "G": "O",    
    "O": "H",   
    "A": "I",   
    "X": "S",   
    "T": "R",  
    "C": "N",   
    "W": "D",  
    "N": "L",   
    "J": "M",  
    "K": "C",  
    "B": "G",
    "V": "U",  
    "P": "F",  
    "L": "P",  
    "S": "W",   
    "D": "Y",   
    "F": "K",   
    "U": "B",   
    "M": "V",   
    "H": "J",   
    "E": "X",   
    "Z": "Q",   
    "I": "Z"
    }

print(decrypt(key, text))
