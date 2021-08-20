from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "asdqwertypenis"

toDoItems = []
removedItems = []
doneItems = []
errors_handler = ["Item already exists!","Please input an item name!","Maximum input lenght is 25 characters!"]

@app.route("/", methods = ["POST", "GET"])
def home():
    global toDoItems
    global removedItems
    global doneItems
    global err
    list_to_check = toDoItems + removedItems + doneItems
    if request.method == "POST":
        if request.form["inputText"] == "":
            err = errors_handler[1]
            return render_template("index.html", error = err, lista=toDoItems, listaDone = doneItems, listaRemoved = removedItems)
        elif request.form["inputText"] in list_to_check:
            err = errors_handler[0]
            return render_template("index.html", error = err, lista=toDoItems, listaDone = doneItems, listaRemoved = removedItems)
        elif len(request.form["inputText"]) >25:
            err = errors_handler[2]
            return render_template("index.html", error = err, lista=toDoItems, listaDone = doneItems, listaRemoved = removedItems)
        else:
            itemName = request.form["inputText"]
            toDoItems.append(itemName)
            return render_template("index.html", lista=toDoItems, listaDone = doneItems, listaRemoved = removedItems)
    else:
        return render_template("index.html", lista=toDoItems, listaDone = doneItems, listaRemoved = removedItems)

@app.route("/remove/<item>/")
def remove(item):
    global toDoItems
    global removedItems
    global doneItems
    toDoItems.remove(item)
    removedItems.append(item)
    return redirect(url_for("home"))

@app.route("/remove2/<item>/")
def remove2(item):
    global toDoItems
    global removedItems
    global doneItems
    doneItems.remove(item)
    removedItems.append(item)
    return redirect(url_for("home"))

@app.route("/done/<item>/")
def done(item):
    global toDoItems
    global removedItems
    global doneItems
    toDoItems.remove(item)
    doneItems.append(item)
    return redirect(url_for("home"))


@app.route("/undone/<item>/")
def undone(item):
    global toDoItems
    global removedItems
    global doneItems
    toDoItems.append(item)
    doneItems.remove(item)
    return redirect(url_for("home"))

@app.route("/undone2/<item>/")
def undone2(item):
    global toDoItems
    global removedItems
    global doneItems
    toDoItems.append(item)
    removedItems.remove(item)
    return redirect(url_for("home"))

@app.route("/fremove/<item>/")
def fremove(item):
    global toDoItems
    global removedItems
    global doneItems
    removedItems.remove(item)
    return redirect(url_for("home"))




if __name__ == "__main__":
    app.run(debug = True)

