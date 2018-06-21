import re

def splitX(txt, seps):
    default_sep = seps[0]

    # we skip seps[0] because that's the default seperator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
        outpt=tuple(i.strip() for i in txt.split(default_sep))
    return outpt

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

clean = [splitX(re.sub('[.,:*()-/|]','',i),('DBA','dba','D B A')) for i in RAW_NAMES]
print(clean)
