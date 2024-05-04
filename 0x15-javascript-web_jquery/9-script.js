#!/usr/bin/node

$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    dataType: 'json',
    success: function (response) {
      $('#hello').text(response.hello);
    },
    error: function (xhr, status, error) {
      console.error('Error fetching hello data:', error);
    }
  });
});
