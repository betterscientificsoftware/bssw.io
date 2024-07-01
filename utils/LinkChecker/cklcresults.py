import ast, datetime, sys

def AddEntryToRecord(cr, key, line):
    assert key not in cr.keys(), f"duplicate key {key}, {line}, {cr}"
    cr[key] = line[11:].replace('\n','')

def StartNewRecord(cr, key, line):
    cr.clear()
    line = line[1:-2]
    AddEntryToRecord(cr, key, line)

def AddRecord(records, cr, key, line, now):
    AddEntryToRecord(cr, key, line)
    AddEntryToRecord(cr, 'Date', now)
    records.append(cr.copy())
    cr.clear()

def AppendLineToPreviousKey(cr, key, line):
    cr[key] += line

#
# Handle command-line args to this script
ghEvent = ""
if len(sys.argv) > 1:
    ghEvent = sys.argv[1]

#
# Open log and read all lines into a python list object
f = open('linkchecker-all.out','r')
lines = f.readlines()
f.close()

#
# Process contents of linkchecker log, looking for groups of lines
# defining each link tested and its results. Each link is its own dict
# object (record) and we append each record to a list named records.
#
records = []
currentRecord = {}
inRecord = False
prevKey = ''
print("Consider date resolution for PRs\n")
nowdate = datetime.datetime.now()
nowstr = ' '*11 + nowdate.strftime("%Y-%m-%d")
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
        AddRecord(records, currentRecord, key, line, nowstr)
    elif inRecord:
        AddEntryToRecord(currentRecord, key, line)

    if key != '':
        prevKey = key

#
# Open trouble_links.txt and read all contents
#
trouble_links = []
if ghEvent != "pull_request":
    with open('utils/LinkChecker/trouble_links.txt','r') as file:
        for line in file:
            trouble_links.append(ast.literal_eval(line.strip()))
trouble_links_original_size = len(trouble_links)

#
# Open bad_links.log 
#
bad_links = []
if ghEvent != "pull_request":
    with open('utils/LinkChecker/bad_links.txt','r') as file:
        for line in file:
            bad_links.append(ast.literal_eval(line.strip()))
bad_links_original_size = len(bad_links)

#
# Process all the links, looking for trouble links.
# Links that have consistently been troubled are deemed bad.
#
for r in records:

    # ignore the entry for the .md file itself
    if 'ParentURL' not in r.keys():
        continue

    linkOK = True
    if '200' not in r['Result'][:20]:
        if r['Result'][:5] == 'Valid':
            if 'Warning' in r.keys() and 'Redirected' not in r['Warning']:
                linkOK = False
        else:
            linkOK = False

    if ghEvent == "pull_request" and not linkOK:
        bad_links += [r]
        continue

    prev_trouble_records = [x for x in trouble_links if x['URL'] == r['URL']]

    if linkOK:

        #
        # If link is good, make sure any instance of it being in trouble in
        # the past is removed.
        #
        for x in prev_trouble_records:
            try:
                trouble_links.remove(x)
            except:
                pass

    else:

        if prev_trouble_records == []:
            trouble_links.append(r)
        else:
            for x in prev_trouble_records:
                date = datetime.datetime.strptime(x['Date'],'%Y-%m-%d')
                if (nowdate - date).days > 90:
                    bad_links += [x] 

#
# Sometimes, we can get duplicate entries in the lists.
# Remove any of those now.
#
trouble_links = list(set(trouble_links))
bad_links = list(set(bad_links))

#
# Update trouble_links file if modified
#
if ghEvent != 'pull_request' and len(trouble_links) != trouble_links_original_size:
    with open('utils/LinkChecker/trouble_links.txt','w') as file:
        for rec in trouble_links:
            file.write(str(rec)+'\n')

#
# Update bad_links file if modified
#
bad_links_out = 'utils/LinkChecker/bad_links.txt'
if ghEvent == 'pull_request':
    bad_links_out = 'bad_links.txt'
if len(bad_links) > bad_links_original_size:
    with open(bad_links_out, 'w') as file:
        for rec in bad_links:
            if ghEvent == 'pull_request':
                file.write(+str(rec['ParentURL'][41:]+', '+str(rec['URL']+'\n')
            else:
                file.write(str(rec)+'\n')
