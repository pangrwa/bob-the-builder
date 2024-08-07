from fastapi import FastAPI, Request, HTTPException
from json_dfa import JSONDFA
from json_parser import JSONParser
from io import BytesIO, TextIOWrapper
from main import scan, parse
from json_exceptions import JSONDFAException, JSONParserException

app = FastAPI()
json_dfa = JSONDFA()
json_parser = JSONParser()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/parse")
async def parse_text(request: Request):
    raw_bytes = await request.body()
    buffer = BytesIO(raw_bytes)
    buffer = TextIOWrapper(buffer, encoding="utf-8")
    try:
        tokens = scan(buffer)
        fi = json_parser.parse(tokens)
        return fi
    except JSONDFAException as e:
        raise HTTPException(status_code=400, detail=str(e.message))
    except JSONParserException as e:
        raise HTTPException(status_code=400, detail=str(e.message))
