from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',name = "BATMAN")


@app.route('/your-url', methods=['GET','POST'])
def your_url():
    if request.method == 'POST':
        # code is the variable we get from home.html file
        #request.form for post and request.args for get
        return render_template('your_url.html',code = request.form['code'])
    else:
        return 'this is not valid'