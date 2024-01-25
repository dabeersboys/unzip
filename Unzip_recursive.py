import zipfile
import io
import os

def extract_zip(zip_data, output_dir):
    with zipfile.ZipFile(io.BytesIO(zip_data)) as zip_ref:
        zip_ref.extractall(output_dir)

def extract_nested_zips(zip_data, output_dir):
    extract_zip(zip_data, output_dir)
    with zipfile.ZipFile(io.BytesIO(zip_data)) as zip_ref:
        for member in zip_ref.namelist():
            if member.endswith('.zip'):
                nested_zip_data = zip_ref.read(member)
                nested_zip_output_dir = os.path.join(output_dir, os.path.splitext(member)[0])
                os.makedirs(nested_zip_output_dir, exist_ok=True)
                extract_nested_zips(nested_zip_data, nested_zip_output_dir)

if __name__ == "__main__":
    zip_file_path = input("Drag and drop your zip file here and remove the quotes in the file path: ")
    output_dir = input("What is the file path you want to output to?  ie C:/User/Matt/Desktop/extracted: ")
    with open(zip_file_path, 'rb') as file:
        zip_data = file.read()
        extract_nested_zips(zip_data, output_dir)


