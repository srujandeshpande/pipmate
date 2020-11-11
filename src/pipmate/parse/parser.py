from .pyproject_parse import pyproject_parse
from .pipfile_parse import pipfile_parse

def parse(name, dopt):
    sopt = 0
    if name[-14:] == "pyproject.toml":
        sopt = 1
    elif name[-7:] == "pipfile":
        sopt = 2
    elif name[-16:] == "requirements.txt":
        sopt = 3
    else:
        return -1

    if sopt == dopt:
        return -2

    with open(name) as file:
        data = file.read()

    if(sopt == 1):
        parsed_data = pyproject_parse(data)
    elif(sopt == 2):
        parsed_data = pipfile_parse(data)

    print(name, dopt, sopt)
