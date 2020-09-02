    $('.deletebutton').click(function(){
    var id;
    id = $(this).attr("data-catid");
    $.ajax(
    {
        type:"GET",
        url: '/users/delete_review',
        data:{
            book_id: id
    },
    success: function( data )
    {
        $( '#review' ).css("display", "none");
     }
     })
     });