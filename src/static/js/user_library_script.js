$('.username').click(function(){
var id;
username = $(this).attr("id");

$.ajax(
  {
    type:"POST",
    url: '/users/user_library/',
    data:{
             username: username
},

 })
 });