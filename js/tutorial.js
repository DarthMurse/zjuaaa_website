var chapter_list = ['part1/chapter1/chapter1.md', 'part1/chapter2/chapter2.md', 'part1/chapter3/chapter3.md', 'part2/chapter4/chapter4.md', 'part2/chapter5/chapter5.md', 'part3/chapter6/chapter6.md', 'part3/chapter7/chapter7.md'];
var title_dict = ['1111', '2222', '3333', '4444', '5555', '6666', '7777'];
var current_num = 0;

function showMarkdown(num) 
{
	const app = document.getElementById('md');
    app.src = 'markdown/'+chapter_list[num];
  	app.render({
    // The class `line-numbers` will be added to the markdown-body container
    classes: 'line-numbers',
    // These are Marked options
    gfm: false,
    mangle: false
    });
	document.getElementById('chapter').innerHTML = title_dict[num];
	current_num = num;
}

function former()
{
	if (current_num != 0)
	{
		current_num -= 1;
		showMarkdown(current_num);
	}
}

function latter()
{
	if (current_num < chapter_list.length-1)
	{
		current_num += 1;
		showMarkdown(current_num);
	}
}
