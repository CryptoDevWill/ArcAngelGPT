#parse response from server when ``` is included in response
import os
import re

#make list of programming languages and their extensions in a dict
programming_languages = {
    "python": "py",
    "javascript": "js",
    "typescript": "ts",
    "html": "html",
    "css": "css",
    "c": "c",
    "c++": "cpp",
    "c#": "cs",
    "java": "java",
    "kotlin": "kt",
    "ruby": "rb",
    "php": "php",
    "go": "go",
    "rust": "rs",
    "swift": "swift",
    "sql": "sql",
    "bash": "sh",
    "powershell": "ps1",
    "r": "r",
    "matlab": "m",
    "perl": "pl",
    "scala": "scala",
    "haskell": "hs",
    "lua": "lua",
    "dart": "dart",
    "elixir": "ex",
    "clojure": "clj",
    "erlang": "erl",
    "f#": "fs",
    "fortran": "f90",
    "julia": "jl",
    "json": "json",
    "lisp": "lisp",
    "pascal": "pas",
    "prolog": "pro",
    "scheme": "scm",
    "verilog": "v",
    "vhdl": "vhd",
    "vb.net": "vb"
}

def parse_code(match):
    if match:
        code_block = match.group(1)
        function_pattern = r"def\s+(\w+)\("
        function_match = re.search(function_pattern, code_block)
        if function_match:
            function_name = function_match.group(1)
        else:
            function_name = "new_program"
        language_pattern = r"(\w+)\n" # pattern to match language in backticks
        language_match = re.search(language_pattern, code_block)
        if language_match:
            language = language_match.group(1).lower() # get the language and convert to lowercase
            file_extension = programming_languages.get(language, "txt") # get the file extension from the programming_languages dict, default to "txt"
            file_name = f"{function_name}.{file_extension}"
            save_code_block(code_block, file_name)



def save_code_block(code_block, file_name):
    save_dir = "./user_scripts"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_path = os.path.join(save_dir, file_name)
    with open(file_path, "w") as f:
        f.write(code_block)
        print(f"Code block saved to {file_path}")