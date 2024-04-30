from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def customer_info():
    if request.method == 'POST':
        customer_name = request.form.get('name', 'Guest')
        return redirect('https://www.honda2wheelersindia.com/products/motorcycle', code=302)
    return render_template('index.html')  # Create an HTML template with the form

if __name__ == '__main__':
    app.run(debug=True)
