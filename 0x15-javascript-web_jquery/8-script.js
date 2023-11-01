// A script that fetches and lists the title for all movies by using this URL

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      for (const movie of data.results) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      }
    },
    error: function () {
      $('#list_movies').text('Cannot find movie');
    }
  });
});
