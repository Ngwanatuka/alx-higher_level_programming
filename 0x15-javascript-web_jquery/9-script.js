$(document).ready(function() {
    $.ajax({
      url: 'https://fourtonfish.com/hellosalut/?lang=fr',
      method: 'GET',
      success: function(response) {
        var translation = response.hello;
        $('#hello').text(translation);
      }
    });
  });  