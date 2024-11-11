#!/usr/bin/env python
# example of PoW Algorithm


import hashlib
import time



max_nonce = 2 ** 32 # 4 billion
max_difficulty = 32 # from 0 to 31 bits

def proof_of_work(header, difficulty_bits):
    # calculation difficulty target
    target = 2 ** (256 - difficulty_bits)
    
    for nonce in range(max_nonce):
        hash_result = hashlib.sha256((str(header) + str(nonce)).encode('utf-8')).hexdigest()
        
        # if below the target
        if int(hash_result, 16) < target:
            return (hash_result, nonce)
    
    print("failed after %d tries" % nonce)
    return nonce
    
if __name__ == "__main__":
    nonce = 0
    hash_result = ""
    
    for difficulty_bits in range(max_difficulty):
        difficulty = 2 ** difficulty_bits
        
        print("Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits))
        
        print("Starting search: ")
        
        start_time = time.time() # checkpoint the current time
        
        # we fake a block of transactions and add the hash of previous block
        new_block = "My name is Francisco Lopez and my transactions are here" + hash_result
        
        (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)
        
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        
        print("Elapsed time: %.4f seconds" % elapsed_time)
        
        if elapsed_time > 0:
            hash_power = float(int(nonce) / elapsed_time)
            
            print("Hashing power: %ld hashes per second" % hash_power)
    
    