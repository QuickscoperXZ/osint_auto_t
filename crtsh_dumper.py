import requests
import csv
from utility import utility

class crtsh_dumper:
    def dump(target_domain:str, debug:bool=False):
        target = utility.crtsh_url + target_domain
        if (target_domain != ""):
            try:
                crtsh_response = requests.get(target,timeout=5)
                if (debug):
                    print(utility.prepare_string("CSV returned: ", utility.debug))
                    print(crtsh_response.text)
               # print(prepare_string(crtsh_response.text,info))
                if (crtsh_response.status_code != 200):
                    raise Exception()
            except:
                return utility.prepare_string("Error receiving request", utility.error)
            response_reader = csv.DictReader(crtsh_response.text.split("\n"))
        if (debug):
            print(utility.prepare_string("Parsing csv:", utility.debug))
            print(type(response_reader))    
        return response_reader

    def prepare_sans(crtsh_dump: csv.DictReader, target_domain: str, debug:bool=False) -> list:
        buff = []
        sans = []
        try:
            for i in crtsh_dump:
                buff += (i['Matching Identities'].split(target_domain))
        except:       
            print(utility.prepare_string("Something went wrong during preparing process, exiting...", utility.error))
            print(buff)

        if (debug):
            print(utility.prepare_string("Intermidiate results of identities separation: ", utility.debug))
            print(buff)

        for i in buff:
            sans.append(i+target_domain)
        
        if (debug):
            print(utility.prepare_string("Prepare finished:", utility.debug))
            print(sans)
        return sans

    def deduplicate_names(SANs: list, target_domain:str) -> list:
        deduplicated_et = list(set(SANs))
        return_set = []
        for i in deduplicated_et:
            if ("*." not in i):
                return_set.append(i)
        return return_set

    