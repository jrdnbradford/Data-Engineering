"""
Module minify

Creates new, minified .json or .xml files.
"""


class FileExtensionError(Exception):
    """Custom exception inheriting from base class."""
    pass


def __create_new_filename(f, custom):
    """Returns new filename."""
    f_path = f.split("/")
    f_dirs = f_path[0] if len(f_path[:-1]) == 1 else "/".join(f_path[:-1])
    f_full_name = f_path[len(f_path) - 1]
    f_split = f_full_name.split(".")
    f_short_name = ".".join(f_split[:-1])
    f_ext = f_split[len(f_split) - 1]   
    return f"{f_dirs}/{f_short_name}{custom}.{f_ext}"


def __get_file_extension(f):
    """Returns file extension."""
    f_split = f.split(".")
    f_ext = f_split[len(f_split) - 1]
    return f_ext


def minify(f):
    """
    Creates a new .json or .xml file without newlines, tabs, 
    and (most?) unnecessary whitespace.

    f: String. Name of file containing valid JSON or XML. 

    If file extension is not .json or .xml, FileExtensionError
    is raised.
    """
    f_ext = __get_file_extension(f)
    if f_ext == "xml": 
        chars = ["<", ">"]
    elif f_ext == "json":
        chars = [":", "\""]
    else:
        raise FileExtensionError(f"File extension must be .json or .xml, not .{f_ext}")
    
    with open(f, "r") as data:
        new_f = __create_new_filename(f, ".min")
        with open(new_f, "w") as min_f:
            for line in data:
                for char in chars:
                    line = line.split(char)
                    for i, section in enumerate(line):
                        line[i] = section.strip()
                    line = char.join(line)
                min_f.write(line)
