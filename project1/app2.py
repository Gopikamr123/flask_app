




from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    submitted_data = None
    if request.method == 'POST':
       
        submitted_data = {
            'username': request.form.get('name'),
            'email': request.form.get('Email'),
            'regno': request.form.get('RegNo'),
            'phone': request.form.get('PhoneNo')
        }
    return render_template("index1.html", data=submitted_data)

@app.route('/de/<name>')
def deb(name):
    
    if len(name) > 5:
        return "The 5th character is {}".format(name[5])
    return "Name is too short!"

@app.errorhandler(404)
def not_found(e):
    return "Page not found!", 404

if __name__ == '__main__':
    app.run(debug=True)