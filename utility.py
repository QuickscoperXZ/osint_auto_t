import xlsxwriter
import ipaddress
import wappalyzer

class utility:
    def prepare_string(input: str, status: str) -> str:
        return status + input + "\033[!p"

    def print_resolving(input: dict, invert:bool):
        if invert:
            input = utility.invert_match(input)
            input = utility.prepare_inverted(input)
        for i in input.keys():
            print(utility.prepare_string(str(i) + ": " + str(input[i]), utility.success))

    def invert_match(input:dict) -> dict:
        all_ips_in = []
        for i in input.keys():
            for j in input[i]:
                all_ips_in.append(j)
        all_ips = list(set(all_ips_in))
        inverted_dict = {}
        for i in all_ips:
            inverted_dict.update({i:[]})
        for i in inverted_dict.keys():
            for j in input.keys():
                if (i in input[j]):
                    inverted_dict[i].append(j)
        return(inverted_dict)
        
    def prepare_inverted(input:dict)->dict:
        ip_list = input.keys()
        ip_list_sorted = sorted(ip_list, key=lambda i: int(ipaddress.ip_address(i)))
        return_dict = {}
        for i in ip_list_sorted:
            return_dict.update({str(i):input[str(i)]})
        return return_dict

    def wappalyze(url:str,thrds:int) -> str:
        wappalyzer_results = wappalyzer.analyze(url,scan_type='balanced',threads=thrds)
        return_buff = ""
        for i in wappalyzer_results[url]:
            return_buff = return_buff + str(i) + "\n"
        return return_buff
    
    def wappalyze_list(input:list, thrds:int) -> str:
        pre_buff = ""
        print(utility.prepare_string("Starting wappalyzer...", utility.info))
        for i in input:
            print(utility.prepare_string("Wappalyzing " + i, utility.info))
            pre_buff = pre_buff + utility.wappalyze("http://"+i,thrds)
        return_buff_pre = pre_buff.split('\n')
        return_buff_pre = list(set(return_buff_pre))
        return_buff = ""
        for i in return_buff_pre:
            return_buff = return_buff + i + '\n'
        return return_buff
    
    success = "\033[32m[+]: "
    info = "\033[36m[!]: "
    error = "\033[31m[-]: "
    debug = "\033[33m[Debug]: "

    crtsh_url = "https://crt.sh/csv?q="

class exporter:
    def save_to_text(input: dict, target_path: str):
        with open(target_path, "w+") as file:
            for i in input.keys():
                file.write((str(i) + ":" + str(input[i]) + "\n").replace('\'','',-1).replace('[','',-1).replace(']','',-1).replace(' ','',-1).replace(',',', ',-1))

    def save_to_csv(input:dict, target_path:str):
        with open(target_path,"w+") as file:
            for i in input.keys():
                file.write((str(i) + "," + str(input[i]) + "\n").replace('\'','',-1).replace(' ','',-1))

    def prepare_xlsx(input:dict, target_path:str, wappalyze:bool, thrds:int):
        input = utility.invert_match(input)
        input = utility.prepare_inverted(input)
        workbook = xlsxwriter.Workbook(target_path+".xlsx")
        worksheet = workbook.add_worksheet()

        worksheet.write('A1', 'IP')
        worksheet.write('B1', 'PORT')
        worksheet.write('C1', 'TECH')
        worksheet.write('D1', 'DOMAIN')
        worksheet.write('E1', 'COMM')

        iterator = 2
        for i in input.keys():
            if (len(input[i]) > 1):
                iterator_before = iterator
                for j in input[i]:
                    worksheet.write('A'+str(iterator), i)
                    worksheet.write('D'+str(iterator), j)
                    iterator+=1
                worksheet.merge_range('A'+str(iterator_before)+':'+'A'+str(iterator-1),data=i)
                worksheet.merge_range('B'+str(iterator_before)+':'+'B'+str(iterator-1),data='')
                techs = ''
                if (wappalyze):
                    techs = utility.wappalyze_list(input[i], thrds)
                worksheet.merge_range('C'+str(iterator_before)+':'+'C'+str(iterator-1),data=techs)
            else:
                worksheet.write('A'+str(iterator), i)
                worksheet.write('D'+str(iterator), input[i][0])
                iterator+=1
        workbook.close()

#print(exporter.prepare_to_xls({1:'asdasd', 2:'asdasdasd', 4:'asqweqwe', 3:'apfppp'}))