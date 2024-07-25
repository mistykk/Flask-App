from flask import Flask, render_template

app = Flask(__name__)

Jobs = [{
    "id": 1,
    "title": "Data Analyst",
    "location": "Bengluru",
    "salary": 100000
}, {
    "id": 2,
    "title": "Data Scientist",
    "location": "Noida",
    "salary": 100000
}, {
    "id": 3,
    "title": "Software Developer",
    "location": "Pune",
    "salary": 100000
}, {
    "id": 4,
    "title": "UI Developer",
    "location": "Hyderabad",
    "salary": 100000
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=Jobs)

@app.route('/jobs')
def list_jobs():
  return Jobs


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
