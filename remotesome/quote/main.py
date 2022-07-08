from fastapi import FastAPI

app = FastAPI()
ALL_QUOTES = {
        1: {
            'author': 'Author1',
            'quote': 'Quote1',
        },
        2: {
            'author': 'Author2',
            'quote': 'Quote2',
        },
    }

# {"author": "author4","quote": "Quote4"}


@app.get("/quotes/{quote_id}")
def quotes(quote_id):
    qs = quotes()
    return {"quote_id": qs[int(quote_id)]}


@app.get("/quotes/")
def all_quotes():
    return {"quotes": quotes()}


@app.put("/quotes/{quote_id}")
def update_quote(quote_id, quote):
    # Should update the previous data
    quote_object = ALL_QUOTES[int(quote_id)]
    quote_object = quote
    return {"quote": quote, "quote_id": quote_id}


@app.post("/quotes/")
def create_quote(quote):
    id_ = len(ALL_QUOTES) + 1
    return {"quote": quote, "quote_id": id_}


@app.delete("/quotes/{quote_id}")
def delete_quote(quote_id):
    quote = ALL_QUOTES[int(quote_id)]
    del ALL_QUOTES[int(quote_id)]
    return {"quote": quote, "quote_id": quote_id}


def quotes():
    return ALL_QUOTES
