if __name__ == "__main__":
    network_add = input("Network address: ")
    host_number = int(input("Host #"))
    sub_number = int(input("Subnet #"))

    last_part = bin(host_number)[2:]
    place_for_subnet = 8 - len(last_part)
    last_of_network = int(str(bin((sub_number))) + ''.join('0' for i in range(len(last_part))), 2)
    final_network = '.'.join(network_add.split('.')[:-1]) + '.' + str(last_of_network) 

    print(f"Network: {final_network}")
    last_part_in_mask = int(''.join('1' for i in range(place_for_subnet)) + '' + ''.join('0' for i in range(len(last_part))), 2)

    final_mask = (f'255.255.255.{last_part_in_mask}')

    print(f"Mask: {final_mask}")


