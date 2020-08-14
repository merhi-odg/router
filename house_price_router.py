# fastscore.schema.0: house_price_router_schema_in
# fastscore.slot.1: in-use

import requests
import pandas as pd

# modelop.init
def begin():
    global lasso_engine, ridge_engine, urlendpoint
    lasso_engine = 'engine-ds-2'
    ridge_engine = 'engine-ds-3'
    urlendpoint = "/2/active/model/roundtrip/0/1"
    pass

# modelop.score
def action(data):
    data = pd.DataFrame([data])
    model_name = data["model_name"].iloc[0]
    data = data.drop(["model_name"], axis=1)
    data = data.to_dict(orient="records")
    
    if model_name.lower()=="ridge":
        out = callEngine(ridge_engine, data[0])
    
    elif model_name.lower()=="lasso":
        out = callEngine(lasso_engine, data[0])
    
    yield out
    
def callEngine(engine_name, payload):
    
    #url = "http://" + engine_name + ":8003" + urlendpoint + "?timeout=2000"
    url = 'http://7b4e4b9b-mocaasin-modelopi-4fff-690205531.us-east-2.elb.amazonaws.com/' + \
            engine_name + urlendpoint
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        
        return(response.content.decode('ascii'))
    
    else:
        
        return("Request Failed!")

# modelop.metrics
def metrics(datum):
    yield {"foo": 1}