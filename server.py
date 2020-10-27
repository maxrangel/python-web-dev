from flask import Flask, render_template, request, redirect
import csv

# Needed to render static files
app = Flask(__name__,
            static_url_path='/static',
            static_folder='static',
            template_folder='templates')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name=None):
    return render_template(f'{page_name}.html')


# Saving data on txt file
# def save_contact_data(data):
#     with open('database.txt', mode="a") as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email},{subject},{message}')

# Saving data on csv file
def save_contact_data(data):
    with open('database.csv', mode="a", newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit-form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            save_contact_data(data)
            return redirect('/thankyou')
        except:
            return 'Did not save to database'
    else:
        return 'Something went very wrong!'
