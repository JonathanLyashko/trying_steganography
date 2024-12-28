from PIL import Image



# Helper functions:
def convert_rgb_to_binary(rgb):
    # Convert an integer tuple (RGB) to a binary tuple
    bin_vals = []
    for value in rgb:
        bin_vals.append(format(value, '08b'))
    return tuple(bin_vals)


def convert_binary_to_rgb(bin_rgb):
    # Converts a binary tuple into an integer tuple (rgb)
    rgb_vals = []
    for value in bin_rgb:
        rgb_vals.append(int(value, 2))
    return tuple(rgb_vals)


def replace_least_significant_bit(og_rgb, bin_bits):
    # Replaces the least significant bit of each RGB component with a bit
    modified_rgb = []
    for i in range(3):
        new_value = og_rgb[i][:-1] + bin_bits[i]
        modified_rgb.append(new_value)
    return tuple(modified_rgb)


DELIMITER = '::END::'

def encode_message(image_path, message, output_path):
    # Encodes a text message into a picture
    img = Image.open(image_path)
    pixels = img.load()

    # Append a delimiter to the message
    message += DELIMITER
    print(f"Message to encode: {message}")

    # Convert the message to a binary format 
    binary_message = ''
    for char in message:
        binary_message += format(ord(char), '08b')
    print(f"Binary message: {binary_message}")

    width, height = img.size
    message_index = 0

    for y in range(height):
        for x in range(width):
            if message_index < len(binary_message):
                # Get the RGB values in binary format 
                current_rgb = convert_rgb_to_binary(pixels[x, y])

                # Replace least significant bits with the message bits
                new_rgb = replace_least_significant_bit(
                    current_rgb, binary_message[message_index : message_index + 3].ljust(3, '0')
                )

                # Update the pixel with the new RGB values
                pixels[x, y] = convert_binary_to_rgb(new_rgb)

                message_index += 3
    
    # Save the modified image
    img.save(output_path)
    print(f"Message encoded and saved to {output_path}")


def decode_message(image_path):
    """Decodes a text message from an image."""

    print("decode called")
    img = Image.open(image_path)
    print("Image opened")
    pixels = img.load()
    print("Pixels loaded")

    binary_message = ''

    width, height = img.size
    print(width, height)
    for y in range(height):
        for x in range(width):
            # Get the RGB values in binary format
            current_rgb = convert_rgb_to_binary(pixels[x, y])

            # Extract the least significant bits
            for value in current_rgb:
                binary_message += value[-1]
                print(value)

    print("Step one complete")

    # Convert binary data to text
    decoded_characters = []
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        decoded_characters.append(chr(int(byte, 2)))
        print(i)

    message = ''.join(decoded_characters)

    # Look for the delimiter to identify the end of the message
    delimiter_position = message.find(DELIMITER)
    if delimiter_position != -1:
        return message[:delimiter_position]
    else:
        return "No hidden message found."



# Example usage
if __name__ == "__main__":
    user_choice = input("Do you want to (e)ncode or (d)ecode a message? ").lower()
    if user_choice == 'e':
        input_image_path = input("Enter the path of the image: ")
        secret_message = input("Enter the message to encode: ")
        output_image_path = input("Enter the output image path: ")
        encode_message(input_image_path, secret_message, output_image_path)
    elif user_choice == 'd':
        input_image_path = input("Enter the path of the image to decode: ")
        print("Decoded message:", decode_message(input_image_path))
    else:
        print("Invalid choice.")

"C:/Users/lyash/Projects/trying_steganography/"