
def part_one():
    file = open("input", "r")

    input_list = [line.strip() for line in file]

    file.close()

    bin_num = ''
    epsi = ''
    first_bit_one = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_bit_zero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for val in input_list:
        for i, bit in enumerate(val):
            if bit == '1':
                first_bit_one[i] += 1
            else:
                first_bit_zero[i] += 1

    for i in range(len(first_bit_one)):
        if first_bit_one[i] > first_bit_zero[i]:
            bin_num += '1'
        else:
            bin_num += '0'

    for i in range(len(first_bit_one)):
        if first_bit_one[i] < first_bit_zero[i]:
            epsi += '1'
        else:
            epsi += '0'

    bin_num = int(bin_num, 2)
    epsi = int(epsi, 2)

    print(bin_num * epsi)


def shorten_list(num, is_zero, bit):
    return num[bit] == is_zero


def part_two():
    file = open("input", "r")

    input_list = [line.strip() for line in file]
    one_list = input_list

    file.close()

    bits = len(input_list[0])
    list_len = len(input_list)

    for b in range(bits):
        one_count = 0

        for entry in one_list:
            if entry[b] == '1':
                one_count += 1

        if list_len - one_count > one_count:
            one_list = list((filter(lambda elem: shorten_list(elem, '0', b), one_list)))
        else:
            one_list = list((filter(lambda elem: shorten_list(elem, '1', b), one_list)))

        list_len = len(one_list)

        if list_len == 1:
            oxy = one_list[0]
            break

    for b in range(bits):
        one_count = 0

        for entry in input_list:
            if entry[b] == '1':
                one_count += 1

        if list_len - one_count > one_count:
            input_list = list((filter(lambda elem: shorten_list(elem, '1', b), input_list)))
        else:
            input_list = list((filter(lambda elem: shorten_list(elem, '0', b), input_list)))

        list_len = len(input_list)

        if list_len == 1:
            co2 = input_list[0]
            break

    bin_num = int(oxy, 2)
    epsi = int(co2, 2)

    print(bin_num * epsi)


if __name__ == '__main__':
    part_two()
