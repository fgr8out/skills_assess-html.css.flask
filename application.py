from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template("index.html")
    """Show an index page."""

@app.route('/application')
def job_form():
    return render_template("application-form.html")
    """Show application form page."""

@app.route('/response')
def app_response():
    f.name = request.args.get("First_Name")
    l.name = request.args.get("Last_Name")
    job_chosen = request.args.get("Job_Title")
    sal_amount = request.args.get("Salary")

    return render_template("application-response.html", First_Name=f.name, 
            Last_Name=l.name, Job_Title=job_chosen, Salary=sal_amount)

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
