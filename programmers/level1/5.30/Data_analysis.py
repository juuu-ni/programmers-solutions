def solution(data, ext, val_ext, sort_by):
    names=["code","date","maximum","remain"]
    ext_idx = names.index(ext)
    sort_idx = names.index(sort_by)
    
    new_data = [i for i in data if i[ext_idx]<val_ext]
    
    new_data.sort(key=lambda x : x[sort_idx])
    
    return new_data