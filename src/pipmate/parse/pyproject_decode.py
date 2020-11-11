import toml

def pyproject_decode(data):
    parsed_toml = toml.loads(data)
    res = dict()
    #print(parsed_toml)
    res['dependencies'] = parsed_toml['tool']['poetry']['dependencies']
    res['dev-dependencies'] = parsed_toml['tool']['poetry']['dev-dependencies']
    if 'python' in res['dependencies']:
        res['dependencies'].pop('python')
    return res
