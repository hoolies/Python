from qrcode import QRCode,constants


# Function to generate a QR code with the given text
def generate_qr_code(
    text, # Text to be encoded in QR code
    # Setting up the default values for the QR code
    version = 1,
    box_size = 10,
    border = 4,
    fill_color = "black",
    back_color = "white"
    ):
    qr = QRCode(
        version = version,
        error_correction = constants.ERROR_CORRECT_L,
        box_size = box_size,
        border = border,
        image_format = 'PNG' # I want PNG format only
        )
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(
        fill_color = fill_color, 
        back_color = back_color)
    return img


def main():
    print("If you want to change the default settings run it in interactive mode.")
    text = input("Enter the text to be encoded in the QR code: ")
    generate_qr_code(text)


if __name__ == "__main__":
    main()
