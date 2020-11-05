pip install python-Levenshtein

!pip install fastapi nest-asyncio pyngrok uvicorn

from typing import Optional
from fastapi import FastAPI
import sys
import nest_asyncio
from pyngrok import ngrok
import uvicorn

from google.colab import files
src = list(files.upload().values())[0]
open('org_country.ipynb','wb').write(src)
from org_country import type_identification

app=FastAPI()

@app.get("/items")
def read_item(search_term: str, rel_score:Optional[float]):
  org_place=type_identification()
  get_org_india=org_place.get_org_india(search_term,rel_score)
  get_org_UK=org_place.get_org_UK(search_term,rel_score)

  if get_org_UK<rel_score and get_org_india>=rel_score:
    return {"organistion":search_term,"org_loc":"India"}

  elif get_org_india<rel_score and get_org_UK>=rel_score:
    return {"organistion":search_term,"org_loc":"United Kingdom"}

  elif get_org_india>=rel_score and get_org_UK>=rel_score and get_org_UK==get_org_India:
    return {"organistion":search_term,"org_loc":"Both country UK and India"}

  else:
    return {"organistion":search_term,"org_loc":"Different Country"}

!ngrok authtoken XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

public_url = ngrok.connect(port='8080')
public_url

#ngrok.kill()

nest_asyncio.apply()
uvicorn.run(app, port=80)