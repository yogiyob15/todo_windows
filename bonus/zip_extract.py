import zipfile

def extract_archive(archivepath, dest_path):
    with zipfile.ZipFile(archivepath, "r") as archive:
        archive.extractall(dest_path)



if __name__ == "--main__":
    extract_archive("C:\\Python\\Projects\\bonus\\compress\\compress.zip", "C:\\Python\\Projects\\bonus\\Extract")
