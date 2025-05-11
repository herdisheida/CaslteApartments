// Validate and Display Gallery Upload for Create Property
document.getElementById('image-upload').addEventListener('change', function(e) {
    const preview = document.getElementById('image-preview');
    preview.innerHTML = '';

    // validation
    if (this.files.length > 10) {
        alert('Maximum 10 images allowed');
        this.value = '';
        return;
    }

    // image preview
    Array.from(this.files).forEach(file => {
        if (!file.type.match('image.*')) return;

        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.classList.add('preview-image');
            preview.appendChild(img);
        }
        reader.readAsDataURL(file);
    });
});