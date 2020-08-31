const capitalize = (s) => {
  if (typeof s !== 'string') return ''
  return s.charAt(0).toUpperCase() + s.slice(1)
}

var used_flag = false;

function chooseMonth(clicked_id) {
    month = capitalize(clicked_id);
    elements = document.querySelectorAll('[id=block]');
    counter = 0;
    console.log(used_flag)


    if (String(month) == 'Year') {
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.display = "block";
            used_flag = false;
        }
    } else {
        for (var i = 0; i < elements.length; i++) {
            if (String(elements[i].children[0].children[0].children[1].children[0].children[1].children[3].innerHTML) != String(month)) {
                elements[i].style.display = "none";
            } else {
                elements[i].style.display = "block";
            }
        }
    }
}