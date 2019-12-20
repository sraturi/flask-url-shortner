from flask import Flask, render_template, request, redirect, url_for,flash
import json
import os.path

app = Flask(__name__)
app.secret_key = 'gfchf45rgcgvhb67vhbnj6ftftyt5yyg'

@app.route('/')
def home():
    return render_template('home.html',name = "BATMAN")


@app.route('/your-url', methods=['GET','POST'])
def your_url():
    if request.method == 'POST':
        urls = {}
        #request.form for post and request.args for get
        #creating a dictionary for url and short name and a json file
        
        # if the path exist, we load the file.
        if os.path.exists('urls.json'):
            with open('urls.json') as url_file:
                urls=json.load(url_file)

        #if the name already exist, go back to home
        # code and url are the variable we get from home.html file
        if request.form['code'] in urls.keys():
            flash('oops looks like the short name has already been taken!')
            return redirect(url_for('home'))

        urls[request.form['code']] = {'url': request.form['url']}
        with open('urls.json','w') as url_file:
            json.dump(urls,url_file)
        return render_template('your_url.html',code = request.form['code'])
    else:
        #if there is someone is trying to do a get request, send them bk to home
        #url_for makes page based on function name
        return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')