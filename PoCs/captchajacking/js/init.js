$('.toggle_code').click(function(){
    var code = $(this).parent().siblings('.input').html();
//    $(this).parent().next().text(code);
    $(this).closest('tr').next().toggle();
    $(this).closest('tr').next().find('td').text(code);
});
