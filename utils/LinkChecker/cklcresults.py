f = open("linkchecker-all.out")
lines = f.readlines()
f.close()


#
# Parse lines for status records which like like...
#
# URL        `file:///home/runner/work/bssw.io/bssw.io/Articles/Blog/2020-01-usrse.md'
# .
# .
# .
# Result     Valid

def AddEntryToRecord(cr, key, line):
    assert key not in cr.keys(), f"duplicate key {key}, {line}, {cr}"
    cr[key] = line[11:].replace('\n','')

def StartNewRecord(cr, key, line):
    cr.clear()
    line = line[1:-2]
    AddEntryToRecord(cr, key, line)

def AddRecord(records, cr, key, line):
    AddEntryToRecord(cr, key, line)
    records.append(cr.copy())
    cr.clear()

def AppendLineToPreviousKey(cr, key, line):
    cr[key] += line

records = []
currentRecord = {}
inRecord = False
prevKey = ''
for line in lines:

    key = line[:11].replace(' ','')

    if inRecord and key == '' and prevKey != '':
        AppendLineToPreviousKey(currentRecord, prevKey, line)
    elif key == "URL":
        assert not inRecord, "Problem starting new record"
        inRecord = True
        StartNewRecord(currentRecord, key, line)
    elif key == "Result":
        assert inRecord, "Problem ending new record"
        inRecord = False
        AddRecord(records, currentRecord, key, line)
    elif inRecord:
        AddEntryToRecord(currentRecord, key, line)
    #else:
    #    print(f'Skipping "{line}"')

    if key != '':
        prevKey = key

for r in records:

    # ignore the entry for the .md file itself
    if 'ParentURL' not in r.keys():
        continue

    goodURL = True
    if '200' not in r['Result'][:20]:
        if r['Result'] == 'Valid':
            if 'Warning' in r.keys() and 'Redirected' not in r['Warning']:
                goodURL = False
        else:
            goodURL = False

    if not goodURL:
        print(f"{r['URL']} in \n\t {r['ParentURL'][41:]}")
