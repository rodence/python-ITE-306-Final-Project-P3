# python-ITE-306-Final-Project-P3
ITE 306 P3 Project
### Proponents of this project:
* Rodence Atacador
* Mark Joshua De Dios
* Kenneth Perez
* Marvin Caventa

# Space World

## Folder Structure: 

![Capture](https://user-images.githubusercontent.com/113341443/196738092-ca02f0b3-bceb-40fe-9eb7-cda093f8b20a.PNG)


## To run this site you need to install flask:

* in cmd run this command `pip install flask`


* function.py source code:
```python
from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/home")
def main():
    return render_template("index2.html")


@app.route("/info")
def info():
    return render_template("aass.html")


@app.route("/planets")
def planets():
    return render_template("apam.html")

@app.route("/view")
def view():
    return render_template("vtss.html")

@app.route("/images")
def images():
    return render_template("sai.html")

@app.route("/quiz")
def quiz():
    return render_template("pq.html")


@app.route("/facts")
def facts():
    return render_template("if.html")


if __name__ == "__main__":
    app.run(debug=True)

```

* go to the file directory of `function.py`
* go to terminal and run function.py using command: `python function.py`

* the output must be:

```bash

(.venv) C:\Users\jesre\OneDrive\Desktop\RodenceFiles\flask\p3 306 final project>python function.py
 * Serving Flask app 'function'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 107-990-516

```

## Try the following URL's:


```bash
http://127.0.0.1:5000/
http://127.0.0.1:5000/home
http://127.0.0.1:5000/info
http://127.0.0.1:5000/planets
http://127.0.0.1:5000/view
http://127.0.0.1:5000/images
http://127.0.0.1:5000/quiz
http://127.0.0.1:5000/facts

```

## Screenshots:

![Screenshot (117)](https://user-images.githubusercontent.com/113341443/196734922-d1c7e453-519c-4cef-b14e-ead1b96c68ee.png)

![Screenshot (118)](https://user-images.githubusercontent.com/113341443/196734931-d5b08484-76b0-4ae0-82cc-01b288d9bf88.png)

![Screenshot (119)](https://user-images.githubusercontent.com/113341443/196734940-b7f59629-4af4-4294-99c8-4f866e608a0e.png)

![Screenshot (120)](https://user-images.githubusercontent.com/113341443/196734952-9b88d054-295e-4641-8392-13a35ffb126d.png)

![Screenshot (121)](https://user-images.githubusercontent.com/113341443/196734958-dc56b221-17f8-47d0-8836-0146ae037a49.png)

![Screenshot (122)](https://user-images.githubusercontent.com/113341443/196734971-6a3afbd2-2a54-4df8-a5e0-d3dc2a1f6a81.png)

![Screenshot (123)](https://user-images.githubusercontent.com/113341443/196734978-fdeb302d-c0a1-4f9e-b7f2-b55c906c94f3.png)

![Screenshot (116)](https://user-images.githubusercontent.com/113341443/196734986-5eab0d71-0c19-4ff8-8529-6737b51184ef.png)




