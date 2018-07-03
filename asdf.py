import json
import sys


data = json.load(sys.stdin)

seen_before = {}


def process_elems(elems, section=None):
    for e in elems:
        if e['model_class'] == 'ToolSection':
            process_elems(e['elems'], section=e['name'])
        elif e['model_class'][-4:] == 'Tool':
            i = e['id'].split('/')
            if len(i) > 2:
                i = '%s/%s' % (i[2], i[3])
            else:
                i = e['id']

            n = '%s|%s' % (i, e['name'])

            if n not in seen_before:
                seen_before[n] = []
            seen_before[n].append(section)


process_elems(data)

print('# Duplicate Tools')
print('')
print('Repo | Tool | Sections')
print('---- | ---- | --------')
for k, v in sorted(seen_before.items()):
    if len(v) > 1:
        j = k.split('|')
        print('%-40s | %-30s | %s' % (j[0], j[1], ', '.join(v)))
