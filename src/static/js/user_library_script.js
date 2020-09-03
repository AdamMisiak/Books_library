function chooseUsername(clicked_id) {
    console.log(clicked_id)
    var data = {'username': clicked_id};

    $.get("/users/user_library/", data);
}