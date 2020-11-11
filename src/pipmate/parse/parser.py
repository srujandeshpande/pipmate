from .pyproject_decode import pyproject_decode, pyproject_encode
from .pipfile_decode import pipfile_decode, pipfile_encode
from .requirements_decode import requirements_decode, requirements_encode


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

    if sopt == 1:
        parsed_data = pyproject_decode(data)
    elif sopt == 2:
        parsed_data = pipfile_decode(data)
    elif sopt == 3:
        parsed_data = requirements_decode(data)

    if dopt == 1:
        ready_data = pyproject_encode(parsed_data)
    elif dopt == 2:
        ready_data = pipfile_encode(parsed_data)
    elif dopt == 3:
        ready_data = requirements_encode(parsed_data)

    print(ready_data)
