
#  ██████  ██████  ███    ██ ██    ██ ███████ ██████  ████████     ██████  ███████  ██████ ███████ ██ ██    ██ ███████ ██████      ███████ ██  ██████  ███    ██  █████  ██
# ██      ██    ██ ████   ██ ██    ██ ██      ██   ██    ██        ██   ██ ██      ██      ██      ██ ██    ██ ██      ██   ██     ██      ██ ██       ████   ██ ██   ██ ██
# ██      ██    ██ ██ ██  ██ ██    ██ █████   ██████     ██        ██████  █████   ██      █████   ██ ██    ██ █████   ██████      ███████ ██ ██   ███ ██ ██  ██ ███████ ██
# ██      ██    ██ ██  ██ ██  ██  ██  ██      ██   ██    ██        ██   ██ ██      ██      ██      ██  ██  ██  ██      ██   ██          ██ ██ ██    ██ ██  ██ ██ ██   ██ ██
#  ██████  ██████  ██   ████   ████   ███████ ██   ██    ██        ██   ██ ███████  ██████ ███████ ██   ████   ███████ ██   ██     ███████ ██  ██████  ██   ████ ██   ██ ███████


def RC(receiver_imput, Convertet_output_lowes, Convertet_output_highest, receiver_imput_lowest=982, receiver_imput_highest=2006):

    receiver_signal_range = receiver_imput_highest - receiver_imput_lowest

    return (((Convertet_output_highest - Convertet_output_lowes) / receiver_signal_range) * (receiver_signal_range - (receiver_imput_highest - receiver_imput))) + Convertet_output_lowes


if __name__ == '__main__':
    print(RC(1494, 0, 1000))
