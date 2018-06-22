import re

def split(txt, seps):
    default_sep = seps[0]
    # we skip seps[0] because that's the default seperator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
        outpt=tuple(i.strip() for i in txt.split(default_sep))
    # print(txt)
    return outpt
def list_split(i):
  return split(re.sub('[.,:*()-/|]','',i),('DBA','dba','D B A'))

RAW_NAMES = [
    'SPV  Inc., DBA:   Super  Company',
    'Michael Forsky LLC d.b.a F/B Burgers .',
    '*** Youthful You Aesthetics ***',
    'Aruna Indika (dba. NGXess)',
    'Diot SA,  -  D. B. A.   *Diot-Technologies*',
    'PERFECT PRIVACY, LLC, d-b-a Perfection,',
    'PostgreSQL DB Analytics',
    '/JAYE INC/',
    ' ETABLISSEMENTS  SCHEPENS /D.B.A./ ETS_SCHEPENS',
    'DUIKERSTRAINING OOSTENDE | D.B.A.:  D.T.O. '
]

clean = [list_split(i) if len(list_split(i))>1 else (list_split(i)+('None',)) for i in RAW_NAMES]
print(clean)
