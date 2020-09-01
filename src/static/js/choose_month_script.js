const capitalize = (s) => {
  if (typeof s !== 'string') return ''
  return s.charAt(0).toUpperCase() + s.slice(1)
}

var chosen_year
var chosen_month

function chooseMonth(clicked_id) {
    month = capitalize(clicked_id);
    elements = document.querySelectorAll('[id=block]');


    if (String(month) == 'Year') {
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.display = "block";
        }
    } else {
        for (var i = 0; i < elements.length; i++) {
            if (String(elements[i].children[0].children[0].children[1].children[0].children[1].children[3].innerHTML) == String(month) &&
                String(elements[i].children[0].children[0].children[1].children[0].children[1].children[4].innerHTML) == String(chosen_year)) {
                elements[i].style.display = "block";
            } else {
                elements[i].style.display = "none";
            }
        }
    }
}

function chooseYear(clicked_id) {
    year = capitalize(clicked_id);
    chosen_year = year
    elements = document.querySelectorAll('[id=block]');

    console.log(String(year))
    if (String(year) == 'All') {
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.display = "block";
        }
    } else {
        for (var i = 0; i < elements.length; i++) {
            if (String(elements[i].children[0].children[0].children[1].children[0].children[1].children[4].innerHTML) == String(year) &&
                String(elements[i].children[0].children[0].children[1].children[0].children[1].children[3].innerHTML) == String(chosen_month)) {
                elements[i].style.display = "block";
            } else {
                elements[i].style.display = "none";
            }
        }
    }
}

