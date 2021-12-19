from pathlib import Path
import sys
import numpy


hex = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

operations_dict = {0: 'sum',
              1: 'product',
              2: 'minimum',
              3: 'maximum',
              4: 'literal',
              5: 'greater',
              6: 'less',
              7: 'equal'}


def read_input(input_path):
    with open(input_path, "r") as infile:
        for l in infile:
            return l


def parse_group(bits, i):
    literal_value = ''
    for _ in range(4):
        i += 1
        literal_value = literal_value + bits[i]
    return literal_value


def parse_literal_value(bits):
    i = 0
    literal_value = ''
    while i < len(bits):
        first_bit = bits[i]
        literal_value = literal_value + parse_group(bits, i)
        if first_bit == '0':
            break
        i += 5
    return int(literal_value, 2), i+5


def parse_packet_task_1(versions, values, bits, length, current):
    versions.append(int(bits[current:current+3], 2))
    type_id = int(bits[current+3:current+6], 2)
    current += 6
    if type_id == 4:
        literal_value, i = parse_literal_value(bits[current:])
        values.append(literal_value)
        current += i
        return current
    else:
        length_type_id = bits[current]
        current += 1
        if length_type_id == '0':
            length = int(bits[current:current+15], 2)
            current += 15
            while length > 0:
                new_position = parse_packet_task_1(versions, values, bits, length, current)
                length -= new_position - current
                current = new_position
            return current
        elif length_type_id == '1':
            packets_count = int(bits[current:current+11], 2)
            current += 11
            for _ in range(packets_count):
                current = parse_packet_task_1(versions, values, bits, length, current)
            return current


def parse_packet_task_2(operations, bits, length, current):
    type_id = int(bits[current+3:current+6], 2)
    current += 6
    if type_id == 4:
        literal_value, i = parse_literal_value(bits[current:])
        operations.append(literal_value)
        current += i
        return current
    else:
        current_oparation = [operations_dict[type_id]]
        length_type_id = bits[current]
        current += 1
        if length_type_id == '0':
            length = int(bits[current:current+15], 2)
            current += 15
            while length > 0:
                new_position = parse_packet_task_2(current_oparation, bits, length, current)
                length -= new_position - current
                current = new_position
            operations.append(current_oparation)
            return current
        elif length_type_id == '1':
            packets_count = int(bits[current:current+11], 2)
            current += 11
            for _ in range(packets_count):
                current = parse_packet_task_2(current_oparation, bits, length, current)
            operations.append(current_oparation)
            return current


def list_product(items):
    prod = 1
    for i in items:
        prod = prod * i
    return prod


def parse_operations(operations):

    # if only a literal is passed
    if isinstance(operations, int):
        return operations

    operation = operations[0]
    operands = []
    for i in range(1, len(operations)):
        operand = operations[i]
        if not isinstance(operand, int):
            operand = parse_operations(operand)
        operands.append(operand)

    if operation == 'sum':
        return sum(operands)
    elif operation == 'product':
        return list_product(operands)
    elif operation == 'maximum':
        return max(operands)
    elif operation == 'minimum':
        return min(operands)
    elif operation == 'greater':
        result = 1 if operands[0] > operands[1] else 0
        return result
    elif operation == 'less':
        result = 1 if operands[0] < operands[1] else 0
        return result
    elif operation == 'equal':
        result = 1 if operands[0] == operands[1] else 0

    return result


def first_task(input_path):
    input = read_input(input_path)
    hex_to_binary = []
    for char in input:
        hex_to_binary.append(hex[char])
    bits = ''.join(hex_to_binary)
    values = []
    versions = []
    parse_packet_task_1(versions, values, bits, len(bits), 0)
    print(sum(versions))


def second_task(input_path):
    input = read_input(input_path)
    hex_to_binary = []
    for char in input:
        hex_to_binary.append(hex[char])
    bits = ''.join(hex_to_binary)
    operations = []
    parse_packet_task_2(operations, bits, len(bits), 0)
    print(operations)
    result = parse_operations(operations[0])
    print(result)


if __name__ == '__main__':
    main_dir = Path(__file__).parent.resolve()
    inputs_directory = main_dir.joinpath('inputs')
    input_path = inputs_directory.joinpath('day16.txt')
    # first_task(input_path)
    second_task(input_path)
