import toml


def pyproject_decode(data):
    parsed_toml = toml.loads(data)
    res = dict()
    # print(parsed_toml)
    res["dependencies"] = parsed_toml["tool"]["poetry"]["dependencies"]
    res["dev-dependencies"] = parsed_toml["tool"]["poetry"]["dev-dependencies"]
    if "python" in res["dependencies"]:
        res["dependencies"].pop("python")
    return res


def pyproject_encode(data):
    res = dict()
    res["tool"] = dict()
    res["tool"]["poetry"] = dict()
    res["tool"]["poetry"]["dependencies"] = dict()

    for i in data["dependencies"]:
        res["tool"]["poetry"]["dependencies"][i] = data["dependencies"][i]

    new_toml = toml.dumps(res)
    return new_toml
