from flask import Flask, request, jsonify

app = Flask(__name__)

from sql_connection import get_sql_connection
import products_dao
import units_dao

connection = get_sql_connection()

@app.route('/getUnits')
def get_unit():
    units = units_dao.get_units(connection)
    responce =  jsonify(units)
    responce.headers.add('Access-Control-Allow-Origin','*')
    return responce


@app.route('/getProducts')
def get_products():
    products = products_dao.get_all_products(connection)
    responce =  jsonify(products)
    responce.headers.add('Access-Control-Allow-Origin','*')
    return responce




if __name__ == '__main__':
    print("Starting Python flask server for Grocery Store Management System")
    app.run(port=5000)