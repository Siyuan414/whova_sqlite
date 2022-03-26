class subSession:
    session_id = "session_id"
    subId = "subId"

    def __init__(self,session_id,subId):
        self.data = {
            self.session_id :session_id,
            self.subId: subId
        }
        
