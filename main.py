from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form= """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color:#eee;
                padding:20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
     <form action="/" method="post">
     <label>Rotate by:
     <input  type="text" name="rot" value="0"><br>
     <textarea name ="text">{0}</textarea><br>
     </label>
     <input type="submit" value="Submit Query">
     </form>
    </body>
</html>
"""

@app.route("/")
def index():

    form_string = " "
   
    return form.format(form_string)


@app.route("/",methods=["POST"])
def encrypt():
    print("In encrypt")
    t = str(request.form["text"])
    r = int(request.form["rot"])
    encrypted_string = rotate_string(t,r)
    result = "<h1>" + encrypted_string + "</h1>"

    return form.format(encrypted_string)

app.run()
