import toml

def pipfile_parse(data):
    parsed_toml = toml.loads(data)
    res = dict()
    print(parsed_toml)
    #res['dependencies'] = parsed_toml['dependencies']
    #res['dev-dependencies'] = parsed_toml['dev-dependencies']
    return res
