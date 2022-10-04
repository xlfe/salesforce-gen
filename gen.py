import json
import random
from faker import Faker

fake = Faker()

industries = [
            'Agriculture, Forestry and Fishing',
            'Mining',
            'Manufacturing',
            'Electricity, Gas, Water and Waste Services',
            'Construction',
            'Wholesale Trade',
            'Retail Trade',
            'Accommodation and Food Services',
            'Transport, Postal and Warehousing',
            'Information Media and Telecommunications',
            'Financial and Insurance Services',
            'Rental, Hiring and Real Estate Services',
            'Professional, Scientific and Technical Services',
            'Administrative and Support Services',
            'Public Administration and Safety',
            'Education and Training',
            'Health Care and Social Assistance',
            'Arts and Recreation Services',
            'Other Services'
        ]


def Account():

    return {
            'Account Name': fake.company(),
            'Industry': random.choice(industries),
            'Phone': fake.phone_number(),
            'Shipping Address': fake.address(),
            'Website': fake.url()
            }



def Contact(account):

    return {
            "Account Name": account['Account Name'],
            "Birthdate" : str(fake.date_of_birth(minimum_age=20, maximum_age=70)),
            "Email":fake.email(),
            "First Name":fake.first_name(),
            "Last Name":fake.last_name(),
            "Phone":fake.phone_number()
            }


accounts = [Account() for i in range(1000)]
contacts = [Contact(random.choice(accounts)) for i in range(10000)]

with open('accounts.json','w') as ac:
    json.dump(accounts, ac)


with open('contacts.json','w') as ac:
    json.dump(contacts, ac)
