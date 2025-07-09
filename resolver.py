import trio
import dns.message
import dns.asyncquery
import dns.asyncresolver
from utility import *

#resolver = dns.asyncresolver.Resolver()

async def resolve_name(name: str):
    response = await dns.asyncresolver.resolve(name)
    return response

def resolve_names(names: list, debug:bool=False) -> dict:
    inter_buff = {}
    if (debug):
        print(utility.prepare_string("Initiating continer for results...", utility.debug))
    for i in names:
        inter_buff.update({i:[]})
    for i in names:
        try:
            if (debug):
                print(utility.prepare_string("Resolving "+ i, utility.debug))
            response = trio.run(resolve_name,i)
        except:
            continue
        for j in response:
            inter_buff[i].append(j.to_text())
    return_buff = {}
    for i in inter_buff.keys():
        if(len(inter_buff[i]) > 0):
            return_buff.update({i:inter_buff[i]})
    return return_buff