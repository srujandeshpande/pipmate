import toml

def pipfile_decode(data):
    parsed_toml = toml.loads(data)
    res = dict()
    #print(parsed_toml)
    res['dependencies'] = parsed_toml['packages']
    res['dev-dependencies'] = parsed_toml['dev-packages']
    return res
