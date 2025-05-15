const validateImage = (input) => {
    const file = input.files[0];
    if (file) {
        // Check file type
        const validTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
        if (!validTypes.includes(file.type)) {
            alert('Please select a JPG, PNG, GIF or WEBP image');
            input.value = '';
            return false;
        }
    }
    return true;
};