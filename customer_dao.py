import random

import mysql.connector
import logging
import random
import os
from mysql.connector import Error

logger = logging.getLogger('customer_dao')

def getMySQLConnection():
    try:
        dbhostname = os.environ['dbhostname']
        print("Database hostname is " + dbhostname)
        logger.info("Database hostname is " + dbhostname)
        connection_config_dict = {
            'user': 'edureka',
            'password': 'edureka',
            'host': dbhostname,
            'port': '3306',
            'database': 'dinasys',
            'raise_on_warnings': True
        }
        connection = mysql.connector.connect(**connection_config_dict)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            logger.info("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            logger.info("You're connected to database: ", record)
        else:
            logger.info("MySQL not connected")
        return connection
    except Error as e:
        logger.info("Error while connecting to MySQL", e)
        print("Error while connecting to MySQL", e)
    finally:
        logger.info("In Finally of DB Connection")
        print("In Finally of DB Connection")
        # if connection.is_connected():
        #     cursor.close()
        #     connection.close()
        #     print("MySQL connection is closed")

def executeDBInsertQuery(connection, statement, data):
    cursor = connection.cursor()
    try:
        result = cursor.execute(statement, data)
        connection.commit()
        logger.info(f"Query executed successfully {statement}")
        return result
    except Error as e:
        logger.info(f"Query execution error '{e}' occurred")

def executeDBExecuteQuery(connection, statement):
    cursor = connection.cursor()
    try:
        cursor.execute(statement)
        logger.info(f"Query executed successfully {statement}")
        return cursor.fetchall()
    except Error as e:
        logger.info(f"Query execution error '{e}' occurred")

def addCustomerDAO(name, address):
    print("In Add Customer DAO Service")
    logger.info("In Add Customer DAO Service")
    customerid = random.randint(1,999999)
    logger.info(
        "customerid " + str(customerid) + " name " + str(name) + " address " + str(address))
    print(
        "customerid " + str(customerid) + " name " + str(name) + " address " + str(address))

    insert_stmt = (
        "INSERT INTO customers (customerid, name, address) "
        "VALUES (%s, %s, %s)"
    )
    data = (customerid, name, address)
    logger.info(insert_stmt, data)
    connection = getMySQLConnection()
    executeDBInsertQuery(connection, insert_stmt, data)

    logger.info("Successfully inserted the customer entry for the id " + str(customerid))
    return "Successfully inserted the customer entry for the id " + str(customerid)

def getCustomersDAO():
    print("In Gets Customers DB Service")
    logger.info("In Get Customers DB Service")

    mySql_Get_Customers_Select_Query = "select * from customers"
    connection = getMySQLConnection()
    result = executeDBExecuteQuery(connection, mySql_Get_Customers_Select_Query)
    logger.info("Successfully get the customers " + str(result))
    return result