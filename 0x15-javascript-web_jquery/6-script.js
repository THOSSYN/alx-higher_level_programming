// A script that updates the text of the <header> element to New Header!!!

$(function () {
  $('#update_header').on('click', function () {
    $('header').text('New Header!!!');
  });
});
