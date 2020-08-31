const capitalize = (s) => {
  if (typeof s !== 'string') return ''
  return s.charAt(0).toUpperCase() + s.slice(1)
}

function chooseMonth(clicked_id) {
    month = capitalize(clicked_id)
    elements = document.querySelectorAll('[id=block]');

    for (var i = 0; i < elements.length; i++) {
        if (String(elements[i].children[0].children[0].children[1].children[0].children[1].children[3].innerHTML) != String(month)) {
        elements[i].style.display = "none";
        }
    }
}