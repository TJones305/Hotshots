let countrySelected = $('#id_default_country').val();
        if(!countrySelected) {
            $('#id_default_country').css('color', '#aab7aa');
        }
        $('#id_default_country'). change(function() {
            countrySelected = $(this).val();
            if(!countrySelected) {
                $(this).css('color', '#aab7aa');
            } else {
                $(this).css('color', '#000');
            }
        });