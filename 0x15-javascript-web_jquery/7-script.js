// A script that fetches the character name from a api/URL

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: function (data) {
      $('#character').append(data.name);
    },
    error: function () {
      $('#character').text('No name found');
    }
  });
});
