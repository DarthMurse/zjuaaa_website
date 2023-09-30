$("#middle-image").on("click", function () {
    $('#LargeImageModal').modal('show');
});
$("#LargeImageModal").on("click", function () {
    $('#LargeImageModal').modal('hide');
});

$("#rightBarOpen").click(rightBarOpen);
$("#rightBarClose").click(rightBarClose);

function rightBarOpen() {
    $("#right-bar").css("margin-left", "0px");
    $("#main-page").css("margin-right", "0px");
    $("#rightBarClose").css("right", "300px");
    document.cookie = "rightBarOpened=true" + "; path=/";

};

function rightBarClose() {
    $("#right-bar").css("margin-left", "20px");
    $("#main-page").css("margin-right", "-320px");
    $("#rightBarClose").css("right", "-50px");
    document.cookie = "rightBarOpened=false" + "; path=/";
};

$(".right-nav-img").click(function () {
    var image_index = $(this).attr("img-index");
    get_nav_image_list(image_list, image_index);
    change_image(image_index);
    get_nav_image(nav_image_list, image_index);


    $(".right-nav-img").removeClass("selected");
    $(this).addClass("selected");
});



var image_list = [];
var nav_image_list = [];
var image_information_path = "/masterpiece/image_information.json";

async function start_function() {
    {
        const cookies = document.cookie.split(';');
        let rightBarOpened = "true";
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith('rightBarOpened=')) {
                rightBarOpened = cookie.substring(15);
                break;
            }
        }
        if (rightBarOpened == "true") {
            rightBarOpen();
        }
        else {
            $("#right-bar").css("transition", "0s");
            $("#main-page").css("transition", "0s");
            $("#rightBarClose").css("transition", "0s");
            rightBarClose();
            setTimeout(function () {
                $("#right-bar").css("transition", "0.3s");
                $("#main-page").css("transition", "0.3s");
                $("#rightBarClose").css("transition", "0.3s");
            }, 300);
        }
    }

    await $.getJSON(image_information_path, function (data) {
        $.each(data, function (image_name, image_information) {
            image_list.push(image_name);
        });
    });
    let current_img_id = "";

    const searchParams = new URLSearchParams(window.location.search);

    current_img_id = searchParams.get("img");

    if (current_img_id == undefined) {
        current_img_id = image_list[0];
    }

    await get_nav_image_list(image_list, current_img_id);

    await change_image(current_img_id);
    await get_nav_image(nav_image_list, current_img_id);
}

function get_nav_image_list(image_list, current_image) {
    var num_length = $(".right-nav-img").length;
    var num_before = Math.trunc((num_length + 1) / 2 - 1);
    var num_after = Math.trunc(num_length / 2);

    var current_image_index = image_list.indexOf(current_image);
    if (current_image_index < num_before) {
        nav_image_list = image_list.slice(0, num_length);
    }
    else if (current_image_index > image_list.length - 1 - num_after) {
        nav_image_list = image_list.slice(image_list.length - num_length, image_list.length);
    }
    else {
        nav_image_list = image_list.slice(current_image_index - num_before, current_image_index + num_after + 1);
    }
}

function change_image(image_index) {
    $.getJSON(image_information_path, function (result) {
        $.each(result, function (image, image_information) {
            if (image == image_index) {
                $.each(image_information, function (key, value) {
                    if ($.isPlainObject(value)) {
                        var isEmpty = true;
                        $.each(value, function (key, value) {
                            if (value != "") {
                                $("#" + key).css("display", "table-row");
                                isEmpty = false;
                            }
                            else {
                                $("#" + key).css("display", "none");
                            }
                            $("#" + key).children("td").text(value);
                        });
                        if (isEmpty == true) {
                            $("#" + key).parent().css("display", "none");
                        }
                        else {
                            $("#" + key).parent().css("display", "block");
                        }
                    }
                    else if (key == "image-name") {
                        $("#image-name-nav, #image-name-middle").text(value);
                    }
                    else {
                        if (value == "") {
                            $("#" + key).parent().parent().css("display", "none");
                        }
                        else {
                            $("#" + key).parent().parent().css("display", "block");
                        }
                        $("#" + key).attr("src", value)
                    }
                });
            }
        });
    });
}

function get_nav_image(nav_image_list, iamge_index) {
    $.getJSON(image_information_path, function (result) {
        for (var i = 0; i < nav_image_list.length; i++) {
            $("#right-bar-image" + (i + 1)).children("img").attr("src", result[nav_image_list[i]]["middle-image"]);
            $("#right-bar-image" + (i + 1)).attr("img-index", nav_image_list[i]);
            if (nav_image_list[i] == iamge_index) {
                $("#right-bar-image" + (i + 1)).addClass("selected");
            }
            else {
                $("#right-bar-image" + (i + 1)).removeClass("selected");
            }
        }
    });
}


start_function();

