#!./venv/bin/python

import sys
import pprint

import db_table
from db_table import db_table
col = sys.argv[1].split(",")
val = sys.argv[2].split(",")

searchParms = {}

for i in range(len(val)):
    searchParms[col[i]] = val[i]

# Init the db connections
session_table = db_table("Sessions")
subsession_table = db_table("subSessions")
speaker_table = db_table("speakers")

# Find each session_id for the searched on column
results = []
if "speaker" in col:
    # use speaker table for speakers
    speakers = speaker_table.select(None, searchParms)
    for i in range(len(speakers)):
        session = session_table.select(None, {"session_id": speakers[i]['session_id']})[0]
        results.append(session)
else:
    results = session_table.select(None, searchParms)


# check each subsession for each session
for i in range(len(results)):
    result = results[i]
    session_id = result['session_id']

    subsessions = subsession_table.select(None, {"session_id": session_id})
    subsessions_list = []
    for row in subsessions:
        subsessions_list.append(row['subId'])

    if len(subsessions_list) != 0:
        newResults = session_table.select(None, None, subsessions_list)

    print(" Session:")
    pprint.pprint (result)
    if len(subsessions_list) != 0:
        print("\Sub sessions")
        pprint.pprint(newResults)

    print("=========================================")




