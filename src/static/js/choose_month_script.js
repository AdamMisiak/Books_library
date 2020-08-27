const capitalize = (s) => {
  if (typeof s !== 'string') return ''
  return s.charAt(0).toUpperCase() + s.slice(1)
}

function chooseMonth(clicked_id) {
    month = capitalize(clicked_id)
    console.log(month)
    elements = document.querySelectorAll('[id=month]');
    for (var i = 0; i < elements.length; i++) {
        if (String(elements[i].innerHTML) == String(month)) {
        console.log('test')
        }
        console.log(elements[i].innerHTML);
    }
}