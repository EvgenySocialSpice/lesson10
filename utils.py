from config import DATA_PATH
import json


# загружает все данные кандидатов
def load_data(path=DATA_PATH):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# список всех кандидатов
def candidates_get_all():
    data = load_data()
    return data


# получение кандидатов по РК
def candidates_get_by_pk(pk):
    candidates = load_data()
    for candidate in candidates:
        if candidate['id'] == pk:
            return candidate


# получение данных по навыкам
def get_candidates_by_skill(skill_name):
    skilled_candidates = []
    skill_name_lower = skill_name.lower()
    candidates = load_data()
    for candidate in candidates:
        skills = candidate['skills'].lower().strip().split(', ')
        if skill_name_lower in skills:
            skilled_candidates.append(candidate)
            continue
        return skilled_candidates
