import sys
from functools import reduce

HEX_LOOKUP = {'0': '0000',
              '1': '0001',
              '2': '0010',
              '3': '0011',
              '4': '0100',
              '5': '0101',
              '6': '0110',
              '7': '0111',
              '8': '1000',
              '9': '1001',
              'A': '1010',
              'B': '1011',
              'C': '1100',
              'D': '1101',
              'E': '1110',
              'F': '1111'}

def hex2bin(hex_str):
    b = list()
    for c in hex_str:
        b.append(HEX_LOOKUP[c])

    return ''.join(b)

def to_int(binary_string):
    return int('0b' + binary_string, 2)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def s(a):
    return sum(a)

def mul(a):
    return reduce((lambda x, y: x * y), a)

def minimum(a):
    return min(a)

def maximum(a):
    return max(a)

def gt(a):
    x = a[0]
    y = a[1]
    if x > y:
        return 1
    else:
        return 0

def lt(a):
    x = a[0]
    y = a[1]
    if x < y:
        return 1
    else:
        return 0

def eq(a):
    x = a[0]
    y = a[1]
    if x == y:
        return 1
    else:
        return 0

class Decoder:
    def __init__(self, bit_str):
        self.bit_str = bit_str
        self.operator_bits = None
        self.version_bits = None

        self.subpacket_string = None
        self.version_list = list()
        self.trailing_data = ''
        self.literal_value = None
        self.literal_bits = None
        self.length_bits = None
        self.length_value = None

        self.eval = None

    def get_version_list(self):
        return self.version_list

    def get_version(self):
        return to_int(self.bit_str[0:3])

    def get_version_bits(self):
        return self.bit_str[0:3]

    def get_type(self):
        return to_int(self.bit_str[3:6])

    def get_type_bits(self):
        return self.bit_str[3:6]

    def get_lengthtype(self):
        return to_int(self.bit_str[6])

    def get_lengthtype_bits(self):
        return self.bit_str[6]

    def get_length(self, l):
        # Return length bits as well as ptr to position in bitstr
        length = self.bit_str[7:7 + l]
        return length, 7 + l
  
    def remainder_data(self):
        return self.trailing_data

    def process(self):
        t = self.get_type()
        v = self.get_version()
        self.operator_bits = t
        self.version_bits = v

        match t:
            case 4:
                self.subpacket_string = self.bit_str[6:]

                if DEBUG:
                    print(self.bit_str)
                    print('V:', self.get_version_bits(), 'O:', self.get_type_bits(), self.subpacket_string)
                    for c in chunks(self.subpacket_string, 5):
                        print(c,)
                    print('')
                    print('--')

                # Literal Binary prepended by 1 values, last value 0
                self.version_list.append(self.get_version())
                data = self.bit_str[6:]
                start = 0
                bit_list = list()

                bit = data[start:start + 5]
                last_bit_marker = bit[0]

                while last_bit_marker != '0':
                    bit_value = bit[1:]
                    bit_list.append(bit_value)

                    start += 5
                    bit = data[start:start + 5]
                    last_bit_marker = bit[0]

                # Last Bit
                bit_value = bit[1:5]
                bit_list.append(bit_value)

                self.literal_value = to_int(''.join(bit_list))
                self.trailing_data = data[start + 5:]
                self.literal_bits = bit_list

                self.eval = self.literal_value

                if DEBUG:
                    print('BL:', self.literal_bits)
                    print('LV:', self.literal_value)
                    print('TD:', self.trailing_data)
            case _:
                # Operator

                self.version_list.append(self.get_version())
                length_type = self.get_lengthtype()
                length = 15 if length_type == 0 else 11

                self.length_bits = self.get_lengthtype_bits()
                self.length_value = length

                length_str, ptr = self.get_length(length)
                l = to_int(length_str)
                self.subpacket_string = self.bit_str[ptr:]

                if DEBUG:
                    print(self.bit_str)
                    print('V:', self.get_version_bits(), 'O:', self.get_type_bits(), 'L:', self.length_bits, 'LV:', length_str, self.subpacket_string)
                    print('V:', self.get_version(), 'O:', self.get_type(), 'L:', length, to_int(length_str), ptr)
                    print('--')

                operator = None
                operands = list()
                match t:
                    case 0:
                        operator = s
                    case 1:
                        operator = mul
                    case 2:
                        operator = minimum
                    case 3:
                        operator = maximum
                    case 5:
                        operator = gt
                    case 6:
                        operator = lt
                    case 7:
                        operator = eq

                if length == 15:
                    # Total Packet lengths
                    # Figure out how many packets by slowly parsing

                    total_package_data = self.bit_str[ptr:ptr + l]
                    tail = self.bit_str[ptr + l:]

                    if DEBUG:
                        print('subpackets', total_package_data, 'Tail', tail)
                    while len(total_package_data) > 0:
                         d3 = Decoder(total_package_data)
                         d3.process()
                         self.version_list += d3.get_version_list()
                         total_package_data = d3.remainder_data()
                         operands.append(d3.eval)
                         if DEBUG:
                             print('remainder', total_package_data)

                    self.trailing_data = tail

                elif length == 11:
                    subpackets_processed = 0
                    data = self.bit_str[ptr:]

                    while subpackets_processed < l:
                        if DEBUG:
                            print('subpackets tot', l, subpackets_processed)

                        d3 = Decoder(data)
                        d3.process()
                        self.version_list += d3.get_version_list()
                        data = d3.remainder_data()
                        subpackets_processed += 1

                        operands.append(d3.eval)

                    self.trailing_data = data

                self.eval = operator(operands)

with open('16.input.txt', 'r') as fh:

    test = 'D2FE28'
    test2 = '38006F45291200'
    test3 = 'EE00D40C823060'
    test4 = '8A004A801A8002F478'
    test5 = '620080001611562C8802118E34'
    test6 = 'C0015000016115A2E0802F182340'
    test7 = 'A0016C880162017C3686B18A3D4780'

    test8 = 'C200B40A82'
    test9 = '04005AC33890'
    test10 = '880086C3E88112'
    test11 = 'CE00C43D881120'
    test12 = 'D8005AC2A8F0'
    test13 = 'F600BC2D8F'
    test14 = '9C005AC2F8F0'
    test15 = '9C0141080250320F1802104A08'

    inputstr = fh.read().rstrip()
    global DEBUG
    DEBUG = False


    print(inputstr)
    decode3 = Decoder(hex2bin(inputstr))
    decode3.process()
    print('Eval:', decode3.eval)
