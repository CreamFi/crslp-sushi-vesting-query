import requests
import math
from datetime import datetime

CREAM_SUBGRAPH_URL = 'https://api.thegraph.com/subgraphs/name/creamfinancedev/cream-portfolio-mainnet'
BLOCKLYTICS_SUBGRAPH_URL = 'https://api.thegraph.com/subgraphs/name/blocklytics/ethereum-blocks'

mint_event_query = """
{
  mintEvents(where: {cToken: "0x73f6cBA38922960b7092175c0aDD22Ab8d0e81fC"}){
    id,
    cToken
  }
}
"""
# params = {'query':mint_event_query}
# res = requests.post(SUBGRAPH_URL,json=params)
# print(res.json())


def datetime_to_block(datetime_obj=None):
    datetime_obj = datetime.now() if datetime_obj is None else datetime_obj
    timestamp = int(datetime.timestamp(datetime_obj))
    query = f"{{blocks(first: 1, orderBy: timestamp, orderDirection: desc, where: {{ timestamp_lte: {timestamp} }}) {{number}}}}"
    params = {'query':query}
    result = requests.post(BLOCKLYTICS_SUBGRAPH_URL, json=params)
    return result.json()['data']['blocks'][0]['number']

