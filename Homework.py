import pyodbc

class Region:
    def __init__(self, RegionID, RegionName):
        self.RegionID = RegionID
        self.RegionName = RegionName

#only contain supplier info
class Suppliers:
    def __init__(self, SupplierID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode,
                 Country, Phone, Fax, Homepage = "NULL"):
        self.SupplierID = SupplierID
        self.CompanyName = CompanyName
        self.ContactName = ContactName
        self.ContactTitle = ContactTitle
        self.Address = Address
        self.City = City
        self.Region = Region
        self.PostalCode = PostalCode
        self.Country = Country
        self.Phone = Phone
        self.Fax = Fax
        self.Homepage = Homepage

#only contains connection information
class Connection:
    def __init__(self, server, database_name, username, password):
        self.server = server
        self.database_name = database_name
        self.username = username
        self.password = password

    def start_connection(self):
        docker_Northwind = pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL SERVER};'
                                          'SERVER=' + self.server + ';'
                                          'DATABASE=' + self.database_name + ';'
                                          'UID=' + self.username + ';'
                                          'PWD=' + self.password)
        cursor = docker_Northwind.cursor()
        return cursor

class ReadOperation:
    def __init__(self, sql):
        self.ops = sql

    def select_from_database(self, x, y):
        list_customers = []
        sql_select = "SELECT " + x + " FROM " + y
        self.cursor.execute(sql_select)
        for z in self.cursor:
            new_customer = Customers(z[0], z[1], z[2], z[3], z[4],
                                     z[5], z[6], [7], [8], [9], [10])
            list_customers.append(new_customer)
        return list_customers
class DeleteOperation:
    def __init__(self):
        self.result = ""


    def delete_database(self, x, y, z):
        sql_delete = "DELETE FROM " + x + " WHERE " + y + " = " + z

        return sql_delete

#where all the connections happen, connects the classes to the sql database, all the operations happen in here
#this is where it will run
class Program_Main:
    def __init__(self):
        self.result = ""

    def run(self, sql):
        connection = Connection("localhost,1433", "Northwind", "sa", "Passw0rd2018")
        cursor = connection.start_connection()
        result = cursor.execute(sql)
        cursor.commit()



   # def crud_operation
        #need an object representing the table
        #need the sql statement to run
        #need the connection object to send query to the database
      #  result =

insert = input("What sql statement would you like to run?  ")
program = Program_Main()
program.run(insert)
