// Event delegation for all select elements
document.addEventListener('change', (e) => {
    if (e.target.classList.contains('offer-state-select')) {
        const offerId = e.target.dataset.offerId;
        const container = document.getElementById(`contingent-reason-container-${offerId}`);
        container.classList.toggle('d-none', e.target.value !== 'contingent');
    }
});

// Initialize all selects on page load
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.offer-state-select').forEach(select => {
        const offerId = select.dataset.offerId;
        const container = document.getElementById(`contingent-reason-container-${offerId}`);
        container.classList.toggle('d-none', select.value !== 'contingent');
    });
});