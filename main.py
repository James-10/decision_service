from ariadne import QueryType, make_executable_schema, gql
from ariadne.asgi import GraphQL
import requests





query = QueryType()

@query.field("predictHousePrice")
def resolve_predict_house_price(_, info, features):
    
    response = requests.post("http://localhost:8000/predict/", json=features)
    result = response.json()
    return {"price": result["price"]}

@query.field("predictLGD")
def resolve_predict_lgd(_, info, features):

    response = requests.post("http://localhost:8000/predict-lgd/", json=features)
    result = response.json()
    return {"lgd": result["lgd"]}


schema = make_executable_schema(type_defs, query)


app = GraphQL(schema)
