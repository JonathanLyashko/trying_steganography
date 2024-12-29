from PIL import Image



# Conversion functions 
def convert_text_to_binary(rgb: str) -> list:
    binary_text = ''
    for char in rgb: 
        binary_text += format(ord(char), '08b')
    return binary_text




if __name__ == "__main__":
    TEST_MESSAGE = "This is a test. PFUDOR!"
    print(f"Original text: {TEST_MESSAGE} \nBinary text: {convert_text_to_binary(TEST_MESSAGE)}")