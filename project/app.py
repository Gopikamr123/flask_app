from flask import Flask, render_template,request,url_for,redirect,session

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = "super_secret_key"

# Define the route for the home page
@app.route('/', methods = ["GET","POST"])
def home():
    email = ""
    regno =""
    password = ""
    
    
    if request.method == "POST":
        email = request.form.get("input_email")
        password = request.form.get("input_password")
        regno = request.form.get("input_regno")
        print(email,regno ,password)
        if email == "admin" and password == "password123":
            session["email"] = email
            return redirect(url_for('dashboard', username=email))

    return render_template("index.html",email = email, regno = regno, password= password )
        
    
@app.route("/dashboard/<username>")
def dashboard(username):
    session_user = session.get("email")                
    
    if not session_user:
        return redirect(url_for('home'))
   
    return render_template("dashboard.html", user=username)

if __name__ == '__main__':
    # Run the app in debug mode so changes appear immediately
    app.run(debug=True,port=8000)