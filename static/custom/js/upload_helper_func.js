// Scroll down
$(`#jump_to_result`).click(function(e) {
    e.preventDefault();
    var aid = $(this).attr("href");
    $('html,body').animate({scrollTop: $(aid).offset().top}, 1000);
});

// handle event when select image btn was clicked
select_img = function(input_id) {
    $(`#${input_id}`).click();
}

function send_img(data) {
    var form_data = new FormData($(`form#${data.form_id}`)[0]);
    form_data.append('is_custom', data.is_custom)
    $.when(ajax_request(data.route, form_data))
        .then( data =>{
            console.log(data);
            show_result('origin_img', 'predict_img', data);
        });
}

function ajax_request(url, form_data) {
    return $.ajax({
        url: url,
        method: 'POST',
        data: form_data,
        dataType: 'json',
        processData: false,
        contentType: false
    });
}




function show_result(origin_id, predict_id, data) {
    // Get origin div & predict div
    origin_div = $(`#${origin_id}`);
    predict_div = $(`#${predict_id}`);
    // Create div content
    origin_title = `<h3>Origin image</h3>`;
    predict_title = `<h3>Predict image</h3>`;
    // Create image elements
    data.origin_img = data.origin_img.split('\'')[1]
    data.predict_img = data.predict_img.split('\'')[1]
    origin_img = `<img style="width: 100%;" src="data:image/jpeg;base64,${data.origin_img}" alt="">`;
    predict_img = `<img style="width: 100%;" src="data:image/jpeg;base64,${data.predict_img}" alt="">`;
    // Create list object
    list_item = ``;
    data.predict_data.forEach( element =>{
        list_item += `<li class="list-group-item">${element[0]}: ${element[1]}</li>`;
    });
    predict_listobj = `
    <ul id="list_obj" class="list-group">${list_item}</ul>`;
    // Append elements
    // ORIGIN
    origin_div.append(origin_title);
    origin_div.append(origin_img);
    // PREDICT
    predict_div.append(predict_title);
    predict_div.append(predict_img);
    predict_div.append(predict_listobj);
}

function erase_result(origin_id, predict_id) {
    $(`#${origin_id}`).empty();
    $(`#${predict_id}`).empty();
}
