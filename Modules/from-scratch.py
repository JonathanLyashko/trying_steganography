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
        new_value = original_rgb[i][:-1] + binary_bits[i]
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

                new_rgb = replace_least_significant_bit(
                    current_rgb, 
                    binary_message[message_index : message_index + 3].ljust(3, '0')
                )

                pixels[x, y] = convert_binary_to_rgb(new_rgb)

                message_index += 3
    
    img.save(output_path)
    print(f"Encoded image saved at {output_path}")
    return


def decode_image(image_path = 'C:/Users/lyash/Projects/trying_steganography/images/encoded_black_square.png'):
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    width, height = img.size
    binary_message = ''

    for y in range(height):
        for x in range(width):

            current_rgb = convert_rgb_to_binary(pixels[x, y])

            for value in current_rgb:
                binary_message += value[-1]

    decoded_characters = []
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i : i + 8]
        decoded_characters.append(chr(int(byte, 2)))

    decoded_text = ''.join(decoded_characters)

    delimiter_position = decoded_text.find(DELIMITER)
    
    if delimiter_position != -1:
        return decoded_text[:delimiter_position]
    else:
        return "Delimiter not found. Either there is no message or the file has been corrupted."


# Testing usage
if __name__ == "__main__":
    
    using = True

    while using:
        choice = input("Do you wish to [E]ncode or [D]ecode an image?: \n").lower()

        if choice == "e":
            chosen_image_path = input("What is the input image path?: ")
            chosen_output_path = input("What is the output path?: ")
            chosen_message = input("What is the message you would like to encode?: ")

            try:
                encode_image(image_path=chosen_image_path, message=chosen_message, output_path=chosen_output_path)
            except:
                print("An error has occured and the file was not encoded. Check to make sure your inputs are correct")
        
        elif choice == "d":
            image_path = input("What is the input image path?: ")
            print(decode_image(image_path=image_path))
        
        else:
            print("Invalid choice. Please select e or d. \n")
        
        decision = input("Do you wish to restart? [Y]es or any other key to exit: ").lower()
        if decision != 'y':
            break
    
    exit()

"C:/Users/lyash/Projects/trying_steganography/images/"