/* A script that makes a static web interactive and
   interprete Hello in various languages
*/

$(function () {
  function translateHello () {
    const langCode = $('#language_code').val();
    if (langCode) {
      $.ajax({
        type: 'GET',
        url: 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode,
        success: function (data) {
          $('#hello').text(data.hello);
        },
        error: function () {
          $('#hello').text('Translation not found');
        }
      });
    }
  }

  $('#btn_translate').click(translateHello);

  $('#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      translateHello();
    }
  });
});
