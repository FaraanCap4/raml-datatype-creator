from json import loads

JSON_DATA = """

[{
"id": 0,
"name": "string",
"released": "2023-12-19",
"rating": 0,
"platforms": [
  "string"
]
},
{
"id": 1,
"name": "string",
"released": "2023-12-19",
"rating": 0,
"platforms": [
  "string"
]
}]


"""



#TODO : add date type
def create_datatype_rec (data: any, raml: str = '#%RAML 1.0 DataType', level: int = 0, tab: str = '  ') -> str :
    """creates RAML datatype recursively from python data"""
    tabs = ''.join(tab for i in range(level))

    if type(data) == dict :
        if data == {} : return raml+ " object\n"    #if object is not defined
        raml = f'{raml}\n{tabs}type: object\n{tabs}properties:\n'   #if object is defined we must add it's properties
        tabs = tabs + tab
        for k,v in data.items() :
            raml = create_datatype_rec(v, raml + tabs + k + ':', level+2, tab)  #foreach key in object, find type of it's value
        return raml
    elif type(data) == list :   #if list empty : array, else we must define the array's items type
        return raml+' array\n' if data == [] else create_datatype_rec(data[0], f'{raml}\n{tabs}type: array\n{tabs}items:', level+1, tab)
    elif type(data) == str:
        return raml+" string\n"
    elif type(data) == int:
        return raml+" number\n"
    elif type(data) == float:
        return raml+" number\n"
    else :
        return raml+' #unsuported type\n'

def json_to_datatype(data :str) -> str :
    """creates RAMl datatype from json string"""
    return create_datatype_rec(loads(data))

print(json_to_datatype(JSON_DATA))
