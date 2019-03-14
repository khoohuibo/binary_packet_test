import struct
#values = [1,126,200,300,400,500,600,2463452]
#template = [1,8,8,16,16,16,16,32]
values = [1,255,200,15,
          15,255,255,255,
          255,255,255,255,
          65535,65535,65535,15,
          255,65535,15,255,
          4294967295,1,4294967295,3,
          1,1,1,1,
          1,1,1,0,0,
          0,0,0,0,
          1,1,1,32432546]
template = [1,8,8,4,4,8,8,8,8,8,8,8,16,16,16,4,8,16,4,8,32,1,32,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,32] 

def write_to_binary(values, internal_template_list):
    print(values)
    print(len(values))
    print(len(internal_template_list))
    sum = 0
    internal_list = []
    counter_list = []
    #internal_template_list = [1,8,8,4,4, #41 parameters
    #8,8,8,8,8,
    #8,8,16,16,16,
    #4,8,16,4,8,
    #32,1,32,2,1,
    #1,1,1,1,1,1,
    #1,1,1,1,1,
    #1,1,1,1,32] #power_rail_4 is missing from configuration file spreadsheet

    internal_bytes = bytearray()
    
    for i in internal_template_list:
        sum = sum + i

    print(sum)
    for i in values:
        if (isinstance(i, str)):
            if i == "on":
                internal_list.append(1)
            elif i == "off":

                internal_list.append(0)
            else:
                new_f = float(i) #rounding error here
                new_i = int(new_f)
                internal_list.append(new_i)
        elif(isinstance(i, int)):
            internal_list.append(i)
        else:
            raise Exception("Unknown Type Error")

    print(internal_list)
    for counter in range(0, len(internal_list)):
        print("The Counter is: {}".format(counter))
        print("Number of bits: {}".format(internal_template_list[counter]))
        print("Value: {}".format(values[counter]))
        if internal_template_list[counter] <= 8:
            internal_bytes.append(internal_list[counter])
            print(internal_bytes[len(internal_bytes)-1])
        elif internal_template_list[counter] > 8:
            bit_counter = int(internal_template_list[counter]/8)
            print("Larger than 255 value encountered. Value is {}, attempting to convert to bytes. Template bits length is {}".format(internal_list[counter], internal_template_list[counter]))
            #result = internal_list[counter].to_bytes(bit_counter, 'little')
            #internal_bytes[counter:counter] = result
            #logging.debug("Output is {}".format(result))
            #logging.debug("Testing reverse: {}".format(int.from_bytes(result, 'little')))
            counter_list.append(counter)

            for i in range(1, bit_counter + 1):
                bitshift = internal_template_list[counter]-(8*i)
                result = internal_list[counter] >> (bitshift) & 0xFF
                internal_bytes.append(result)
                print("Bitshifting value of {} by {}, result is {}. New Length of Bytearray is {}".format(internal_list[counter], bitshift, result, len(internal_bytes)))
    print(internal_bytes)
    print(len(internal_bytes))
    return internal_bytes
def bytes_to_list(bytes):
    result =bytearray()

    result.append(bytes[50])
    result.append(bytes[51])
    result.append(bytes[52])
    result.append(bytes[53])
    new_result = int.from_bytes(result, byteorder='big')
    print(new_result)
    return result
bytes = write_to_binary(values, template)
bytes_to_list(bytes)
