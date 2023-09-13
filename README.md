# zjuaaa_website
A repository to store all the codes and resources for the Zhejiang University Amateur Astronomy Association website.ion

## 注意事项
各位在项目里新建文件夹的时候请在这里标注一下文件夹的内容和功能：  

+ img: 用于存放各种图片，命名时请加上页面前缀，如`tutorial_logo.png`代表`tutorial.html`中引用的图片。
+ js: 用于存放各种javascript代码，命名规则同上。
+ css: 用于存放各种css文件，命名规则同上。
+ maintain: 用于存放各种用于维护的代码，如一些python脚本，命名规则同上。
+ markdown: 用于保存科普知识分享中的各种markdown文件。含有三个子目录对应三个大章节，每个大章节中的小节目录存放需要展示的markdown文件和其中用到的各种资源
每个目录中的`title.txt`内填写改节的名称（不直接用名称命名文件夹是为了防止中文无法识别）。
+ font: 用于保存网页中用到的各种字体（防止用户本机没有导致网页不能达到预期效果），用字体本身的名字命名，如`MicrosoftYaHei.ttf`。

## 更新记录

8.28 18:07 hyz

按照概念图设计了「天文科普」板块(`article.html`)，选用的图片来自我玩的游戏，不知道上传到 Github 版权有没有问题。

左右滑动部分采用了现成的 `slick slider` 提供的内容(`slick`文件夹)，同网页文件上传了。

---
8.28 18：43 lk

添加了尾页

---
8.28 23:16 pb

添加了照片页面，随便做了做，用于测试

---
9.5 12:59 zzy

初步设计了电脑端知识分享的页面，有部分代码还没有完成，先保存上传一下

---
9.6 20:47 pb

初步设计单张照片展示的页面

---
9.6 22:44 zzy

基本上完成知识分享页面的设计（包括pc、平板和手机端），未来可能需要针对手机端进行一些设计上的改进（手机字体较小）。
知识分享的markdown放`markdown`目录下，更新后运行`maintain`目录下的`update_tutorial_html.py`以更新内容。

---
9.6 23:29 hyz

完成了活动页的设计，和后台维护 python 程序 `article_change.py`, 数据存在 `article_content.json` 里。程序内含说明。

---
9.9 23:16 zzy

完成了联系我们页面的设计

---
9.13 15:39 pb

完成了图库页和详情页的设计。图片页面都需要挂载才能工作。图片信息列表要/masterpiece/image_information.json

