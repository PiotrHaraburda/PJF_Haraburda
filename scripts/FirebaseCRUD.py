import scripts.FirebaseConnection


class FirebaseCRUD:
    def __init__(self):
        con = scripts.FirebaseConnection.FirebaseConnection()
        self.database = con.database

    def createUser(self, first_name, login, email, age, password):
        data = {'first_name': first_name, 'login': login, 'email': email, "age": age, "password": password}
        user_id = login
        self.database.child('users').child(user_id).set(data)

    def createFuelRecord(self, login, year, month, day, money_spent, liters_refueled, fuel_type, gas_station):
        data = {'year': year, 'month': month, 'day': day, "money_spent": money_spent,
                "liters_refueled": liters_refueled, "fuel_type": fuel_type, "gas_station": gas_station}
        user_id = login
        self.database.child('users').child(user_id).child('fuel_records').push(data)

    def readUser(self, user_id, desired_item):
        try:
            users_info = self.database.child('users').child(user_id)
            return users_info.get().val().get(desired_item)
        except AttributeError:
            return ""

    def read_fuel_records(self, user_id):
        try:
            year_data = []
            month_data = []
            day_data = []
            money_data = []
            liters_data = []
            fuel_data = []
            station_data = []
            for key in self.database.child('users').child(user_id).child("fuel_records").get().val():
                year_info = self.database.child('users').child(user_id).child("fuel_records").child(
                    key).get().val().get("year")
                month_info = self.database.child('users').child(user_id).child("fuel_records").child(
                    key).get().val().get("month")
                day_info = self.database.child('users').child(user_id).child("fuel_records").child(key).get().val().get(
                    "day")
                money_info = self.database.child('users').child(user_id).child("fuel_records").child(
                    key).get().val().get("money_spent")
                liters_info = self.database.child('users').child(user_id).child("fuel_records").child(
                    key).get().val().get("liters_refueled")
                fuel_info = self.database.child('users').child(user_id).child("fuel_records").child(
                    key).get().val().get("fuel_type")
                station_info = self.database.child('users').child(user_id).child("fuel_records").child(
                    key).get().val().get("gas_station")
                year_data.append(year_info)
                month_data.append(month_info)
                day_data.append(day_info)
                money_data.append(money_info)
                liters_data.append(liters_info)
                fuel_data.append(fuel_info)
                station_data.append(station_info)
            return year_data, month_data, day_data, money_data, liters_data, fuel_data, station_data
        except AttributeError:
            return ""

    def read_nr_of_fuel_records(self, user_id, day, month, year):
        try:
            nr_of_fuel_records = 0
            for key in self.database.child('users').child(user_id).child("fuel_records").get().val():
                year_info = self.database.child('users').child(user_id).child("fuel_records").child(
                    key).get().val().get("year")
                month_info = self.database.child('users').child(user_id).child("fuel_records").child(
                    key).get().val().get("month")
                day_info = self.database.child('users').child(user_id).child("fuel_records").child(
                    key).get().val().get("day")

                if day == day_info and month == month_info and year == year_info:
                    nr_of_fuel_records = nr_of_fuel_records + 1
            return nr_of_fuel_records
        except AttributeError:
            return ""

    def updateUser(self):
        user_id = '1234536'
        self.database.child('users').child(user_id).update({'name': 'Mario'})

    def deleteUser(self):
        user_id = '123456'
        self.database.child('users').child(user_id).remove()
