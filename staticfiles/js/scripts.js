// filepath: c:\Users\Ali\Documents\VS_CODE projects\listo\static\js\scripts.js

const form = document.getElementById('todoForm');

if (form) {
    //document.activeElement.blur(); // Remove focus from the submit button
    const modal = new bootstrap.Modal(document.getElementById('staticBackdrop'));

    form.addEventListener('submit', function(event) {
        const dueDateInput = document.querySelector('input[type="date"]');
        const dueDate = new Date(dueDateInput.value);
        const today = new Date();
        today.setHours(0, 0, 0, 0); // Set time to midnight to compare only dates

        if (dueDate < today) {
            event.preventDefault(); // Prevent form submission
            modal.show();            
        }
    });

    const submitButton = document.getElementById("confirm-submit");
    submitButton.addEventListener('click', function() {
        form.submit();
    });
}

document.addEventListener('DOMContentLoaded', function() {
    // Handle alert messages
    setTimeout(function () {
        let messages = document.getElementById('msg');
        if (messages) {
            let alert = new bootstrap.Alert(messages);
            alert.close();
        }
    }, 2500);
});