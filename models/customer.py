from db import db


class CustomerModel(db.Model):
    __tablename__ = "customers"
    CustomerID = db.Column(db.String(5), primary_key=True)
    CompanyName = db.Column(db.String(40))
    ContactName = db.Column(db.String(30))
    ContactTitle = db.Column(db.String(30))
    Address = db.Column(db.String(60))
    City = db.Column(db.String(15))
    Region = db.Column(db.String(15))
    PostalCode = db.Column(db.String(10))
    Country = db.Column(db.String(15))
    Phone = db.Column(db.String(24))
    Fax = db.Column(db.String(24))

    def __init__(self, customerid, companyname, contactname, contacttitle, address, city, region, postalcode, country, phone, fax):
        self.CustomerID = customerid
        self.CompanyName = companyname
        self.ContactName = contactname
        self.ContactTitle = contacttitle
        self.Address = address
        self.City = city
        self.Region = region
        self.PostalCode = postalcode
        self.Country = country
        self.Phone = phone
        self.Fax = fax

    def json(self):
        return {'CustomerID': self.CustomerID,
                'CompanyName': self.CompanyName,
                'ContactName': self.ContactName,
                'ContactTitle': self.ContactTitle,
                'Address': self.Address,
                'City': self.City,
                'Region': self.Region,
                'PostalCode': self.PostalCode,
                'Country': self.Country,
                'Phone': self.Phone,
                'Fax': self.Fax,
                }

    @classmethod
    def find_by_customerid(cls, customerid):
        return cls.query.filter_by(CustomerID=customerid).first()