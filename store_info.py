
class Payment_info:
    def __init__(self, name, email, phone_number, address, address2,
                 zipcode, city, state_abbr, country, card_num, exp_month, exp_year, ccv):
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._address = address
        self._address2 = address2
        self._zipcode = zipcode
        self._city = city
        self._state_abbr = state_abbr
        self._country = country
        self._card_num = card_num
        self._exp_month = exp_month
        self._exp_year = exp_year
        self._ccv = ccv

    def __str__(self):
        return "{} {}".format(str(self._name), str(self._card_num)[-4:])

    def make_list(self):
        return [self._name, self._email, self._phone_number, self._address, self._address2,
                self._zipcode, self._city, self._state_abbr, self._country, self._card_num,
                self._exp_month, self._exp_year, self._ccv]

class Order_info:
    def __init__(self, name, type, color, size, quantity):
        self._name = name
        self._type = type
        self._color = size
        self._quantity = quantity
        self._active_state = False

    def get_type(self):
        return self._type

    def get_name(self):
        return self._name

    def get_quantity(self):
        return self._quantity
    def is_active(self):
        return self._active_state

    def set_quantity(self, qty):
        self._quantity = qty

    def make_list(self):
        return [self._name, self._type, self._color, self._quantity]

