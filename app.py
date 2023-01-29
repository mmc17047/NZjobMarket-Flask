import asyncio
from flask import Flask, render_template, request
from forms import SearchForm
from typing import List
from job import Job
from fetch import get_job_titles


skills_list = []
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'


@app.route('/', methods=['GET', 'POST'])
def search():
    global skills_list
    form = SearchForm()
    if form.is_submitted():
        try:
            data = request.get_json()
            if data is not None:
                skills = data["skills"]
                skills_list = skills.split(",")
        except:
            print("An exception occurred")
        joblist: List[Job] = get_job_titles(request.form.get('jobTitle'))
        return render_template('result.html', joblist=joblist)
    return render_template('search.html', form=form)


if __name__ == '__main__':
    app.run()
