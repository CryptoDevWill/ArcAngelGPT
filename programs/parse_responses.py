#parse response from server when ``` is included in response
import os
import re

def parse_python_code(match):
    if match:
        code_block = match.group(1)
        function_pattern = r"def\s+(\w+)\("
        function_match = re.search(function_pattern, code_block)
        if function_match:
            function_name = function_match.group(1)
            file_name = f"{function_name}.py"
            save_code_block(code_block, file_name)



def save_code_block(code_block, file_name):
    function_pattern = r"def\s+(\w+)\("
    function_match = re.search(function_pattern, code_block)
    if function_match:
        function_name = function_match.group(1)
        save_dir = "./user_scripts"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        file_path = os.path.join(save_dir, file_name)
        with open(file_path, "w") as f:
            f.write(code_block)
            print(f"Code block saved to {file_path}")