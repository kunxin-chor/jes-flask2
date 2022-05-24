from flask import Flask, flash, render_template, request, redirect, url_for

# create an instance of the Flask application
app = Flask(__name__) # __name__ is a magic variable. If is 'main' then it means we are running app.py as the application

# enable sessions by providing an encryption key
app.secret_key = b"lxS9x3VFdCrHxyBapzZp3hTQa9jONvUq"

# define routes
@app.route('/')
def home():
    return render_template('home.html') # render_template will automatically look for the file in the templates folder

@app.route('/greet')
def greet():
    first_name = "John"
    return render_template('greeting.html', fname = first_name, lname = "Smith")

@app.route('/hello/<username>')
def say_hello(username):
    return render_template('say_hello.html', name=username)

@app.route('/feedback', methods=["GET"])
def feedback():
    return render_template('feedback.html')

@app.route('/feedback', methods=["POST"])
def process_feedback():
    # extract out each field from the form
    print(request.form)
    fullname = request.form.get('fullname')
    email = request.form['email']
    feedback_type = request.form.get('feedback_type')
    hear_about = request.form.getlist('hear_about')
    print("hear_about =>", hear_about)
    return render_template("thanks.html", fullname=fullname, email=email, 
                           feedback_type=feedback_type, hear_about=hear_about)


# step 1: create the route to display the form 
@app.route('/register',methods=["GET"])
def register():
    return render_template('register.html')


# step 2: route to process the form
@app.route('/register', methods=["POST"])
def process_register():
    print(request.form)
    if request.form.get('password') == request.form.get('password_confirm'):
        flash("The customer has been created successful", "success")
    else:
        flash("Invalid password so account creation failed", "error")   
    return redirect(url_for('register'))
       

# begin our server
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)