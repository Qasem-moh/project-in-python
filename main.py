# import phonenumbers
# from test import number
#
# from phonenumbers import geocoder
# from phonenumbers import carrier
#
# ch_number = phonenumbers.parse(number, "CH")
#
# print(geocoder.description_for_number(ch_number, "ar"))
# service_number = phonenumbers.parse(number, "RO")
# print(carrier.name_for_number(service_number, "ar"))
import pywhatkit

pywhatkit.sendwhatmsg('+962781315670', 'Hello', 10, 46)
