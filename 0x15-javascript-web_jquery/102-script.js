// A script that return Hello in different translation

$(function () {
  function TranslateHello () {
    const langCode = $('#language_code').val();
    if (langCode) {
      $.ajax({
        type: 'GET',
        url: 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode,
        success: function (data) {
          $('#hello').text(data.hello);
        },
        error: function () {
          $('#hello').text('Translation not found!');
        }
      });
    }
  }
  $('#btn_translate').click(TranslateHello);
});
