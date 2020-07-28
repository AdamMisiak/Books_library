
//AJAX SCRIPT TO SEND BOOK ID TO VIEW AND CHANGE CLASS AND TEXT OF BUTTON
$('.addbutton').click(function(){
var id;
id = $(this).attr("data-catid");
$.ajax(
  {
    type:"GET",
    url: '/users/delete',
    data:{
             book_id: id
},
success: function( data )
{
    if($( '#like'+ id ).text() == 'Delete'){
        $( '#like'+ id ).removeClass('btn btn-danger btn-lg');
        $( '#like'+ id ).text('Add');
        $( '#like'+ id ).addClass('btn btn-primary btn-lg');
        $( '#div'+ id ).hide();
    }
 }
 })
 });


//SCRIPT FOR CHANGING BOOK'S TABS AND OPENING DEFAULT TAB
document.getElementById("defaultOpen").click();

function openCategory(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}