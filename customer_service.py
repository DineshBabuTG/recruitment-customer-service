"""Service to manage customers
"""
import os
import json
import logging
import customer_dao

logger = logging.getLogger('customer_service')
dir_path = os.path.dirname(os.path.realpath(__file__))
print("dir path is ", dir_path)

def addCustomer(name, address):
    print("In Add Customer API")
    logger.info("In Add Customer API")

    logger.info("name " + str(name) + " address " + str(address))
    print("name " + str(name) + " address " + str(address))
    customer_dao.addCustomerDAO(name, address)
    return "Successfully added the customer"

def getAllCustomers():
    print("In Get All Customers API")
    logger.info("In Ger All Customers API")
    #Sample Customer Data
    #customer1 = dict({'name': 'test1', 'address': 'abc'})
    #customer2 = dict({'name': 'test2', 'address': 'abc'})
    customerList = []
    customersFromDB = customer_dao.getCustomersDAO()
    for row in customersFromDB:
        customer = dict({'customerid': row[0], 'name': row[1], 'address': row[2]})
        customerList.append(customer)
    logger.info(customerList)
    data = json.dumps(customerList)
    return data