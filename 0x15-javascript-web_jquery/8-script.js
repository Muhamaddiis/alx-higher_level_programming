#!/usr/bin/node

$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (response) {
      $.each(response.results, function (index, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    },
    error: function (xhr, status, error) {
      console.error('Error fetching movie data:', error);
    }
  });
});
