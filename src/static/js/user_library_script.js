const capitalize = (s) => {
  if (typeof s !== 'string') return ''
  return s.charAt(0).toUpperCase() + s.slice(1)
}

function chooseUsername(clicked_id) {
    username = capitalize(clicked_id);
    alert(username)

}