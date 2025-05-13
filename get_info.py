import itertools

def grade(report):
    grades = {'A': 100, 'B': 14, 'C': 6, 'D': 4, 'E': 2}
    try:
        return (10 + 1 / int(report['time'])) * grades[report['grade']]
    except ZeroDivisionError:
        return 0

def clean_info():
    reports = []
    with open('output.txt', 'r') as f:
        lines = f.readlines()  # Read all lines up front!
    for i, line in enumerate(lines):
        line = line.strip(" \n\t")
        if line == '' or line == '[' or line == ']':
            continue
        if line == '{':
            cur_dict = {}
        elif line.rstrip(',') == '}':
            reports.append(cur_dict)
        else:
            key = line.split(':')[0]
            val = "".join(list(itertools.chain.from_iterable(line.split(':')[1:])))
            val = val.replace('https//', 'https://')
            key = key.lstrip('"').rstrip('"')
            val = val.lstrip(' "').rstrip(',"')
            cur_dict[key] = val
    return reports

def get_info():
    reports = clean_info()
    species = []
    for report in reports:
        if report['name'] not in species:
            species.append(report['name'])
    
    final = []
    for specie in species:
        entries = [entry for entry in reports if entry['name'] == specie]
        entries = sorted(entries, key=lambda x: grade(x), reverse=True)
        entry = entries[0]
        entry['score'] = grade(entry)
        final.append(entry)
    return final