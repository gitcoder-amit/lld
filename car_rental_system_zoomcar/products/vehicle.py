from datetime import datetime

class Vehicle:
    def __init__(self, vehicle_id, vehicle_number, vehicle_type, company_name, model_name, km_driven, manufacturing_date, average, cc, daily_rental_cost, hourly_rental_cost, no_of_seat, status):
        self._vehicle_id = vehicle_id
        self._vehicle_number = vehicle_number
        self._vehicle_type = vehicle_type
        self._company_name = company_name
        self._model_name = model_name
        self._km_driven = km_driven
        self._manufacturing_date = manufacturing_date
        self._average = average
        self._cc = cc
        self._daily_rental_cost = daily_rental_cost
        self._hourly_rental_cost = hourly_rental_cost
        self._no_of_seat = no_of_seat
        self._status = status

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value

    @property
    def vehicle_number(self):
        return self._vehicle_number

    @vehicle_number.setter
    def vehicle_number(self, value):
        self._vehicle_number = value

    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value

    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        self._model_name = value

    @property
    def km_driven(self):
        return self._km_driven

    @km_driven.setter
    def km_driven(self, value):
        self._km_driven = value

    @property
    def manufacturing_date(self):
        return self._manufacturing_date

    @manufacturing_date.setter
    def manufacturing_date(self, value):
        self._manufacturing_date = value

    @property
    def average(self):
        return self._average

    @average.setter
    def average(self, value):
        self._average = value

    @property
    def cc(self):
        return self._cc

    @cc.setter
    def cc(self, value):
        self._cc = value

    @property
    def daily_rental_cost(self):
        return self._daily_rental_cost

    @daily_rental_cost.setter
    def daily_rental_cost(self, value):
        self._daily_rental_cost = value

    @property
    def hourly_rental_cost(self):
        return self._hourly_rental_cost

    @hourly_rental_cost.setter
    def hourly_rental_cost(self, value):
        self._hourly_rental_cost = value

    @property
    def no_of_seat(self):
        return self._no_of_seat

    @no_of_seat.setter
    def no_of_seat(self, value):
        self._no_of_seat = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
