var image_list = [];
var image_information_path = "/masterpiece/image_information.json";

async function start_function() {

    await $.getJSON(image_information_path, function (data) {
        $.each(data, function (image_index, image_information) {
            image_list.push(image_index);
        });
    });
    await get_waterflow_image(image_list);

}

async function get_waterflow_image(image_list) {
    await $.getJSON(image_information_path, function (result) {
        for (var i = 0; i < image_list.length; i++) {
            var newDiv = document.createElement("div");
            newDiv.className = "col-sm-6 col-lg-4 col-xl-3 mb-4";
            newImgDiv = document.createElement("div");
            newImgDiv.className = "waterflow-images";
            newImg = document.createElement("img");
            newImg.className = "img-fluid";
            newImg.src = result[image_list[i]]["thumbnail-image"];
            newImg.setAttribute("img-index", image_list[i]);
            newImgDiv.appendChild(newImg);
            newDiv.appendChild(newImgDiv);

            $("#main-page .row").append(newDiv);

        }
    });
    var msnry = new Masonry("#main-page .row", {});

    await $(".waterflow-images img").imagesLoaded(async function (images) {
        await msnry.layout();
    });

    await $(".waterflow-images").on("click", function () {
        var img_index = $(this).children("img").attr("img-index");
        window.location.href = "/masterpiece/detail.html" + "?img=" + img_index;
    });

}

start_function();

