function includeHTML() {

  $('.include').each(function(i, e) {
    
    // getHtmlAndRender($(e).attr('include-html'), e);
    let url = $(e).attr('include-html');
    $(e).load(url, '', function() {
      $('#recp').text(0)
    });
  });
}
