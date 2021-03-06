from flask import Flask, render_template, request

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
    firstname = request.args.get("firstname")
    print firstname
    lastname = request.args.get("lastname")
    print lastname
    job_chosen = request.args.get("careeroptions")
    print job_chosen
    sal_amount = request.args.get("currency")
    print sal_amount

    return render_template("application-response.html", First_Name=firstname, 
            Last_Name=lastname, Job_Title=job_chosen, Salary=sal_amount)

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
