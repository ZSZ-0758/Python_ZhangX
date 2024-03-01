import sys
import csv
import json
if sys.argv[1]=='-b':
    with open(sys.argv[2],'r',encoding='utf-8',newline='') as csvf:
        moviesinfo=csvf.readlines()
    #读取csv文件
    n=len(moviesinfo)
    #计算信息条数
    menulist=moviesinfo[0]
    menulist=menulist.replace('\r','').replace('\n','')
    if 'movie_author1' in menulist:
        menulist=menulist.replace('movie_author1','movie_author')
    menulist=menulist.split(',')
    if 'movie_author2' in menulist:
        menulist.remove('movie_author2')
    #获取菜单
    #此处需要合并author1,author2
    result_dict={}
    result=[]
    for i in range(1,n): 
        infolist=moviesinfo[i]
        infolist=infolist.replace('\r','').replace('\n','')
        infolist=infolist.split(',')
        #infolist为单条电影信息
        #menulist为键信息
        #result_dict存将传入json的信息
        #result存储最终结果
        j=0
        for every in menulist:
            if every == 'movie_author':
                templist=[]
                templist.append(infolist[j])
                j+=1
                templist.append(infolist[j])
                j+=1
                if '' in templist:
                    templist.remove('')
                result_dict[every]=templist
            #此处需要合并author1,author2
            else:
                if every == 'movie_rating':
                    result_dict[every]=float(infolist[j])
                else:
                    result_dict[every]=infolist[j]
                j+=1
        result.append(dict(result_dict))
    with open(sys.argv[2].split('.')[0]+'.json','w',encoding='utf-8') as f:
        f.write(json.dumps(result,indent=4,ensure_ascii=False))
#写入json
elif sys.argv[1]=='-p':
    with open(sys.argv[2],'r',encoding='utf-8',newline='') as jsonf:
        moviesinfo=list(json.load(jsonf))
    #读取json文件
    n=len(moviesinfo)
    #取信息条数
    menu=[]
    menuinfo=moviesinfo[0]
    menuinfo=dict(menuinfo)
    for key in menuinfo.keys():
        if key =='movie_author':
            menu.append('movie_author1')
            menu.append('movie_author2')
        else:
            menu.append(key)
    #取菜单栏键列表
        with open(sys.argv[2].split('.')[0]+'.csv','w',encoding='utf-8',newline='')as f:
            writecsv=csv.writer(f)
            writecsv.writerow(menu)
            #写入菜单栏键
            for i in range(0,n):
                resultinfo=[]
                j=0
                for value in moviesinfo[i].values():
                    if type(value)==list:
                        for every in value:
                            resultinfo.append(every)
                        if len(value)==1:
                            resultinfo.append('')
                    else:
                        resultinfo.append(value)
                writecsv.writerow(resultinfo)
#写入csv