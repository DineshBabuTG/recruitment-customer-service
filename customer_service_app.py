from flask import Flask, abort, request
import logging.config
import customer_service
app = Flask(__name__)

logging.config.fileConfig('logging.conf')
# create logger
logger = logging.getLogger('customer_service_app')

@app.route('/', methods=["GET"])
def customer_service_home():
    return "Customer Service App..."

@app.route('/customerservice/addcustomer', methods=["POST"])
def add_customer():
    if not request.json:
        logger.info('The Request Body is not the JSON Type... Hence throwing 400 error code...')
        abort(400)
    logger.info('JSON Request: ' + str(request.json))
    print(request.json)
    data = request.json
    name = data['name']
    logger.info('name: ' + name)
    print('name: ' + name)
    address = data['address']

    logger.info('Going to call add customer API...')
    customerAdded = customer_service.addCustomer(name=name, address=address)
    print("Customer Added " + str(customerAdded))
    logger.info("Customer Added " + str(customerAdded))
    return str(customerAdded)

@app.route('/customerservice/getallcustomers', methods=["GET"])
def get_All_Customers():
    customersList = customer_service.getAllCustomers()

    return customersList

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8001)