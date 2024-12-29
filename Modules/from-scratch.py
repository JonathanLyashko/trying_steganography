from PIL import Image

# Global variable declarations
DELIMITER = '::END::'

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


def replace_least_significant_bit(original_rgb, binary_bits):
    modified_rgb = []
    for i in range(3):
        new_value = original_rgb[i][:-2] + binary_bits[i]
        modified_rgb.append(new_value)
    return tuple(modified_rgb)


def encode_image(image_path = "C:/Users/lyash/Projects/trying_steganography/images/black_square.png", 
                 message = 'This is the default message', 
                 output_path = "C:/Users/lyash/Projects/trying_steganography/images/encoded_black_square.png"
                 ):
    
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size
    binary_message = convert_text_to_binary(message + DELIMITER)

    message_index = 0
    for y in range(height):
        for x in range(width):
            if message_index < len(binary_message):

                current_rgb = convert_rgb_to_binary(pixels[x, y])
                print(current_rgb)

                new_rgb = replace_least_significant_bit(
                    current_rgb, 
                    binary_message[message_index : message_index + 3].ljust(3, '0')
                )

                pixels[x, y] = convert_binary_to_rgb(new_rgb)

                message_index += 3
    
    img.save(output_path)
    print(f"Encoded image saved at {output_path}")
    return


def decode_message(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()


# Testing usage
if __name__ == "__main__":
    """ TEST_MESSAGE = "This is a test. PFUDOR!"
    print(f"Original text: {TEST_MESSAGE} \nBinary text: {convert_text_to_binary(TEST_MESSAGE)} \n")

    TEST_RGB = (109, 57, 255)
    print(f"Original RGB: {TEST_RGB} \nBinary RGB: {convert_rgb_to_binary(TEST_RGB)} \n")

    TEST_BINARY_RGB = ('10010011', '01011100', '11101001')
    print(f"Original binary RGB: {TEST_BINARY_RGB} \nInt RGB: {convert_binary_to_rgb(TEST_BINARY_RGB)} \n")

    TEST_BINARY_BITS = ('00', '01', '10')
    print(f"Testing bit replacement: \nOriginal binary rgb: {TEST_BINARY_RGB} \nModified binary rgb: {replace_least_significant_bit(TEST_BINARY_RGB, TEST_BINARY_BITS)}") """

    encode_image()

    