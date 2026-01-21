from address import Address
from mailing import Mailing

to_address = Address("630126", "Новосибирск", "Рябиновая", "10", "120")
from_address = Address("630089", "Новосибирск", "Лазурная", "90", "11")
track = "293-115"
cost = 380


mailing = Mailing(to_address, from_address, cost, track)


print(mailing)
