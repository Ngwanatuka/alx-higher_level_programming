$(document).ready(function() {
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
      method: 'GET',
      success: function(response) {
        var movies = response.results;
        var ul = $('#list_movies');
        
        $.each(movies, function(index, movie) {
          var li = $('<li>').text(movie.title);
          ul.append(li);
        });
      }
    });
  });
  