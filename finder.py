import hashlib
import os


def get_hash(file_path):
    hasher = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()


def find_duplicates(folder):
    hashes = {}
    duplicates = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            file_hash = get_hash(path)

            if file_hash in hashes:
                duplicates.append((hashes[file_hash], file))
            else:
                hashes[file_hash] = file

    return duplicates
