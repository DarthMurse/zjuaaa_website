function getCatalog() {
	console.log("See markdown folder");
	fs.readdir("markdown/", function(err, files){
		if (err) {
			return console.error(err);
		}
		files.forEach(function(file) {
			console.log(file);
		});
	});
}

function loadMD(path) {
	
}
