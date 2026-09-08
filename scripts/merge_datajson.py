#!/usr/bin/env python3
"""Resolve a rebase conflict in a data.json: start from ours (upstream/main), add entries only present in theirs (branch), bump colliding 'order'."""
import json, subprocess, sys
from collections import OrderedDict
for path in sys.argv[1:]:
    ours = json.loads(subprocess.check_output(['git', 'show', f':2:{path}']), object_pairs_hook=OrderedDict)
    theirs = json.loads(subprocess.check_output(['git', 'show', f':3:{path}']), object_pairs_hook=OrderedDict)
    orders = {v.get('order') for v in ours.values() if isinstance(v, dict) and 'order' in v}
    for k, v in theirs.items():
        if k in ours: continue
        if isinstance(v, dict) and 'order' in v and v['order'] in orders:
            v['order'] = max(orders) + 1
        if isinstance(v, dict) and 'order' in v: orders.add(v['order'])
        ours[k] = v
    with open(path, 'w') as f:
        json.dump(ours, f, indent=2, ensure_ascii=False); f.write('\n')
    subprocess.check_call(['git', 'add', path])
    print('merged', path)
