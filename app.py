from flask import Flask, render_template, request, redirect
from database import get_connection

# Create Flask application
app = Flask(__name__)


# Home page: show all supplies.
@app.route("/")
def home():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    # Retrieve all supplies from database
    cursor.execute("SELECT * FROM supplies")
    supplies = cursor.fetchall()

    # Count total items
    total = len(supplies)

    cursor.close()
    connection.close()

    return render_template("index.html", supplies=supplies, total=total)


# Add new supply item
@app.route("/add", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        item_name = request.form["item_name"]
        category = request.form["category"]
        quantity = request.form["quantity"]
        unit = request.form["unit"]
        minimum_stock = request.form["minimum_stock"]

        connection = get_connection()
        cursor = connection.cursor()

        # Insert new item into supplies table.
        cursor.execute(
            """
            INSERT INTO supplies 
            (item_name, category, quantity, unit, minimum_stock)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (item_name, category, quantity, unit, minimum_stock)
        )

        connection.commit()
        cursor.close()
        connection.close()

        return redirect("/")

    return render_template("add_item.html")


# Edit existing supply item
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_item(id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == "POST":
        item_name = request.form["item_name"]
        category = request.form["category"]
        quantity = request.form["quantity"]
        unit = request.form["unit"]
        minimum_stock = request.form["minimum_stock"]

        # Update selected item.
        cursor.execute(
            """
            UPDATE supplies
            SET item_name=%s,
                category=%s,
                quantity=%s,
                unit=%s,
                minimum_stock=%s
            WHERE id=%s
            """,
            (item_name, category, quantity, unit, minimum_stock, id)
        )

        connection.commit()
        cursor.close()
        connection.close()

        return redirect("/")

    # Get selected item data
    cursor.execute("SELECT * FROM supplies WHERE id=%s", (id,))
    item = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template("edit_item.html", item=item)


# Delete supply item
@app.route("/delete/<int:id>")
def delete_item(id):
    connection = get_connection()
    cursor = connection.cursor()

    # Delete selected item.
    cursor.execute("DELETE FROM supplies WHERE id=%s", (id,))
    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/")


# View transaction history using JOIN
@app.route("/transactions")
def transactions():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    # Join supplies and transactions tables
    cursor.execute(
        """
        SELECT
            supplies.item_name,
            transactions.transaction_type,
            transactions.quantity,
            transactions.transaction_date
        FROM transactions
        JOIN supplies
        ON transactions.supply_id = supplies.id
        """
    )

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("transactions.html", records=records)


# Run application
if __name__ == "__main__":
    app.run(debug=True, port=5050)