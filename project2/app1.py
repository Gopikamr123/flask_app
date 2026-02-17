#from flask import Flask, render_template,request,url_for,redirect
#import requests

#app = Flask(__name__)

#@app.route('/',methods = ["GET"])
#def Home():
 #   user_id = request.args.get("userid")
  #  posts = []
   # if user_id:
    #    url ="https://jsonplaceholder.typicode.com/posts"
     #   response = requests.get(url,params={"userId": user_id})


      #  if response.status_code == 200:
       #     posts = response.json()
    #return render_template("home.html",posts=posts)

#app.run(debug=True)



from flask import Flask, render_template, request
import string
import random
#import secret
app = Flask(__name__)


def generate_password(length, uppercase, lowercase, digits, special):
    #random .seed(10)
    characters = string.ascii_lowercase

    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special:
        characters += string.punctuation
    


    if not characters:
        characters = string.ascii_lowercase



    password = ''.join(random.choice(characters) for _ in range(length))#scert
    return password 

@app.route('/', methods=["GET", "POST"])
def home():
    password = None
    if request.method == "POST":
        
        length = int(request.form.get("length", 12))
        use_upper = "uppercase" in request.form
        use_lower = "lowercase" in request.form 
        use_digits = "digits" in request.form
        use_special = "special" in request.form
        
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)

    
    return render_template("password.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)