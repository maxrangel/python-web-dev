from flask import Flask, render_template, request, redirect
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


@app.route('/submit-form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        data = request.form.to_dict()

        return redirect('/thankyou')
