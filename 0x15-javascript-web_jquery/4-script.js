/* script that toggles the class of the <header> element
  when the user clicks on the tag */

$(function () {
  $('#toggle_header').on('click', function () {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red').addClass('green');
    } else if ($('header').hasClass('green')) {
      $('header').removeClass('green').addClass('red');
    }
  });
});
