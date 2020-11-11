import toml

def pyproject_parse(data):
    parsed_toml = toml.loads(data)
    res = dict()
    res['dependencies'] = parsed_toml['dependencies']
    res['dev-dependencies'] = parsed_toml['dev-dependencies']
    return res
