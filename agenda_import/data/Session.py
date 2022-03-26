from turtle import title


class Session:
    id = "session_id"
    date = "date"
    start = "time_start"
    end = "time_end"
    session = "session"
    session_title = "title"
    location = "location"
    description = "description"
    speakers = "spearkers"

    def __init__(self, date,start,end,session_title,location,description):
        self.data = {
            self.date : date,
            self.start: start,
            self.end: end,
            self.session_title: title,
            self.location: location,
            self.description: description
        }


        def __res__(self):
            return "date:{}\n" \
                   "time_start{}\n" \
                    "time_end{}\n" \
                    "title{}\n" \
                    "location{}\n" \
                    "description{}\n".format(self.data.date,self.data.start,
                    self.data.end,self.data.session_title,self.data.location,self.data.description)
                    