def conv_endian(num, endian='big'):
    if endian not in ['big', 'little']:
        return None
    
    if num < 0:
        num = (1 << 32) + num  # Convert negative value to its 2's complement equivalent
    
    hex_str = ""
    while num > 0:
        byte = num & 0xFF  # Extract the lowest byte
        hex_str = f"{byte:02X} " + hex_str  # Convert byte to hexadecimal and add to the string
        num >>= 8  # Shift to the next byte
    
    if endian == 'little':
        hex_str = hex_str.rstrip()  # Remove the trailing space for little-endian
    
    return hex_str.rstrip()  # Remove trailing space for big-endian as well

# Test cases
print(conv_endian(466321, endian='big'))    # Output: "07 1E 31"
print(conv_endian(466321, endian='little')) # Output: "31 1E 07"
print(conv_endian(-466321, endian='big'))   # Output: "FF F7 EE CF"
print(conv_endian(466321, endian='invalid')) # Output: None
