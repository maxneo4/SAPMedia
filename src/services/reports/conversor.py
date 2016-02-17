def quarters_to_months(quarter):
    switcher = {
        "q1": "'01','02','03'",
        "q2": "'04','05','06'",
        "q3": "'07','08','09'",
        "q4": "'10','11','12'"
    }
    return switcher.get(quarter, "nothing")


def get_type(path):
    switcher = {
        "articles": "'article'",
        "videos": "'video'",
        "all": "'article','video'",
        }
    return switcher.get(path, "nothing")


def get_all_months():
    return "'01','02','03','04','05','05','07','08','09','10','11','12'"