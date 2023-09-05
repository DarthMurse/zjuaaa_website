import os 

def getMD():
    parts = os.listdir("markdown/")
    chapter_dict = dict()
    for part in parts:
        chapters = os.listdir("markdown/"+part+"/")
        chapters.remove("title.txt")
        chapter_dict[part] = chapters
    return parts, chapter_dict

def getTitle(path):
    with open(path+'/title.txt', 'r') as f:
        title = f.readline()
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
        if "<span id="chapter">" in content[i]:
            return i

if __name__ == "__main__":
    HTML = "tutorial.html"
    with open(HTML, "r") as f:
        content = f.readlines()
    start, end = findOuterUL(content)
    print(content)
