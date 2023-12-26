import package.FirebaseConnection


class FirebaseCRUD:
    def __init__(self):
        con = package.FirebaseConnection.FirebaseConnection()
        self.database = con.database

    def createData(self, first_name, login, email, age, password):
        data = {'first_name': first_name, 'login': login, 'email': email, "age": age, "password": password}
        user_id = login
        self.database.child('users').child(user_id).set(data)

    def readData(self):
        user_id = '1234536'
        user_info = self.database.child('users').child(user_id).get()
        print(user_info.val())

    def updateData(self):
        user_id = '1234536'
        self.database.child('users').child(user_id).update({'name': 'Mario'})

    def deleteData(self):
        user_id = '123456'
        self.database.child('users').child(user_id).remove()
