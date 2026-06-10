def solution(id_pw, db):
    db_dict = {db_id: db_pw for db_id, db_pw in db}
    id, pw = id_pw
    
    if id in db_dict:
        if db_dict[id] == pw:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"