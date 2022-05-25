def build_html_for_one_candidate(candidate):
    # вывод характеристики одного кандидата
    code_for_candidate = ""
    code_for_candidate += f"<img src=\"{candidate['picture']}\">\n"
    code_for_candidate += f"{candidate['name']}\n"
    code_for_candidate += f"{candidate['skills']}\n"
    code_for_candidate += f"{candidate['position']}\n"
    code_for_candidate += "\n"
    return "<pre>" + code_for_candidate + "</pre>"


def build_html_for_some_candidate(candidates):
    # вывод характеристики нескольких кандидатов
    code_for_candidates = ""
    for candidate in candidates:
        code_for_candidates += f"{candidate['name']}\n"
        code_for_candidates += f"{candidate['skills']}\n"
        code_for_candidates += f"{candidate['position']}\n"
        code_for_candidates += "\n"

    return "<pre>" + code_for_candidates + "</pre>"
