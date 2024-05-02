from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image
import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def encrypt_image(image_path, key, iv):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        encrypted_directory = os.path.join(script_dir, "encrypted_images")
        create_directory(encrypted_directory)
        file_name = os.path.splitext(os.path.basename(image_path))[0]
        encrypted_image_path = os.path.join(encrypted_directory, file_name + ".bin")

        img = Image.open(image_path)
        img_rgb = img.convert("RGB")  # Convertir la imagen a RGB

        # Convertir la imagen a bytes
        img_bytes = img_rgb.tobytes()

        # Obtener el tamaño de la imagen original
        width, height = img.size
        img_size_bytes = width.to_bytes(4, byteorder='big') + height.to_bytes(4, byteorder='big')

        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(pad(img_size_bytes + img_bytes, AES.block_size))

        with open(encrypted_image_path, "wb") as f:
            f.write(encrypted_data)
        print("Imagen encriptada guardada como:", encrypted_image_path)
        return img.size  # Devolver las dimensiones de la imagen original
    except Exception as e:
        print("Error al encriptar la imagen:", e)
        return None

def decrypt_image(encrypted_image_path, key, iv):
    try:
        decrypted_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "decrypted_images")
        create_directory(decrypted_directory)
        file_name = os.path.splitext(os.path.basename(encrypted_image_path))[0]
        decrypted_image_path = os.path.join(decrypted_directory, file_name + "_decrypted.png")

        with open(encrypted_image_path, "rb") as f:
            encrypted_data = f.read()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        # Extraer el tamaño de la imagen original
        width = int.from_bytes(decrypted_data[:4], byteorder='big')
        height = int.from_bytes(decrypted_data[4:8], byteorder='big')
        img_bytes = decrypted_data[8:]

        img_decrypted = Image.frombytes("RGB", (width, height), img_bytes)
        img_decrypted.save(decrypted_image_path)
        print("Imagen desencriptada guardada como:", decrypted_image_path)
    except Exception as e:
        print("Error al desencriptar la imagen:", e)

if __name__ == "__main__":
    # Encriptación
    image_paths = [
        "imagenes/Gato.jpeg",
        "imagenes/gato2.png",
        "imagenes/gato3.jpeg"
    ]
    key = get_random_bytes(16)
    iv = get_random_bytes(AES.block_size)
    sizes = []
    for image_path in image_paths:
        size = encrypt_image(image_path, key, iv)
        if size:
            sizes.append(size)
    print("Dimensiones de las imágenes encriptadas:", sizes)
    
    # Desencriptación
    for image_path in image_paths:
        file_name = os.path.splitext(os.path.basename(image_path))[0]
        encrypted_image_path = os.path.join("encrypted_images", file_name + ".bin")
        if os.path.exists(encrypted_image_path):
            decrypt_image(encrypted_image_path, key, iv)
        else:
            print("No se encontró la imagen encriptada para:", image_path)
