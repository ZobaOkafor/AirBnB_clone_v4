$(document).ready(function () {
  let checkedAmenities = {};
  let checkedStates = {};
  let checkedCities = {};

  $(document).on('change', "input[type='checkbox']", function () {
    if ($(this).closest('.locations').length > 0) {
      if (this.checked) {
        checkedStates[$(this).data('id')] = $(this).data('name');
      } else {
        delete checkedStates[$(this).data('id')];
      }
      let statesList = Object.values(checkedStates).join(', ');
      $('div.locations > h4').text(statesList || '&nbsp;');
    } else {
      if (this.checked) {
        checkedAmenities[$(this).data('id')] = $(this).data('name');
      } else {
        delete checkedAmenities[$(this).data('id')];
      }
      let amenitiesList = Object.values(checkedAmenities).join(', ');
      $('div.amenities > h4').text(amenitiesList || '&nbsp;');
    }
  });

  $('.filters > button').click(function () {
    $('.places > article').remove();
    $.ajax({
      type: 'POST',
      url: 'http://0.0.0.0:5001/api/v1/places_search',
      data: JSON.stringify({'amenities': Object.keys(checkedAmenities),
                            'states': Object.keys(checkedStates),
                            'cities': Object.keys(checkedCities)}),
      dataType: 'json',
      contentType: 'application/json',
      success: function (data) {
        for (let i = 0; i < data.length; i++) {
          let place = data[i];
          $('.places ').append('<article><h2>' + place.name + '</h2><div class="price_by_night"><p>$' + place.price_by_night + '</p></div><div class="information"><div class="max
