import binascii
import pycrc.algorithms
import time
import string
import random

crc = pycrc.algorithms.Crc(width=32, poly=0x4c11db7,
                           reflect_in=True, xor_in=0xffffffff,
                           reflect_out=True, xor_out=0xffffffff)

# your data is probably already in binary form, so you won't have to convert it again.
# data = '0'
# calculate the CRC, using the bit-by-bit-fast algorithm.
# my_crc = crc.bit_by_bit_fast(data)
# print('{:#04x}'.format(my_crc))

data = "754AB59CD91E4F1F06273DA46E58E6AE" 
md5_crc = crc.bit_by_bit_fast(str(data))
print("target: " + str(md5_crc))
data = ''.join(random.SystemRandom().choice(string.digits + string.ascii_uppercase + string.punctuation) for _ in range(random.randrange(10, 100)))
start_time = time.time()
while(1):
    my_crc = crc.bit_by_bit_fast(str(data))
    if(my_crc == md5_crc):
        print("String2 = " + data)
        print("Hash = " + '{:#04x}'.format(my_crc))
        print("Time elapsed = " + str(time.time() - start_time) + " seconds")
        break
    else:
        data = ''.join(random.SystemRandom().choice(string.digits + string.ascii_uppercase +
                                                    string.punctuation) for _ in range(random.randrange(10, 100)))
