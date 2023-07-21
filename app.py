from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title' : 'Data Analyst',
    'location' : 'Kisumu, Kenya',
    'salary' : 'KES. 1,000,000'
  },
  {
    'id' : 2,
    'title' : 'Data Scientist',
    'location' : 'Paris, France',
    'salary' : 'KES. 2,000,000'
  },
  {
    'id' : 3,
    'title' : 'Videographer',
    'location' : 'Geneve, Switzerland',
    'salary' : 'USD. 5000'
  },
  {
    'id' : 4,
    'title' : 'Software Developer',
    'location' : 'Remote',
    'salary' : 'USD. 10,000'
  }
]

@app.route("/")

def My_family():
  return render_template('home.html', jobs=JOBS, company_name='ChakTek')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)