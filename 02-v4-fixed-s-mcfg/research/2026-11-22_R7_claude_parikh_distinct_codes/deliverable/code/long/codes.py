RND={1: 'cfdfdeddc', 2: 'cefffdedfdc', 3: 'cefdeeefc', 4: 'cfeefedc', 5: 'cddfefffdfc', 6: 'cedfefddfc', 7: 'cfeedfeefdc', 8: 'cfeffefddfc'}
CODES={'sq':lambda s:'c'+'a'*s+'c'+'b'*(s*s)+'c',
       'exp':lambda s:'c'+'a'*s+'c'+'b'*(2**s)+'c',
       'pal':lambda s:'c'+'a'*s+'c'+'b'*(s*s)+'c'+'a'*s+'c',
       'rnd':lambda s:RND[s]}
RIG={1: 'dcdeeecde', 2: 'cddcceeeddeddc', 3: 'dceddccdc', 4: 'ceecdceee', 5: 'dccdceced', 6: 'eeedecedd', 7: 'ddcccecceedd', 8: 'ceededced'}
CODES['rig']=lambda s:RIG[s]
