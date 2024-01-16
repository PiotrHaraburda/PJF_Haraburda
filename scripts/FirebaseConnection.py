import pyrebase


class FirebaseConnection:
    def __init__(self):
        config = {"apiKey": "",
                  "authDomain": "",
                  "databaseURL": "",
                  "projectId": "", "storageBucket": "",
                  "messagingSenderId": "", "appId": "",
                  "measurementId": ""}

        self.firebase = pyrebase.initialize_app(config)
        self.database = self.firebase.database()
