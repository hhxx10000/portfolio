from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///StockDB.db'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/stock')
def stockData():
    return render_template('stock.html')

@app.route('/trans')
def trans():
    return render_template('trans.html')

@app.route('/import', methods=['GET', 'POST'])
def StockDataImport():
    if request.method == 'POST':
        trans_csv = request.form.get('trans_csv').split('\n')
        reader = csv.DictReader(trans_csv)

        results = []
        for row in reader:
            results.append(dict(row))
        
        print(results)
        return 'post'
    else:
        return render_template('import.html')

PortfTableHeader = (r'#', r'Ticker', r'Current Price', r'Cost', r'Quantity', r'Gain/Loss', r'Gain/Loss %')
PortfData = (
    (1,'AAPL',300,100,10,2000,2),
    (2,'U',130,100,20,-600,-0.6,)
)
@app.route('/portf')
def StockPortfolio():
    return render_template('portf.html', headings=PortfTableHeader, data=PortfData)

@app.route('/upload_test', methods=['GET', 'POST'])
def uploadTest():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author = post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')

    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('testUpload.html', posts = all_posts)

if __name__ == "__main__":
    app.run(debug = True)