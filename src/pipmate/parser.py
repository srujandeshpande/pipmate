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
    print(name, dopt, sopt)
