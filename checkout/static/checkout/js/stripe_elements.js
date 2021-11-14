/*
    Core logic can be found here:

    CSS from here


*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_stripe_public_key').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var card = elements.create('card');

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

card.mount('#card-element', {style:style});