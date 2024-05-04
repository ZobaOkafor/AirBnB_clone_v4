$(document).ready(function() {
    // Initialize an empty array to store Amenity IDs
    let amenityIDs = [];

    // Listen for changes on each input checkbox tag
    $('input[type="checkbox"]').change(function() {
        const amenityID = $(this).data('id');
        const amenityName = $(this).data('name');

        // Check if the checkbox is checked
        if ($(this).is(':checked')) {
            // Add Amenity ID to the array if checked
            amenityIDs.push(amenityID);
        } else {
            // Remove Amenity ID from the array if unchecked
            const index = amenityIDs.indexOf(amenityID);
            if (index !== -1) {
                amenityIDs.splice(index, 1);
            }
        }

        // Update the h4 tag inside the div Amenities with the list of Amenities checked
        const amenitiesList = amenityIDs.map(id => $('#' + id).data('name')).join(', ');

        $('.amenities h4').text(amenitiesList);
    });
});
