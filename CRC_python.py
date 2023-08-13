def calculate_crc(data):
    crc = 0xFFFF
    polynomial = 0xA001

    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= polynomial
            else:
                crc >>= 1

    return crc

# Take input data as a space-separated string of hex values
input_data_hex = input("Enter data in hex format (e.g., 01 04 00 01 00 01): ")
data_list = [int(byte, 16) for byte in input_data_hex.split()]

crc = calculate_crc(data_list)

# Convert CRC to two bytes (MSB and LSB) and print as hexadecimal
crc_msb = (crc >> 8) & 0xFF
crc_lsb = crc & 0xFF

print("Calculated CRC:", format(crc_lsb, '02X'), format(crc_msb, '02X'))
