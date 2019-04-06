"""
Module minify

Creates new, minified .json or .xml files.
"""


class FileExtensionError(Exception):
    """Raised when file extension is not .json or .xml."""
    pass


def __create_new_filename(f, custom):
    """Returns new filename."""
    f_list = f.split(".")
    f_list[-1] = f"{custom}{f_list[-1]}"
    return ".".join(f_list)


def __get_file_extension(f):
    """Returns file extension."""
    return f.split(".")[-1] 


def minify(f, custom="min."):
    """
    Creates a new .json or .xml file without newlines, tabs, 
    and (most?) unnecessary whitespace.

    f: String. Name of file containing valid JSON or XML. 

    custom: Optional string. Used to create new file name. 
    "min." is the default: filename.extension becomes 
    filename.min.extension.

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
        new_f = __create_new_filename(f, custom)
        with open(new_f, "w") as min_f:
            for line in data:
                for char in chars:
                    line = line.split(char)
                    for i, section in enumerate(line):
                        line[i] = section.strip()
                    line = char.join(line)
                min_f.write(line)
