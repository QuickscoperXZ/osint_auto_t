from crtsh_dumper import crtsh_dumper
from utility import utility, exporter
import argparse
import resolver
import trio

#argparse
parser = argparse.ArgumentParser(
    prog="Autosint.py",
    description="Automates some boring af osint tasks"
) 
parser.add_argument('target_domain')
parser.add_argument('-d', '--debug',help='Enables debug messages',action='store_true')
parser.add_argument('-n', '--no-resolve', help='Disables resolving names', action='store_true')
parser.add_argument('-oT', help='Export output to txt file (no specific sepparation)')
parser.add_argument('-oC', help='Export output to csv file')
parser.add_argument('-oX', help='Prepare and export results into formated Excel-compatible file')
parser.add_argument('-i', '--invert-match', help='Invert list matching from DOMAIN:IP to IP:DOMAIN (usefull)', action='store_true')
parser.add_argument('-w','--wappalyze', help='Enables wappalyzer, scans resolved domain names for the web application technologies', action='store_true')
parser.add_argument('-wt', help='Sets wappalyzer thread count')
args = parser.parse_args()

#args
target_domain = args.target_domain
debug = args.debug
nresolve = args.no_resolve
text_ouput = args.oT
csv_output = args.oC
xsl_output = args.oX
invert = args.invert_match
walyze = args.wappalyze
walyzeth = args.wt

#main
if (walyze):
    print(utility.prepare_string("ATTENTION! Wappalyzing may take a while (around 30 to 50 s per site)", utility.info))
print(utility.prepare_string("Starting dumping data for " + target_domain, utility.info))
dump = crtsh_dumper.dump(target_domain, debug)
names = crtsh_dumper.prepare_sans(dump, target_domain,debug)
names = crtsh_dumper.deduplicate_names(names, target_domain)
print(utility.prepare_string("Found "+ str(len(names))+" domains", utility.info))
if (not nresolve or xsl_output is not None): 
    print(utility.prepare_string("Resolving names", utility.info))
    resolved_addresses = resolver.resolve_names(names)
    utility.print_resolving(resolved_addresses,invert)
else:
    for i in names:
        print(utility.prepare_string(i,utility.success))

if (text_ouput is not None):
    print(utility.prepare_string("Printing text...", utility.info))
    if (invert):
        exporter.save_to_text(utility.invert_match(resolved_addresses), text_ouput)
    else:
        exporter.save_to_text(resolved_addresses,text_ouput)
if (csv_output is not None):
    print(utility.prepare_string("Printing csv...", utility.info))
    if (invert):
        exporter.save_to_csv(utility.invert_match(resolved_addresses),csv_output)
    else:
        exporter.save_to_csv(resolved_addresses, csv_output)
if (xsl_output is not None):
    print(utility.prepare_string("Preparing xlsx...", utility.info))
    exporter.prepare_xlsx(resolved_addresses, xsl_output, walyze, walyzeth)
