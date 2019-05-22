
# LIMIT = 200000
# file_count = 0
# url_list = []
#
# with open("xyt/xyt_cn") as f:
#     for line in f:
#         url_list.append(line)
#         if len(url_list)< LIMIT:
#             continue
#         filr_name ="xyt_cn" +  str(file_count)+".excel"
#         with open(filr_name,'w') as file:
#             for url in url_list[:-1]:
#                 file.write(url)
#             file.write(url_list[-1].strip())
#             url_list = []
#             file_count += 1
#     if url_list:
#         filr_name ="xyt_cn" + str(file_count)+".excel"
#         with open(filr_name,"w") as file:
#             for url in url_list:
#                 file.write(url)
#     print('done')



