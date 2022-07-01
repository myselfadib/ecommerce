var stripe = stripe('sk_test_51LGNYHK9Mq6UmztsyW63k9TTi4nbfBzoew7qsMxkgFRcfaiKvSs5NMsr6K6U8PKwx4BtH5TI39uxcY3C24J9HQDL004yG4wz95');

var elm = document.getElementById('submit');
clientsecret = elm.getAttribute('data-secret');

// Set up Stripe.js and Elements to use in checkout form
var elements = stripe.elements();

var style = {
    base: {
      color: "#000",
      lineHeight: '2.4',
      fontSize: '16px'
    }
    };
var card = elements.create("card", { style: style });
card.mount("#card-element");
    
card.on('change', function(event) {
    var displayError = document.getElementById('card-errors')
    if (event.error) {
      displayError.textContent = event.error.message;
      $('#card-errors').addClass('alert alert-info');
    } else {
      displayError.textContent = '';
      $('#card-errors').removeClass('alert alert-info');
    }
    });


var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev)
{
  ev.preventDefault();
  var custName = document.getElementById("custName").value;
  var custAdd = document.getElementById("custAdd").value;
  var custAdd2 = document.getElementById("custAdd2").value;
  var postCode = document.getElementById("postCode").value;

  


})