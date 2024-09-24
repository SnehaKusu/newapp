from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.comments_db
comments_collection = db.comments

@app.route('/')
def index():
    comments = comments_collection.find()
    return render_template('index.html', comments=comments)

@app.route('/add_comment', methods=['POST'])
def add_comment():
    name = request.form.get('name')
    comment = request.form.get('comment')

    if name and comment:
        comments_collection.insert_one({'name': name, 'comment': comment})
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
