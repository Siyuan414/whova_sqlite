import sys
import xlrd
from db_table import db_table
from data import Session, speaker,subSession

file = sys.argv[1]
print(file)
book = xlrd.open_workbook(file)
agenda = book.sheet_by_index(0)



sessionTable = db_table("Sessions")
subSessionTbale = db_table("subSessions")
speakerTable = db_table("speakers")

parrent_id = 0
for r in range(15,agenda.nrows):
    id = r - 14
    date = str(agenda.cell_value(rowx = r, colx =0)).replace("'","")
    start = str(agenda.cell_value(rowx = r, colx =1)).replace("'","")
    end = str(agenda.cell_value(rowx = r, colx =2)).replace("'","")
    session = str(agenda.cell_value(rowx = r, colx =3)).replace("'","")
    session_title = str(agenda.cell_value(rowx= r, colx =4)).replace("'","")
    location = str(agenda.cell_value(rowx = r, colx =5)).replace("'","")
    description = str(agenda.cell_value(rowx = r, colx =6)).replace("'","")
    speakers = str(agenda.cell_value(rowx = r, colx =7)).replace("'","")

    if speakers != "":
        speakers = speakers.split("; ")
        for sp in speakers:
            speakerTable.insert(speaker.speaker(sp,id).data)
    
    if session == "Session":
        sessionTable.insert(Session.Session(date,start,end,session_title,location,description).data)
        parrent_id = id
    else:
        sessionTable.insert(Session.Session(date,start,end,session_title,location,description).data)
        subSessionTbale.insert(subSession.subSession(parrent_id,id).data)
