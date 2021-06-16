"""
typically namesake coins, genesis
"""
from hashlib import sha256
import math
MAX_NONCE = int(math.pi**620)
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transaction, previous_hash, prefix_zeros):
    for nonce in range(4300147707,MAX_NONCE):
        prefix_str = '0' * prefix_zeros
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        
        if new_hash.startswith(prefix_str):
            print(f"success :{nonce}")
            return new_hash
        if nonce == nonce:
            pass
         #   print(f'{nonce}')
        else:
            break

    raise BaseException(f"Couldn't find the correct nonce value:{nonce}")
    
if __name__ == '__main__':
	transactions = ''
	difficulty = 5
	import time
	start = time.time()
	print('fishing ...')
	new_hash = mine(5,transactions, 'zxce2594b1e263d47c37c5bd97102ae5236425d893c30979306a01b50313d888', difficulty)
	total_time = str((time.time()-start))

print(f"fishing ended, time taken :{total_time} seconds")
print(new_hash)