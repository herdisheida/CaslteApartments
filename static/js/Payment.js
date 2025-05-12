//Displaying payment menu
  const methodSelect = document.getElementById("payment-method");
  const card = document.getElementById("card-fields");
  const bank = document.getElementById("bank-fields");
  const mortgage = document.getElementById("mortgage-fields");

  methodSelect.addEventListener("change", function () {
    card.style.display = "none";
    bank.style.display = "none";
    mortgage.style.display = "none";

    if (this.value === "card") {
      card.style.display = "block";
    } else if (this.value === "bank") {
      bank.style.display = "block";
    } else if (this.value === "mortgage") {
      mortgage.style.display = "block";
    }
  });

document.addEventListener('DOMContentLoaded', () => {
  // Contact info
  const street = document.getElementById('street-name');
  const city = document.getElementById('city');
  const postal = document.getElementById('postal-code');
  const nationalId = document.getElementById('national-id');
  const country = document.getElementById('select-country');

  // Card info
  const cardName = document.getElementById('card-name');
  const cardNumber = document.getElementById('card-number');
  const cardMonth = document.getElementById('card-month');
  const cardYear = document.getElementById('card-year');
  const cardCVV = document.getElementById('card-cvv');

  const method = document.getElementById('payment-method');
  const payButton = document.getElementById('pay-button');
  const cardSection = document.getElementById('card-fields');

  //Bank info
  const bankNumber = document.getElementById('bank-number')
  const bankReferenceNumber = document.getElementById('bank-reference-number')

  //Mortgage info
  const mortgageBankNumber = document.getElementById('mortgage-bank-number')
  const mortgageLoanReferenceNumber = document.getElementById('mortgage-loan-reference-number')

  function isFilled(el) {
    return el && el.value.trim() !== '';
  }

  function validate() {
    const infoFilled = [street, city, postal, nationalId, country].every(isFilled);
    const cardFilled = [cardName, cardNumber, cardMonth, cardYear, cardCVV].every(isFilled);
    const bankFilled = [bankNumber, bankReferenceNumber].every(isFilled)
    const mortgageFilled = [mortgageBankNumber, mortgageLoanReferenceNumber].every(isFilled);

    if (method.value === 'card') {
      payButton.disabled = !(infoFilled && cardFilled);
    } else if (method.value === 'bank') {
      payButton.disabled = !(infoFilled && bankFilled);
    } else if (method.value === 'mortgage') {
      payButton.disabled = !(infoFilled && mortgageFilled);
    } else {
      payButton.disabled = true;
    }
}

  // Show/hide card section based on selection
  method.addEventListener('change', () => {
    cardSection.style.display = method.value === 'card' ? 'block' : 'none';
    validate();
  });

  const allInputs = [street, city, postal, nationalId, country, cardName, cardNumber, cardMonth, cardYear, cardCVV,
   bankNumber, bankReferenceNumber, mortgageBankNumber, mortgageLoanReferenceNumber];

  allInputs.forEach(input => {
    input.addEventListener('input', validate);
  });

  // Optional: redirect on submit
  document.getElementById('payment-form').addEventListener('submit', e => {
    e.preventDefault();
    alert('Form submitted!');
    // window.location.href = '/thank-you/';
  });

  // Initial state
  validate();
});





