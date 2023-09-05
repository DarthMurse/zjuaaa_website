import os 

ROOT_PATH = "../markdown/"

def getMD():
    parts = os.listdir(ROOT_PATH)
    chapter_dict = dict()
    for part in parts:
        chapters = os.listdir(ROOT_PATH+part+"/")
        chapters.remove("title.txt")
        chapter_dict[part] = chapters
    return parts, chapter_dict

def getTitle(path):
    with open(path+'/title.txt', 'r') as f:
        title = f.readline()
    title = title[0: -1]
    return title

def findOuterUL(content):
    start, end = 0, 0
    n = len(content)
    for i in range(n):
        if "<ul" in content[i]:
            start = i
            break
    for i in range(n):
        if "</ul>" in content[n-i-1]:
            end = n-i-1
            break
    return start, end

def findChapterSpan(content):
    for i in range(len(content)):
        if "<span id=\"chapter\">" in content[i]:
            return i

def getChapterList(parts, chapter_dict):
    chapter_list = []
    title_list = []
    for part in parts:
        for chapter in chapter_dict[part]:
            name = part + '/' + chapter + '/' + chapter + '.md'
            chapter_list.append(name)
            title_list.append(getTitle(ROOT_PATH+part+'/'+chapter))
    return chapter_list, title_list

def getNum(part, chapter, full_chapter_list):
    full = part + '/' + chapter + '/' + chapter + '.md'
    result = -1
    for i in range(len(full_chapter_list)):
        if full == full_chapter_list[i]:
            result = i
            break
    return result

def writePart(part):
    result = "\t\t\t\t<li>" + getTitle(ROOT_PATH+part) + "</li>\n"
    return result

def writeChapter(part, chapter_list, full_chapter_list):
    result = []
    result.append("\t\t\t<ul class=\"second\">\n")
    for chap in chapter_list:
        line = "\t\t\t\t<li><a href=\"#\" onClick=\"showMarkdown(" + str(getNum(part, chap, full_chapter_list)) + ")\">" + getTitle(ROOT_PATH+part+'/'+chap) + "</a></li>\n"
        result.append(line)
    result.append("\t\t\t</ul>\n")
    return result

if __name__ == "__main__":
    HTML = "../tutorial.html"
    JS = "../js/tutorial.js"
    with open(HTML, "r") as f:
        content = f.readlines()
    with open(JS, 'r') as f:
        js_content = f.readlines()

    start, end = findOuterUL(content)
    parts, chapter_dict = getMD()
    parts.sort()
    for part in parts:
        chapter_dict[part].sort()
    chapter_list, title_list = getChapterList(parts, chapter_dict)
    span_num = findChapterSpan(content)

    new_html = []
    for i in range(start+1):
        new_html.append(content[i])
    for part in parts:
        new_html.append(writePart(part))
        new_html.extend(writeChapter(part, chapter_dict[part], chapter_list))

    for i in range(end, span_num):
        new_html.append(content[i])

    new_html.append("<span id=\"former\"><a href=\"#\" onClick=\"former()\">&larr; 上一节</a></span><span id=\"chapter\">"+getTitle(ROOT_PATH+'part1/chapter1')+"</span><span id=\"latter\"><a href=\"#\" onClick=\"latter()\">下一节 &rarr;</a></span>\n")
    
    for i in range(span_num+1, len(content)):
        new_html.append(content[i])
    
    new_js = []
    line = "var chapter_list = [\'" + chapter_list[0] + "\'"
    for i in range(1, len(chapter_list)):
        line += ", \'" + chapter_list[i] + "\'"
    line += ']\n'
    new_js.append(line) 

    line = "var title_list = [\'" + title_list[0] + "\'"
    for i in range(1, len(title_list)):
        line += ", \'" + title_list[i] + "\'"
    line += ']\n'
    new_js.append(line)

    for i in range(2, len(js_content)):
        new_js.append(js_content[i])

    with open('../tutorial.html', 'w') as f:
        f.writelines(new_html)
    with open('../js/tutorial.js', 'w') as f:
        f.writelines(new_js)
