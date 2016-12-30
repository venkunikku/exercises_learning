import pandas as pd
import json

def test():

    jsonn = '''\
    {"auditid":"123o923.apple",
            "date":"timestampd"
            "param":{
                        "order_id":"1238972"
                        "inventory_id":"238493"
                    }

            }
    '''

    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

    jj = json.loads(json_string)
    print(jj)

    df = pd.read_json(jj)
    print(json_string)

if __name__ == '__main__':
    test()