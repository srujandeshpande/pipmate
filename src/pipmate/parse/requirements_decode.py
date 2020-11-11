import toml

def requirements_decode(data):
    line_data = data.split('\n')
    res = dict()
    t = dict()
    #print(line_data)
    for i in line_data:
        if len(i) < 1:
            continue
        trim_line = i.strip()
        if trim_line[0] == '#':
            continue
        part_line = trim_line.split('==')
        if '#' in part_line[1]:
            part_line[1] = part_line[1].split('#')[0].strip()
        t[part_line[0]] = part_line[1]
    res['dependencies'] = t
    #res['dev-dependencies'] = parsed_toml['dev-dependencies']
    return res
