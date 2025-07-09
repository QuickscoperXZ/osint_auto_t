from wappalyzer import analyze

results = analyze('https://talcom.ru',scan_type='balanced')

for i in results['https://talcom.ru']:
    print(i)

#print(results)