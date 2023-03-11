def str2byte(string):
    byte_array = string.encode()
    byte_int = int.from_bytes(byte_array, 'big')
    byte_string = bin(byte_int)
    return byte_string

def byte2str(bin_data):
    binary_int = int(bin_data, 2)
    byte_len = (binary_int.bit_length() + 7) // 8
    binary_array = binary_int.to_bytes(byte_len, 'big')
    string = binary_array.decode()
    return string

byte_str = str2byte("سلام عزیزم چطوری؟")
print(byte_str)
print(len(byte_str) - 2)

string = byte2str(byte_str)
print(string)