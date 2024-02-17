# interpreter.py
from bp_dict import bengali_to_python_dict

def translate_to_python(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        bengali_code = file.read()

    python_code = bengali_code
    for bengali, python in bengali_to_python_dict.items():
        python_code = python_code.replace(bengali, python)

    return python_code

# Example usage
file_path = 'example.bp'  # Replace with the path to your .bp file
python_code = translate_to_python(file_path)

# print(python_code)

exec(python_code)