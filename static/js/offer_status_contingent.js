// make contingent/reason container appear/disappear
document.addEventListener("change", (e) => {
  if (e.target.classList.contains("offer-state-select")) {
    const offerId = e.target.dataset.offerId;
    const selectedValue = e.target.value;

    // Contingent reason container
    const contingentContainer = document.getElementById(
      `contingent-reason-container-${offerId}`
    );
    contingentContainer.classList.toggle(
      "d-none",
      selectedValue !== "contingent"
    );

    // Reject reason container
    const rejectContainer = document.getElementById(
      `reject-reason-container-${offerId}`
    );
    rejectContainer.classList.toggle("d-none", selectedValue !== "reject");
  }
});

// Initialize on page load
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".offer-state-select").forEach((select) => {
    const offerId = select.dataset.offerId;
    const selectedValue = select.value;

    document
      .getElementById(`contingent-reason-container-${offerId}`)
      .classList.toggle("d-none", selectedValue !== "contingent");

    document
      .getElementById(`reject-reason-container-${offerId}`)
      .classList.toggle("d-none", selectedValue !== "reject");
  });
});

// Validation - cannot submit make offer contingent without stating a reason
document.querySelector("form").addEventListener("submit", (e) => {
  const select = document.querySelector(".offer-state-select");
  if (
    select?.value === "contingent" &&
    !document
      .getElementById(`contingent-reason-${select.dataset.offerId}`)
      .value.trim()
  ) {
    e.preventDefault();
    alert("Please provide a contingency reason");
    document
      .getElementById(`contingent-reason-container-${select.dataset.offerId}`)
      .classList.remove("d-none");
  }
});
