// Payment method toggle with drop down menu
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
document.getElementById('continue-payment-btn').addEventListener('click', toggleReview)
