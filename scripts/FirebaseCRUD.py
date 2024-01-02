import scripts.FirebaseConnection
from datetime import datetime, timedelta


class FirebaseCRUD:
    def __init__(self):
        con = scripts.FirebaseConnection.FirebaseConnection()
        self.database = con.database

    def create_user(self, first_name, login, email, age, password):
        data = {'first_name': first_name, 'login': login, 'email': email, "age": age, "password": password}
        user_id = login
        self.database.child('users').child(user_id).set(data)

    def create_car_data(self,user_id,make,type,model,year):
        data = {'make': make, 'model': model, 'year': year, "type": type}
        self.database.child('users').child(user_id).child("car_data").set(data)

    def create_fuel_record(self, login, year, month, day, money_spent, liters_refueled, fuel_type, gas_station):
        data = {'year': year, 'month': month, 'day': day, "money_spent": money_spent,
                "liters_refueled": liters_refueled, "fuel_type": fuel_type, "gas_station": gas_station}
        user_id = login
        self.database.child('users').child(user_id).child('fuel_records').push(data)

    def create_service_record(self, login, year, month, day, money_spent, service_type, if_successful, repair_shop):
        data = {'year': year, 'month': month, 'day': day, "money_spent": money_spent,
                "service_type": service_type, "if_successful": if_successful, "repair_shop": repair_shop}
        user_id = login
        self.database.child('users').child(user_id).child('service_records').push(data)

    def read_user(self, user_id, desired_item):
        try:
            users_info = self.database.child('users').child(user_id)
            return users_info.get().val().get(desired_item)
        except AttributeError:
            return ""

    def read_car_data(self,user_id):
        make_info = []
        type_info = []
        model_info =[]
        year_info = []
        try:
            make_info = self.database.child('users').child(user_id).child("car_data").get().val().get("make")
            type_info = self.database.child('users').child(user_id).child("car_data").get().val().get("type")
            model_info = self.database.child('users').child(user_id).child("car_data").get().val().get("model")
            year_info = self.database.child('users').child(user_id).child("car_data").get().val().get("year")
        except AttributeError:
            return make_info,type_info,model_info,year_info

        return make_info,type_info,model_info,year_info

    def read_fuel_records(self, user_id):
        year_data = []
        month_data = []
        day_data = []
        money_data = []
        liters_data = []
        fuel_data = []
        station_data = []
        try:
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
            return year_data, month_data, day_data, money_data, liters_data, fuel_data, station_data
        except TypeError:
            return year_data, month_data, day_data, money_data, liters_data, fuel_data, station_data

    def read_services_records(self, user_id):
        year_data = []
        month_data = []
        day_data = []
        money_data = []
        serviceType_data = []
        ifSuccessful_data = []
        repairShop_data = []
        try:
            for key in self.database.child('users').child(user_id).child("service_records").get().val():
                year_info = self.database.child('users').child(user_id).child("service_records").child(
                    key).get().val().get("year")
                month_info = self.database.child('users').child(user_id).child("service_records").child(
                    key).get().val().get("month")
                day_info = self.database.child('users').child(user_id).child("service_records").child(
                    key).get().val().get(
                    "day")
                money_info = self.database.child('users').child(user_id).child("service_records").child(
                    key).get().val().get("money_spent")
                serviceType_info = self.database.child('users').child(user_id).child("service_records").child(
                    key).get().val().get("service_type")
                ifSuccessful_info = self.database.child('users').child(user_id).child("service_records").child(
                    key).get().val().get("if_successful")
                repairShop_info = self.database.child('users').child(user_id).child("service_records").child(
                    key).get().val().get("repair_shop")
                year_data.append(year_info)
                month_data.append(month_info)
                day_data.append(day_info)
                money_data.append(money_info)
                serviceType_data.append(serviceType_info)
                ifSuccessful_data.append(ifSuccessful_info)
                repairShop_data.append(repairShop_info)
            return year_data, month_data, day_data, money_data, serviceType_data, ifSuccessful_data, repairShop_data
        except AttributeError:
            return year_data, month_data, day_data, money_data, serviceType_data, ifSuccessful_data, repairShop_data
        except TypeError:
            return year_data, month_data, day_data, money_data, serviceType_data, ifSuccessful_data, repairShop_data

    def read_nr_of_fuel_records(self, user_id, day, month, year):
        nr_of_fuel_records = 0
        try:
            for key in self.database.child('users').child(user_id).child("fuel_records").get().val():
                year_info = self.database.child('users').child(user_id).child("fuel_records").child(
                    key).get().val().get("year")
                month_info = self.database.child('users').child(user_id).child("fuel_records").child(
                    key).get().val().get("month")
                day_info = self.database.child('users').child(user_id).child("fuel_records").child(
                    key).get().val().get("day")

                if int(day) == int(day_info) and int(month) == int(month_info) and year == year_info:
                    nr_of_fuel_records = nr_of_fuel_records + 1
            return nr_of_fuel_records
        except AttributeError:
            return nr_of_fuel_records
        except TypeError:
            return nr_of_fuel_records

    def read_nr_of_service_records(self, user_id, day, month, year):
        nr_of_service_records = 0
        try:
            for key in self.database.child('users').child(user_id).child("service_records").get().val():
                year_info = self.database.child('users').child(user_id).child("service_records").child(
                    key).get().val().get("year")
                month_info = self.database.child('users').child(user_id).child("service_records").child(
                    key).get().val().get("month")
                day_info = self.database.child('users').child(user_id).child("service_records").child(
                    key).get().val().get("day")

                if int(day) == int(day_info) and int(month) == int(month_info) and year == year_info:
                    nr_of_service_records = nr_of_service_records + 1
            return nr_of_service_records
        except AttributeError:
            return nr_of_service_records
        except TypeError:
            return nr_of_service_records

    def read_money_spent(self, user_id):
        year_data = []
        month_data = []
        day_data = []
        money_data = []

        try:
            current_date = datetime.now()
            recent_month_limit = current_date - timedelta(days=30 * 7)  # 7 miesięcy wstecz
            service_records = self.database.child('users').child(user_id).child("service_records").get().val()
            if service_records is not None:
                for key in service_records:
                    year_info = int(self.database.child('users').child(user_id).child("service_records").child(
                        key).get().val().get("year"))
                    month_info = int(self.database.child('users').child(user_id).child("service_records").child(
                        key).get().val().get("month"))
                    day_info = int(self.database.child('users').child(user_id).child("service_records").child(
                        key).get().val().get("day"))
                    money_info = int(self.database.child('users').child(user_id).child("service_records").child(
                        key).get().val().get("money_spent"))

                    record_date = datetime(year_info, month_info, day_info)
                    if record_date >= recent_month_limit:
                        year_data.append(year_info)
                        month_data.append(month_info)
                        day_data.append(day_info)
                        money_data.append(money_info)

            fuel_records = self.database.child('users').child(user_id).child("fuel_records").get().val()
            if fuel_records is not None:
                for key in fuel_records:
                    year_info = int(self.database.child('users').child(user_id).child("fuel_records").child(
                        key).get().val().get("year"))
                    month_info = int(self.database.child('users').child(user_id).child("fuel_records").child(
                        key).get().val().get("month"))
                    day_info = int(
                        self.database.child('users').child(user_id).child("fuel_records").child(key).get().val().get(
                            "day"))
                    money_info = int(self.database.child('users').child(user_id).child("fuel_records").child(
                        key).get().val().get("money_spent"))

                    record_date = datetime(year_info, month_info, day_info)
                    if record_date >= recent_month_limit:
                        year_data.append(year_info)
                        month_data.append(month_info)
                        day_data.append(day_info)
                        money_data.append(money_info)

            return month_data, money_data

        except AttributeError:
            return month_data, money_data

    def update_user_password(self,user_id,password):
        self.database.child('users').child(user_id).update({'password': password})

    def delete_user(self, user_id):
        self.database.child('users').child(user_id).remove()
