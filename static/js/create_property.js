// Validate and Display Gallery Upload for Create Property
document.addEventListener('DOMContentLoaded', () => {
    const uploadInput = document.getElementById('image-upload');
    const previewContainer = document.getElementById('image-preview');

    // only add event listener if elements exist on this page
    if (uploadInput && previewContainer) {
        uploadInput.addEventListener('change', (e) => {
            previewContainer.innerHTML = '';

            // Validation - Max 10 images
            if (this.files.length > 10) {
                alert('Maximum 10 images allowed');
                this.value = '';
                return;
            }

            // Process each file
            Array.from(this.files).forEach(file => {
                if (!file.type.match('image.*')) {
                    console.warn(`Skipped non-image file: ${file.name}`);
                    return;
                }

                const reader = new FileReader();

                reader.onload = (e) => {
                    const img = document.createElement('img');
                    img.src = e.target.result;
                    img.classList.add('preview-image');
                    img.alt = 'Preview of ' + file.name;
                    previewContainer.appendChild(img);
                };

                reader.onerror = () => {
                    console.error('Error reading file:', file.name);
                };

                reader.readAsDataURL(file);
            });
        });
    }
});