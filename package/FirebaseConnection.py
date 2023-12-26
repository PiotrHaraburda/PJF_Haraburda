import pyrebase


class FirebaseConnection:
    def __init__(self):
        config = {"apiKey": "AIzaSyA-3TnhSy6fWy7wgIiTnUyxvo4SH5_DeVw",
                  "authDomain": "mileagemate-cdfe4.firebaseapp.com",
                  "databaseURL": "https://mileagemate-cdfe4-default-rtdb.europe-west1.firebasedatabase.app",
                  "projectId": "mileagemate-cdfe4", "storageBucket": "mileagemate-cdfe4.appspot.com",
                  "messagingSenderId": "688371519767", "appId": "1:688371519767:web:ac097913d5f51dc6146752",
                  "measurementId": "G-4D2QFK1PT6"}

        self.firebase = pyrebase.initialize_app(config)
        self.database = self.firebase.database()
