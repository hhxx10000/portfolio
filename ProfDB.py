from StockWebApp import db
import datetime

class user_account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False) #what user
    account = db.Column(db.String(20)) #what account
    trans_acct = db.relationship('transaction', backref='usr_acct')

class stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Ticker = db.Column(db.String(20), unique=True, nullable=False)
    Descp = db.Column(db.String(120), unique=True, nullable=False)
    price_stock = db.relationship('stock_price',backref='price_stock')
    trans_stock = db.relationship('transaction',backref='trans_stock')

    def __repr__(self):
        return Ticker

class stock_price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    time = db.Column(db.DateTime)
    open = db.Column(db.Float)
    close = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)

class transaction_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Descp = db.Column(db.String(30), nullable=False)
    type_trans = db.relationship('transaction', backref='type_trans')

class transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usr_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    trans_type = db.Column(db.Integer, db.ForeignKey('transaction_type.id'), nullable=False)
    time = db.Column(db.DateTime)
    unit_price = db.Column(db.Float)
    quantity = db.Column(db.Float)

if __name__=='__main__':
    db.create_all()
    Xin_Chase = user_account(name='Xin Huang', account='Chase')
    Stock_AAPL = stock(Ticker='AAPL', Descp='Apple Inc')
    AAPL_price_time1 = stock_price(price_stock=Stock_AAPL, time=datetime.datetime(2021,2,18), open=100, close=120, high=150, low=90)
    AAPL_price_time2 = stock_price(price_stock=Stock_AAPL, time=datetime.datetime(2021,2,19), open=130, close=90, high=130, low=85)
    buy = transaction_type(Descp='Buy Stock')
    sell = transaction_type(Descp='Sell Stock')
    dividend = transaction_type(Descp='Dividend')
    trans1 = transaction(usr_acct=Xin_Chase, trans_stock=Stock_AAPL, type_trans=buy, time=datetime.datetime(2021,2,18), unit_price=130, quantity=5)
    trans2 = transaction(usr_acct=Xin_Chase, trans_stock=Stock_AAPL, type_trans=sell, time=datetime.datetime(2021,2,19), unit_price=100, quantity=3)

    db.session.add_all([Xin_Chase,Stock_AAPL,AAPL_price_time1,AAPL_price_time2,buy,sell,dividend,trans1,trans2])
    db.session.commit()