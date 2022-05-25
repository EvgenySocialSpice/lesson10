from flask import Flask, render_template
import utils
import sreened

app = Flask(__name__)


@app.route('/')
def page_all_candidates():
    candidates = utils.candidates_get_all()
    html_code = sreened.build_html_for_some_candidate(candidates)
    return html_code


@app.route('/skills/<skill>')
def page_candidates_by_skill(skill):
    candidates = utils.get_candidates_by_skill(skill)
    if len(candidates) == 0:
        return "Таких кандидатов нет"
    html_code = sreened.build_html_for_some_candidate(candidates)
    return html_code


@app.route('/candidates/<int:pk>')
def page_candidates_by_pk(pk):
    candidate = utils.candidates_get_by_pk()
    if candidate is None:
        return "Такого кандидата нет"
    html_code = sreened.build_html_for_one_candidate(candidate)
    return html_code


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
