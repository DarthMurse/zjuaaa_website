# -*- coding: utf-8 -*-
import os
import json
import re
import math

class Event:
    def __init__(self) -> None:
        pass

jsonContent = {}
# "events" 键对应活动预告
# "article" 键对应天协动态
# "version" 对应修改版本, 用来作为更新 js 虚拟版本号的辅助功能

# 从文件中加载 json 数据, 置于 jsonContent 中
def loadJSON(filename):
    Jfile = open(filename, 'r', encoding='utf-8')
    content = Jfile.read()
    jsonContent = json.loads(content)
    # print(jsonContent)
    Jfile.close()
    return jsonContent

# 在终端按表格显示 jsonContent 数据
def displayRecord():
    print("当前内容:")
    # event part
    print("活动预告:")
    no = 0
    print("{0:1} | {1:^9} | {2:^19}-{3:^19} | {4}".format("序", "名", "起", "讫", "细则"))
    for event in jsonContent['event']:
        print("{0:02} | {1:^6} | {2:^20}-{3:^20} | {4}".format(no, event["name"], event["time"][0], event["time"][1], event["details"]))
        no = no + 1
    # trend part
    print("天协动态:")
    print("{0:1} | {1:^6} | {2:} |".format("序", "类", "名"))
    print("   | {0:} | {1}".format("细则", "图"))
    no = 0
    for article in jsonContent['article']:
        print("{0:02} | {1:^6} | {2:} |".format(no, article["type"], article["name"]))
        print("   | {0:} | {1}".format(article["details"], article["picture"]))
        no = no + 1

# 添加活动记录, time = [start_time, end_time] 是一个二元数组, 但时间格式是字符串
def addEvent(name, time, details):
    jsonContent['event'].append({"name": name, "details": details, "time": time})

# 添加天协动态
def addArticle(type, name, details, picture):
    jsonContent['article'].append({"type": type, "name": name, "details": details, "picture": picture})

# 删除活动记录
def removeEvent(id):
    jsonContent['event'].pop(id)

# 删除天协动态
def removeArticle(id):
    jsonContent['article'].pop(id)

# 从终端手动添加活动记录
def terminalAddEvent():
    str = input('请按 名称$起始时间$结束时间$细节 的格式输入信息, 并用 $ 符号分隔, 输入后按回车. 如细节中有链接, 请按html格式输入\n例: 路边天文$08/29 18:00$08/29 22:00$地点：<a href="./index.html">链接</a>\n')
    arr = str.split('$')
    if (len(arr) != 4):
        print("格式有误, 未处理")
        return -1
    addEvent(arr[0], [arr[1], arr[2]], arr[3])

# 从终端手动添加天协动态
def terminalAddArticle():
    str = input('请按 类型$名称$细节$图片 的格式输入信息, 并用 $ 符号分隔, 输入后按回车. 如细节中有链接, 请按html格式输入\n例: 社会实践$探寻戈壁“孤星”冷湖天文观测基地$浙江大学学生天文爱好者协会赴青海冷湖天文台暑期社会实践团总结$./img/icon_13.png\n')
    arr = str.split('$')
    if (len(arr) != 4):
        print("格式有误, 未处理")
        return -1
    addArticle(arr[0], arr[1], arr[2], arr[3])

# 从文件添加活动记录
def fileAddEvent(filename):
    data = open(filename, 'r', encoding='utf-8')
    result = data.readline()
    line = 0
    while result:
        line = line + 1
        arr = result.split('$')
        if (len(arr) != 4):
            print("行 {0} 格式有误, 已跳过".format(line))
            result = data.readline()
            continue
        addEvent(arr[0], [arr[1], arr[2]], arr[3])
        result = data.readline()

# 从文件添加天协动态
def fileAddArticle(filename):
    data = open(filename, 'r', encoding='utf-8')
    result = data.readline()
    line = 0
    while result:
        line = line + 1
        arr = result.split('$')
        if (len(arr) != 4):
            print("行 {0} 格式有误, 已跳过".format(line))
            result = data.readline()
            continue
        addArticle(arr[0], arr[1], arr[2], arr[3])
        result = data.readline()

# 把 jsonContent 编译成 JSON 格式
def encodeJSON():
    return json.JSONEncoder().encode(jsonContent)

# 保存数据, 并更新 activity-config.js 和 article_content.json
def saveData(jsonFilename, jsFilename, htmlFilename, tail):
    # global jsonContent
    print(jsonContent["version"])
    jsonContent["version"] = jsonContent["version"] + 1
    jsonFile = open(jsonFilename, "w", encoding="utf-8")
    json.dump(jsonContent, jsonFile, ensure_ascii=False, indent=2)
    jsonFile.close()
    # 更新 js 文件
    jsFile = open(jsFilename, "w", encoding="utf-8")
    print("var eveve = {\n\tevent: [", end = "", file=jsFile)
    first = True
    # eveve
    for events in jsonContent["event"]:
        if first:
            print("\n\t\t{", file=jsFile)
            first = False
        else:
            print(",\n\t\t{", file=jsFile)
        print('\t\t\tname: "{0}",'.format(events["name"]), file=jsFile)
        print('\t\t\tdetails: "{0}",'.format(events["details"]), file=jsFile)
        print('\t\t\ttime: [\n\t\t\t\t"{0}",\n\t\t\t\t"{1}"\n\t\t\t]'.format(events["time"][0], events["time"][1]), file=jsFile)
        print("\t\t}", end="", file=jsFile)
    print("\n\t]\n};", file=jsFile)
    # article
    print("var article = {\n\tarticle: [", end = "", file=jsFile)
    first = True
    for art in jsonContent["article"]:
        if first:
            print("\n\t\t{", file=jsFile)
            first = False
        else:
            print(",\n\t\t{", file=jsFile)
        print('\t\t\ttype: "{0}",'.format(art["type"]), file=jsFile)
        print('\t\t\tname: "{0}",'.format(art["name"]), file=jsFile)
        print('\t\t\tdetails: "{0}",'.format(art["details"]), file=jsFile)
        print('\t\t\tpicture: "<img src=\\"{0}\\" alt=\\"{1}\\" />"'.format(art["picture"], art["name"]), file=jsFile)
        print("\t\t}", end="", file=jsFile)
    print("\n\t]\n};", file=jsFile)
    print("", file=jsFile)
    print(tailString, file=jsFile)
    # 修改 html 文件, 为 script 添加版本号
    htmlFile = open(htmlFilename, "r", encoding="utf-8")
    lines = htmlFile.readlines()
    lines[-3] = '\t\t<script src="./js/activity-config.js?version=' + str(round(math.pi, jsonContent["version"])) + '"></script>\n'
    htmlFile.close()
    htmlFile = open(htmlFilename, "w", encoding="utf-8")
    for line in lines:
        htmlFile.write(line)


# 指令界面, 输出错误信息
def errCommand():
    print("指令有误, 输入 help 可获得帮助.")

if __name__ == "__main__":
    JS = "../js/activity-config.js"
    JSON = "./article_content.json"
    HTML = "../activity.html"
    jsonContent = loadJSON(JSON)
    displayRecord()

    # js 文件的尾巴
    tailString = '''
let eve = template("news-list", eveve);
let art = template("article-list", article);
document.getElementById("news-list").innerHTML = eve;
document.getElementById("article-list").innerHTML = art;'''

    while True:
        order = input('>')
        command = order.split()
        match command[0]:
            case "help":
                print(" add  | 从终端手动添加数据\n      | 后加一个参数, 表示类型(活动 event/动态 article). 随后会进入有指导的输入模式.\n      | 例如: add event 可从终端添加活动预告")
                print(" disp | 显示当前所有活动信息")
                print(" exit | 退出（不会自动保存）")
                print(" help | 打印帮助文段")
                print(" load | 从文件中读取数据\n      | 后加两个参数, 第一个表示类型(活动 event/动态 article), 后者为文件路径\n      | 例如: load event ./test.txt 可从 ./text.tst 中读取数据并加到活动预告中")
                print(" save | 将当前信息保存到 json 文件中, 并更新 js 和 html 以在网页显示新内容")
                print("  rm  | 删除记录\n      | 后加两个参数, 前者表示类型(活动 event/动态 article), 后者为编号, 可用 disp 指令查看编号")
                print("  ver | 查看当前记录的版本号, 可用 reset 重置")
                print(" reset| 重置版本号到 0")
            case "add":
                if (len(command) != 2):
                    errCommand()
                    continue
                if command[1] == "event":
                    terminalAddEvent()
                elif command[1] == "article":
                    terminalAddArticle()
                else:
                    errCommand()
            case "disp":
                displayRecord()
            case "exit":
                print("再见~")
                break
            case "save":
                saveData(JSON, JS, HTML, tailString)
            case "load":
                if (len(command) != 3):
                    errCommand()
                    continue
                if command[1] == "event":
                    fileAddEvent(command[2])
                elif command[1] == "article":
                    fileAddArticle(command[2])
                else:
                    errCommand()
            case "rm":
                if (len(command) != 3):
                    errCommand()
                    continue
                if command[1] == "event":
                    removeEvent(int(command[2]))
                elif command[1] == "article":
                    removeArticle(int(command[2]))
                else:
                    errCommand()
            case "ver":
                print(jsonContent["version"])
            case "reset":
                jsonContent["version"] = 0
            case _:
                errCommand()