from flask import Flask, render_template, request
from exam import movies

app = Flask(__name__)
@app.route('/movies', methods = ['GET', 'POST'])
def movie():
    if request.method == 'GET':
        return render_template('ex6.html')
    else:
        title = request.form['title']

        if title in movies['favourite']:
            message = 'favourite'
        elif title in movies['hated']:
            message = 'hated'
        else:
            message = 'no such movie'
    return render_template('ex6.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)