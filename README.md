# Autosint
## RU
Инструмент для автоматизации некоторых надоедающих задач при осинте.

Возможности:
- Дамп CSV с crt.sh
- Разрешение имен в адреса
- Поиск веб-технологий с помощью Wappalyzer
- Подготовка микро-отчета в текстовом формате, CSV или форматированном XLSX файле

Использование:
```
Autosint.py [-h] [-d] [-n] [-oT OT] [-oC OC] [-oX OX] [-i] [-w] [-wt WT] target_domain
Automates some boring af osint tasks
positional arguments:
  target_domain
options:
  -h, --help          show this help message and exit
  -d, --debug         Enables debug messages
  -n, --no-resolve    Disables resolving names
  -oT OT              Export output to txt file (no specific sepparation)
  -oC OC              Export output to csv file
  -oX OX              Prepare and export results into formated Excel-compatible file
  -i, --invert-match  Invert list matching from DOMAIN:IP to IP:DOMAIN (usefull)
  -w, --wappalyze     Enables wappalyzer, scans resolved domain names for the web application technologies
  -wt WT              Sets wappalyzer thread count
```
### TODO:
- Добавить поддержку результатов с FOFA, Shodan, Censys, Netlas
- Добавить вывод данных о портах и проверку к ним

## EN
Tool to automate some boring osint tasks

Features:
- CSV dump from crt.sh
- Resolving domain names
- Scan for web application technologies with Wappalyzer
- Creating text, csv or XLSX report

Usage:
```

Autosint.py [-h] [-d] [-n] [-oT OT] [-oC OC] [-oX OX] [-i] [-w] [-wt WT] target_domain
Automates some boring af osint tasks
positional arguments:
  target_domain
options:
  -h, --help          show this help message and exit
  -d, --debug         Enables debug messages
  -n, --no-resolve    Disables resolving names
  -oT OT              Export output to txt file (no specific sepparation)
  -oC OC              Export output to csv file
  -oX OX              Prepare and export results into formated Excel-compatible file
  -i, --invert-match  Invert list matching from DOMAIN:IP to IP:DOMAIN (usefull)
  -w, --wappalyze     Enables wappalyzer, scans resolved domain names for the web application technologies
  -wt WT              Sets wappalyzer thread count
```
### TODO:
- Add FOFA, Shodan, Censys, Netlas support
- Add port data and port checker
