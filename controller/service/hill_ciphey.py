from .constants import KEY_MATRIX, KEY_MATRIX_INV, BLOCK_SIZE
from .cipher_utils import clean_text, pad_text, chars_to_nums, nums_to_chars

class cypherService():
    def encoder(message: str) -> str:
        clean = clean_text(message)
        if not clean:
            return ""
        tokens = pad_text(clean, BLOCK_SIZE)
        numeric_tokens = chars_to_nums(tokens)

        encrypted_numeric = []
        for x, y, z in numeric_tokens:
            x_new = (KEY_MATRIX[0][0] * x + KEY_MATRIX[0][1] * y + KEY_MATRIX[0][2] * z) % 26
            y_new = (KEY_MATRIX[1][0] * x + KEY_MATRIX[1][1] * y + KEY_MATRIX[1][2] * z) % 26
            z_new = (KEY_MATRIX[2][0] * x + KEY_MATRIX[2][1] * y + KEY_MATRIX[2][2] * z) % 26
            encrypted_numeric.append([x_new, y_new, z_new])

        return nums_to_chars(encrypted_numeric)


    def decoder(ciphertext: str) -> str:
        clean = clean_text(ciphertext)
        if not clean:
            return ""
        tokens = pad_text(clean, BLOCK_SIZE)
        numeric_tokens = chars_to_nums(tokens)

        decrypted_numeric = []
        for x, y, z in numeric_tokens:
            x_new = (KEY_MATRIX_INV[0][0] * x + KEY_MATRIX_INV[0][1] * y + KEY_MATRIX_INV[0][2] * z) % 26
            y_new = (KEY_MATRIX_INV[1][0] * x + KEY_MATRIX_INV[1][1] * y + KEY_MATRIX_INV[1][2] * z) % 26
            z_new = (KEY_MATRIX_INV[2][0] * x + KEY_MATRIX_INV[2][1] * y + KEY_MATRIX_INV[2][2] * z) % 26
            decrypted_numeric.append([x_new, y_new, z_new])

        return nums_to_chars(decrypted_numeric)
