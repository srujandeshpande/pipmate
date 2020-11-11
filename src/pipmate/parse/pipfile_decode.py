import toml


def pipfile_decode(data):
    parsed_toml = toml.loads(data)
    res = dict()
    # print(parsed_toml)
    res["dependencies"] = parsed_toml["packages"]
    res["dev-dependencies"] = parsed_toml["dev-packages"]
    return res


def pipfile_encode(data):
    res = dict()
    res["packages"] = dict()

    for i in data["dependencies"]:
        res["packages"][i] = data["dependencies"][i]

    new_toml = toml.dumps(res)
    return new_toml
