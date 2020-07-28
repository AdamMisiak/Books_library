    $('.addbutton').click(function(){
    var id;
    id = $(this).attr("data-catid");
    $.ajax(
    {
        type:"GET",
        url: '/books/add',
        data:{
                 book_id: id
    },
    success: function( data )
    {
        if($( '#like'+ id ).text() == 'Add'){
            $( '#like'+ id ).removeClass('btn btn-primary btn-lg');
            $( '#like'+ id ).text('Delete');
            $( '#like'+ id ).addClass('btn btn-danger btn-lg');
        }
        else if($( '#like'+ id ).text() == 'Delete'){
            $( '#like'+ id ).removeClass('btn btn-danger btn-lg');
            $( '#like'+ id ).text('Add');
            $( '#like'+ id ).addClass('btn btn-primary btn-lg');
        }
     }
     })
     });