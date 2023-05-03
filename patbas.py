import random
import zlib

preimages = [b"r\xacN\x96\xda\xd4\xcau\xc7\x8d", b'JYr \x1b|\xa7X7&', b'\xdf\xa2&\xf0\xaavh\x07\xf4\xec']


def split_num(num):
    chars = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [str(i) for i in range(6)]
    num = (32 - len(str(bin(num))[2:])) * '0' + str(bin(num))[2:]
    return "".join([chars[int(num[i: i+5], 2)] for i in range(0, len(num), 5)])


def find_collision():
    d = {}
    for i in range(1000000):
        text = random.randbytes(10)
        ret = split_num(zlib.crc32(text))[:5]
        if ret in d:
            d[ret].append(text)
        else:
            d[ret] = [text]
    return {x: y for x, y in d.items() if len(y) > 1}

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

def generate_preimages(first_preimage):
    return [byte_xor(first_preimage, byte_xor(v[0], v[1])) for v in find_collision().values()]

for preimage in generate_preimages(preimages[0]):
    print(preimage)
    print(split_num(zlib.crc32(preimage)))
