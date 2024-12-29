from PIL import Image



# Conversion functions 
def convert_text_to_binary(rgb: str) -> list:
    binary_text = ''
    for char in rgb: 
        binary_text += format(ord(char), '08b')
    return binary_text


def convert_rgb_to_binary(rgb):
    binary_values = []
    for value in rgb:
        binary_values.append(format(value, '08b'))
    return tuple(binary_values)


def convert_binary_to_rgb(binary_rgb):
    rgb_values = []
    for value in binary_rgb:
        rgb_values.append(int(value, 2))
    return tuple(rgb_values)


# Testing usage
if __name__ == "__main__":
    TEST_MESSAGE = "This is a test. PFUDOR!"
    print(f"Original text: {TEST_MESSAGE} \nBinary text: {convert_text_to_binary(TEST_MESSAGE)} \n")

    TEST_RGB = (109, 57, 255)
    print(f"Original RGB: {TEST_RGB} \nBinary RGB: {convert_rgb_to_binary(TEST_RGB)} \n")

    TEST_BINARY_RGB = ('10010011', '01011100', '11101001')
    print(f"Original binary RGB: {TEST_BINARY_RGB} \nInt RGB: {convert_binary_to_rgb(TEST_BINARY_RGB)} \n")

    