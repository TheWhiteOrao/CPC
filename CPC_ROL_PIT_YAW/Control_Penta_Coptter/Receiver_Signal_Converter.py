

# Receiver Signal Converter, converts the receiver signal in usable values, between a set Range

def receiver_signal_converter(receiver_signal_imput, set_lowest_output, set_highest_output, lowest_receiver_output=982, highest_receiver_output=2006):

    receiver_output_range = highest_receiver_output - lowest_receiver_output

    return (((set_highest_output - set_lowest_output) / receiver_output_range) * (receiver_output_range - (highest_receiver_output - receiver_signal_imput))) + set_lowest_output


if __name__ == '__main__':

    print(receiver_signal_converter(1494, -1, 1))
