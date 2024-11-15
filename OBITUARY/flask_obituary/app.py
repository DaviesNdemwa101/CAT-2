from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary "database"
obituaries = []

@app.route('/')
def home():
    return render_template('view_obituaries.html', obituaries=obituaries)

@app.route('/submit', methods=['GET', 'POST'])
def submit_obituary():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        date_of_birth = request.form['date_of_birth']
        date_of_death = request.form['date_of_death']
        content = request.form['content']
        author = request.form['author']

        # Add it to the "database"
        obituaries.append({
            'name': name,
            'date_of_birth': date_of_birth,
            'date_of_death': date_of_death,
            'content': content,
            'author': author
        })

        # Go back to the homepage
        return redirect(url_for('home'))

    # Show the form
    return render_template('obituary_form.html')

if __name__ == '__main__':
    app.run(debug=True)
