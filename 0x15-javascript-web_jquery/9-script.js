/* A script that fetches and displays the value of Hello
 in another language
*/

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      $('#hello').text(data.hello);
    },
    error: function () {
      $('#hello').text('Error finding interpretation');
    }
  });
});
