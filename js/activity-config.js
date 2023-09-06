var eveve = {
	event: [
		{
			name: "秋季纳新",
			details: "报名方式：链接",
			time: [
				"09/01",
				"09/01"
			]
		}
	]
};
var article = {
	article: [
		{
			type: "社会实践",
			name: "探寻戈壁“孤星”冷湖天文观测基地",
			details: "浙江大学学生天文爱好者协会赴青海冷湖天文台暑期社会实践团总结",
			picture: "<img src=\"./img/icon_13.png\" alt=\"探寻戈壁“孤星”冷湖天文观测基地\" />"
		}
	]
};


let eve = template("news-list", eveve);
let art = template("article-list", article);
document.getElementById("news-list").innerHTML = eve;
document.getElementById("article-list").innerHTML = art;
