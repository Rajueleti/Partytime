from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://RajuEleti:RajuEleti@cluster0.iz79rqq.mongodb.net/?retryWrites=true&w=majority")
db = client['db']
collection = db['Partytime']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    brand_name = request.form.get('brand_name')
    brand_details = collection.find_one({'brand': brand_name})
    return render_template('index.html', brand_details=brand_details)

if __name__ == '__main__':
    app.run(debug=True)
