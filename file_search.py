import os, re

pwd = os.getcwd()
configs = os.listdir(pwd+'\\Files')

with open('search keywords.txt') as search_file:
    search_list = search_file.read().splitlines()

for config in configs:
    print("Searching in "+config)
    file_path = 'Files\\'+config
    with open(file_path) as cf:
        cf_content = cf.read()
        for ip in search_list:
            start_index = cf_content.find(ip)
            end_index = cf_content.find(' ',start_index)
            print(cf_content[start_index:end_index+1])