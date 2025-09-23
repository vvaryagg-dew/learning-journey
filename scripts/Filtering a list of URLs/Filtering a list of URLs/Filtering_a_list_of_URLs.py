#Условие: Дан список строк с URL-адресами.
#Требуется: Найти только те, которые начинаются с "https://". 
#Убрать у них суффикс "/" на конце (если он есть).
#Сформировать новый список и вывести его.

url_list = ["http://example.com", "https://google.com/", "https://github.com", "ftp://fileserver.org/"]
lst = []

for url in url_list:
    if url.startswith("https://"):
        if url.endswith("/"):
            lst.append(url[:-1])
        else:
            lst.append(url)

print(lst)

#           ---(Первый вариант программы, плохой)---
#
#
#url_list = ["http://example.com", "https://google.com/", "https://github.com", "ftp://fileserver.org/"]
#lst = []
#for i in range(len(url_list)):
#    if url_list[i][-1] != '/' and url_list[i][:8] == "https://":
#        lst.append(url_list[i])
#    elif url_list[i][-1] == '/' and url_list[i][:8] == "https://":
#        lst.append(url_list[i][:-1])
#
#print(lst)