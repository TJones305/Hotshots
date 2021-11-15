/*
    Core logic can be found here:

    CSS from here


*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_stripe_public_key').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#f5dad5',
        fontFamily: '"Pontano Sans", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#3b0d11'
        }
    },
    invalid: {
        color: '#d7263d',
        iconColor:'#d7263d'
    }
};

var card = elements.create('card');
card.mount('#card-element', {style:style});

//Handle realtime validation errors on card element
card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = ` 
        <span class="icon" role="alert">
            <i class="fas fa-times></i>
        </span>
        <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});