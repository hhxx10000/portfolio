from app import db, BlogPost

db.create_all()
BlogPost.query.all()
db.session.add(BlogPost(title='Blog Post 1', content='Content of Blog Post 1. lalala', author = 'Fish'))
db.session.add(BlogPost(title='Blog Post 2', content='Content of Blog Post 2. lululu'))
db.session.commit()
# BlogPost.query.all()[0].date_posted

BlogPost.query.first()
BlogPost.query[1]
BlogPost.query.filter_by(title = 'First').all()
BlogPost.query.get(2)

db.session.delete(BlogPost.query.get(2))
db.session.commit()

BlogPost.query.get(1).author = 'AAA'
db.session.commit()