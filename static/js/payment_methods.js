  // Get all elements
  const continueBtn = document.getElementById('continue-to-review-page');
  const backBtn = document.getElementById('back-to-form-btn');
  const purchaseForm = document.getElementById('form-purchase');
  const reviewSection = document.getElementById('preview-purchase');


// Payment method toggle with drop down menu (mortgage, card, bank)
document.addEventListener('DOMContentLoaded', () => {
  const paymentMethod = document.getElementById('payment-method');
  const toggleSections = (selectedValue) => {
    document.querySelectorAll('.payment-section').forEach(section => {
      section.classList.add('d-none');
    });
    if (selectedValue) {
      document.getElementById(`${selectedValue}-fields`).classList.remove('d-none');
    }
  };
  paymentMethod.addEventListener('change', (e) => toggleSections(e.target.value));

  // Format card number
  document.getElementById('card-number')?.addEventListener('input', (e) => {
    e.target.value = e.target.value.replace(/\W/gi, '').replace(/(.{4})/g, '$1 ').trim();
  });
});


// Display Review page and Hide the form page
const toggleReview = () => {
  // Toggle review section visibility
  const reviewSection = document.getElementById('preview-purchase');
  reviewSection.classList.toggle('d-none');

  // Toggle form section visibility
  const purchaseForm = document.getElementById('form-purchase');
  purchaseForm.classList.toggle('d-none');

}


// Validate - personal info
const validatePersonalInfo = () => {
  // Helper arrow functions
  const validateField = (field, errorMessage) => {
    if (!field.value.trim()) {
      alert(errorMessage);
      return false;
    }
    return true;
  };

  const isNumber = (field, errorMessage) => {
    if (isNaN(Number(field.value)) || field.value.trim() === '') {
      alert(errorMessage);
      return false;
    }
    return true;
  };

  // Get form elements (assuming these IDs match your Django form)
  const streetName = document.getElementById('id_street_name');
  const houseNumber = document.getElementById('id_house_nr');
  const city = document.getElementById('id_city');
  const postalCode = document.getElementById('id_postal_code');
  const country = document.querySelector('[id="id_country"]');
  const nationalId = document.getElementById('id_national_id');

  // Validate all fields
  return (
    validateField(streetName, 'Please enter your street name') &&
    validateField(houseNumber, 'Please enter your house number') &&
    validateField(city, 'Please enter your city') &&
    validateField(postalCode, 'Please enter your postal code') &&
    validateField(country, 'Please select your country') &&
    validateField(nationalId, 'Please enter your national ID') &&
    validateField(nationalId, 'National ID should only be numbers') &&
    isNumber(houseNumber, 'House number must only be numbers')
  );
};



// Validate - payment form
const validPaymentForm = (form) => {
  const paymentMethod = document.getElementById('payment-method')?.value;
  if (!paymentMethod) {
    alert('Please select a payment method');
    return false;
  }

  // More robust field validation
  const validateField = (fieldId, errorMessage) => {
    const field = document.getElementById(fieldId);
    if (!field) {
      console.error(`Field ${fieldId} not found`);
      return false;
    }
    const value = field.value?.toString().trim();
    if (!value) {
      alert(errorMessage);
      field.focus();
      return false;
    }
    return true;
  };

  const isValidCardNumber = (number) => {
    const cleaned = number?.toString().replace(/\s+/g, '') || '';
    if (!/^\d{13,19}$/.test(cleaned)) {
      alert('Please enter a valid card number (13-19 digits)');
      return false;
    }
    return true;
  };

  const isValidMonth = (month) => {
    const num = parseInt(month?.toString() || '');
    if (isNaN(num) || num < 1 || num > 12) {
      alert('Please enter a valid month (01-12)');
      return false;
    }
    return true;
  };

  const isValidYear = (year) => {
    const currentYear = new Date().getFullYear() % 100;
    const input_year = parseInt(year?.toString() || '');
    if (isNaN(input_year) || input_year < currentYear) {
      alert('Please enter a valid expiration year');
      return false;
    }
    return true;
  };

  const isValidCVV = (cvv) => {
    if (!/^\d{3,4}$/.test(cvv?.toString() || '')) {
      alert('Please enter a valid CVV (3-4 digits)');
      return false;
    }
    return true;
  };

  // Validate based on payment method
  switch (paymentMethod) {
    case 'card':
      if (!validateField('card-name', 'Please enter cardholder name')) return false;
      if (!validateField('card-number', 'Please enter card number') ||
          !isValidCardNumber(document.getElementById('card-number')?.value)) return false;
      if (!validateField('card-month', 'Please enter expiration month') ||
          !isValidMonth(document.getElementById('card-month')?.value)) return false;
      if (!validateField('card-year', 'Please enter expiration year') ||
          !isValidYear(document.getElementById('card-year')?.value)) return false;
      if (!validateField('card-cvv', 'Please enter CVV') ||
          !isValidCVV(document.getElementById('card-cvv')?.value)) return false;
      break;

    case 'bank':
      if (!validateField('bank-number', 'Please enter account number')) return false;
      if (!validateField('bank-reference-number', 'Please enter reference number')) return false;
      break;

    case 'mortgage':
      if (!validateField('mortgage-bank-number', 'Please enter bank number')) return false;
      if (!validateField('mortgage-loan-reference-number', 'Please enter loan reference')) return false;
      break;
  }
  return true;
};

continueBtn.addEventListener('click', () => {
  if (validatePersonalInfo(purchaseForm) && validPaymentForm(purchaseForm)) {
    toggleReview()
  }
});
backBtn.addEventListener('click', toggleReview);

