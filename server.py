from flask import Flask, render_template,redirect,session,request
app = Flask(__name__)

app.secret_key ="asdfk"

#===============
#RENDER FORM ROUTE 
#================

@app.route('/')
def hello():
    return render_template("index.html")

#===============
#PROCESS FORM ROUTE 
#================

@app.route('/user', methods=["POST"])
def process_form():
    session["session_user_name"] = request.form["user_name"]
    session["session_location"] = request.form["location"]
    session["session_fav_language"] = request.form["fav_language"]
    session["session_comment_area"] = request.form["comment_area"]
    return redirect("/results")


@app.route('/results')
def show_results():

    user = {
            "user_name" : session["session_user_name"], 
            "location": session["session_location"], 
            "fav_language":session["session_fav_language"], 
            "comment_area":session["session_comment_area"]
        }   
    return render_template("show_user.html", user=user)

@app.route("/reset")
def reset_session(): 
    session.clear()
    return redirect("/")

#! MUST BE AT THE BOTTOM ---------------
if __name__ == "__main__":
    app.run(debug=True)
