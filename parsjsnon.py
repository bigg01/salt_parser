#sudo salt "*" state.single pkg.installed name=bash  --out json | python -c 'import json,sys;obj=json.load(sys.stdin);print obj';

import json
import sys

obj=json.load(sys.stdin)

for m in obj:
    #print(obj.get(m, {}))
    for step in obj.get(m, {}):
        ret = (obj.get(m).get(step))
        print('Minion: {} rpm: {} result: {}'.format(m, ret.get('name'), ret.get('result')))
