from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Menu page
@app.route('/menu', methods=['GET', 'POST'])
def menu():
    items = [
        {"name": "Paneer Butter Masala", "price": "$12.99"},
        {"name": "Chicken Biryani", "price": "$14.99"},
        {"name": "Tandoori Roti", "price": "$2.99"},
        {"name": "Veg Manchurian", "price": "$10.99"},
        {"name": "Gulab Jamun", "price": "$4.99"},
        {"name": "rabdi", "price": "$3.99"},
    ]
    
    if request.method == 'POST':
        # Get selected items from the form
        selected_items = request.form.getlist('menu_item')
        return render_template('selected.html', selected_items=selected_items)
    
    return render_template('menu.html', menu_items=items)

if __name__ == '__main__':
    app.run(debug=True)


