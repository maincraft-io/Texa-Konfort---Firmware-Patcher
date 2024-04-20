
# Step 1: Recreate the Uncrypt Table
g_uncrypt_table = [
    36, 208, 121, 197, 229, 37, 16, 228, 142, 113,
    152, 155, 120, 99, 148, 111, 179, 189, 40, 125,
    177, 105, 136, 123, 108, 98, 124, 216, 87, 157,
    6, 81, 186, 213, 129, 156, 14, 215, 77, 130,
    30, 7, 172, 74, 174, 161, 29, 15, 173, 153,
    21, 134, 128, 92, 248, 139, 79, 167, 232, 71,
    50, 90, 80, 143, 57, 19, 227, 54, 102, 138,
    27, 72, 243, 33, 48, 63, 184, 192, 35, 65,
    166, 44, 201, 220, 114, 135, 118, 159, 42, 170,
    231, 185, 144, 209, 34, 69, 150, 84, 13, 85,
    55, 31, 219, 224, 194, 76, 86, 9, 181, 175,
    222, 73, 176, 51, 235, 249, 188, 217, 212, 183,
    28, 210, 91, 109, 101, 214, 96, 25, 205, 58,
    252, 20, 115, 38, 253, 255, 70, 43, 168, 12,
    66, 207, 247, 78, 89, 88, 245, 223, 131, 154,
    145, 151, 117, 246, 133, 97, 187, 241, 8, 254,
    211, 234, 110, 83, 26, 218, 45, 158, 182, 149,
    206, 52, 39, 107, 147, 32, 67, 0, 93, 250,
    160, 240, 238, 236, 11, 199, 230, 1, 3, 56,
    198, 22, 140, 221, 178, 68, 62, 23, 24, 106,
    237, 103, 164, 202, 5, 191, 200, 190, 244, 104,
    59, 61, 225, 193, 60, 171, 119, 17, 132, 94,
    196, 2, 49, 165, 64, 100, 126, 204, 242, 53,
    203, 4, 46, 112, 226, 141, 162, 95, 41, 137,
    116, 163, 47, 82, 233, 251, 18, 146, 10, 180,
    122, 239, 127, 195, 75, 169
]


g_crypt_table = [
    177, 187, 221, 188, 231, 204, 30, 41, 158, 107,
    248, 184, 139, 98, 36, 47, 6, 217, 246, 65,
    131, 50, 191, 197, 198, 127, 164, 70, 120, 46,
    40, 101, 175, 73, 94, 78, 0, 5, 133, 172,
    18, 238, 88, 137, 81, 166, 232, 242, 74, 222,
    60, 113, 171, 229, 67, 100, 189, 64, 129, 210,
    214, 211, 196, 75, 224, 79, 140, 176, 195, 95,
    136, 59, 71, 111, 43, 254, 105, 38, 143, 56,
    62, 31, 243, 163, 97, 99, 106, 28, 145, 144,
    61, 122, 53, 178, 219, 237, 126, 155, 25, 13,
    225, 124, 68, 201, 209, 21, 199, 173, 24, 123,
    162, 15, 233, 9, 84, 132, 240, 152, 86, 216,
    12, 2, 250, 23, 26, 19, 226, 252, 52, 34,
    39, 148, 218, 154, 51, 85, 22, 239, 69, 55,
    192, 235, 8, 63, 92, 150, 247, 174, 14, 169,
    96, 151, 10, 49, 149, 11, 35, 29, 167, 87,
    180, 45, 236, 241, 202, 223, 80, 57, 138, 255,
    89, 215, 42, 48, 44, 109, 112, 20, 194, 16,
    249, 108, 168, 119, 76, 91, 32, 156, 116, 17,
    207, 205, 77, 213, 104, 253, 220, 3, 190, 185,
    206, 82, 203, 230, 227, 128, 170, 141, 1, 93,
    121, 160, 118, 33, 125, 37, 27, 117, 165, 102,
    83, 193, 110, 147, 103, 212, 234, 66, 7, 4,
    186, 90, 58, 244, 161, 114, 183, 200, 182, 251,
    181, 157, 228, 72, 208, 146, 153, 142, 54, 115,
    179, 245, 130, 134, 159, 135
]

# Step 2: Implement the decryption function
def decrypt(buffer):
    return bytes(g_uncrypt_table[b] for b in buffer)

def read_and_decrypt_file(file_path):
    try:
        # Open and read the encrypted file
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        # Decrypt the data using the previously defined decryption function
        decrypted_data = decrypt(encrypted_data)

        # Convert bytes to string assuming UTF-8 encoding
        return decrypted_data.decode('utf-8')
    except Exception as e:
        return f"An error occurred: {e}"


g_crypt_table = [0] * 256
for index, value in enumerate(g_uncrypt_table):
    g_crypt_table[value] = index


# Step 2: Implement the encryption function
def encrypt(buffer):
    return bytes(g_crypt_table[b] for b in buffer)


# Step 3: Function to modify the version number and re-encrypt the file
def modify_and_encrypt_file(file_path, flag_name, new_version):
    try:
        # Read and decrypt the current file content
        decrypted_content = read_and_decrypt_file(file_path)
        # Modify the version number
        lines = decrypted_content.splitlines()
        updated_lines = []
        for line in lines:
            if line.startswith(f"{flag_name}="):
                updated_lines.append(f"{flag_name}={new_version}")  # Replace with new version
            else:
                updated_lines.append(line)
        modified_content = "\r\n".join(updated_lines)

        # Re-encrypt the modified content
        encrypted_data = encrypt(modified_content.encode('utf-8'))

        # Write the encrypted data back to the file
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

        return "File updated and re-encrypted successfully."
    except Exception as e:
        return f"An error occurred: {e}"

if len(sys.argv) != 2:
    print("Set the flag to enable or disable for updates!")
    sys.exit(1)

argument = sys.argv[1]
file_path = "knf_app.ini"
modify_and_encrypt_file("knf_app.ini", "flg_1", argument)
decrypted_content = read_and_decrypt_file(file_path)
print("####### Complete #######")
print((decrypted_content))
print("1) Copy your newest knf_app.ini to the firmware directory and overwrite the default.")
print("2) Upload to SD card and insert SD to your Texa Konfort 720R")
print("3) When the firmware update is complete, set the flag back to 0.")
print("4) Upload to SD card and insert SD to your Texa Konfort 720R")
print("5) Enjoy")

