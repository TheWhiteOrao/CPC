

# Receiver Signal Converter, converts the receiver signal in usable values, between a set Range

def receiver_signal_converter(receiver_signal_imput, lowest_receiver_output=982, highest_receiver_output=2006):

    output_dir = {}

    for i in receiver_signal_imput:
        set_lowest_output = receiver_signal_imput[i][-1][0]
        set_highest_output = receiver_signal_imput[i][-1][-1]

        receiver_output_range = highest_receiver_output - lowest_receiver_output

        output_dir[i] = (((set_highest_output - set_lowest_output) / receiver_output_range) * (receiver_output_range - (highest_receiver_output - receiver_signal_imput[i][0]))) + set_lowest_output

    return output_dir


if __name__ == '__main__':

    print(receiver_signal_converter(

        {0: (982, (0, 1)), 1: (1494, (-1, 1)), 2: (1494, (-1, 1)), 3: (1494, (-1, 1))}

    ))
