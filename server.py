from flask import Flask, render_template, redirect, url_for

from forms import TeamForm, ProjectForm

from model import connect_to_db, db, User, Team, Project 

user_id= 1

app = Flask(__name__)
app.secret_key="SecretKey"

@app.route("/")
def home():
    team_form = TeamForm()
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams)
    return render_template("home.html", team_form=team_form, project_form=project_form)

@app.route("/add-team", methods =["POST"])
def add_team():
    team_form = TeamForm()
        
    if team_form.validate_on_submit():
        print(team_form.team_name.data)
    else:
        print("Form failed to validate.")
    return redirect(url_for("home"))

@app.route("/add-project", methods = ["POST"])
def add_project():
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams)

    if project_form.validate_on_submit():
        print(project_form.project_name.data)
        print(project_form.description.data)
        print(project_form.completed.data)
        print(project_form.team_selection.data)
    return redirect(url_for("home"))

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)