import scripts.FirebaseConnection


class FirebaseCRUD:
    def __init__(self):
        con = scripts.FirebaseConnection.FirebaseConnection()
        self.database = con.database

    def createData(self, first_name, login, email, age, password):
        data = {'first_name': first_name, 'login': login, 'email': email, "age": age, "password": password}
        user_id = login
        self.database.child('users').child(user_id).set(data)

    def readData(self,user_id,desired_item):
        try:
            users_info = self.database.child('users').child(user_id)
            return users_info.get().val().get(desired_item)
        except AttributeError:
            return ""

    def updateData(self):
        user_id = '1234536'
        self.database.child('users').child(user_id).update({'name': 'Mario'})

    def deleteData(self):
        user_id = '123456'
        self.database.child('users').child(user_id).remove()
