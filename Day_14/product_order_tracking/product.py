from flask import Flask, request, render_template,redirect,url_for,session

appProduct = Flask(__name__)
appProduct.secret_key = 'secret'
print(appProduct)

@appProduct.route('/')
def home():
    return render_template('Home.html')

@appProduct.route('/productdetails',methods=['POST'])
def product():
    product_name = request.form['productname']
    product_quantity = request.form['quantity']

    session['Product_name'] = product_name
    session['Quantity'] = product_quantity

    return render_template('Shipping_details.html')


@appProduct.route('/shippingdetails', methods=['POST'])
def shipping():
    username = request.form['name']
    shipping_address = request.form['address']
    phone_no = request.form['contact number']

    session['user'] = username
    session['Address'] = shipping_address
    session['Contact No'] = phone_no

    return redirect(url_for('order_summary'))

@appProduct.route('/ordersummary')
def order_summary():
    product_name = session.get('Product_name')
    product_quantity = session.get('Quantity')
    shipping_user = session.get('user')
    shipping_address = session.get('Address')
    shipping_contact = session.get('Contact No')

    return render_template("order_summary.html",productname = product_name,quantity=product_quantity,username=shipping_user,add=shipping_address,contct=shipping_contact)

if __name__ == '__main__':
    appProduct.run(debug=True,port=5001)