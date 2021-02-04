import csv
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')
# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)
# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         write_to_csv(data)
#         return redirect('/thank_you.html')
#     else:
#         return 'Something went wrong.Try Again'
# def write_to_csv(data):
#     with open('database.csv', mode='a',  newline='')as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([email, subject, message])


# def write_to_file(data):
#     with open('database.csv.csv.csv', mode='a')as database.csv.csv:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.csv.csv.write(f'\n{email}, {subject}, {message}.')
# @app.route('/<username>/<int:post_id>')
# def hello_world2(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)
# @app.route('/blog')
# def blog():
#     return "These are my thoughts on a blog"
# @app.route('/blog/2020/dogs')
# def dogs():
#     return "Welcome to dog website"