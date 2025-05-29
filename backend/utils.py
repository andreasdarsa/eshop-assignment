def serialize(p):
    p["_id"] = str(p["_id"])
    return p