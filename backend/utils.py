# a function that turns the id field (ObjectId type) into a string
# that makes any object of the db ready to be jsonified
def serialize(p):
    p["_id"] = str(p["_id"])
    return p
