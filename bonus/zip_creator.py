import zipfile
import pathlib


def make_archive(files, folder):
    path = pathlib.Path(folder, "compress.zip")
    with zipfile.ZipFile(path, 'w') as archive:
        for filepath in files:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(files=["bonus1.py", "csv_exp.py"], folder="compress")