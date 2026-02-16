from flask import Flask

app = Flask(__name__)

houses = [
    {
        Title: "Overland - 2 Bedroom 1 Bath",
        Price: '$1400',
        Description: "This is a 2 bedroom 1 bath house located in Overland. It has a spacious living room and a modern kitchen.",
        Address: "123 Main St, Overland, MO 63114",
        Status: "Available"
    }
]

app.get('/houses')
def get_houses():
    return {"houses": houses}

