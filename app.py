from flask import Flask, render_template, request, redirect, url_for

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
        #if there is someone is trying to do a get request, send them bk to home
        #url_for makes page based on function name
        return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')