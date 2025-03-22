// filepath: c:\Users\Ali\Documents\VS_CODE projects\listo\static\js\scripts.js

const modal = new bootstrap.Modal(document.getElementById('backdrop'));
const form = document.getElementById('todoForm');


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

/*
function showToast(message, duration = 10000) {
    const toastContainer = document.getElementById('toastContainer');
    const toastTemplate = document.getElementById('toastTemplate');
    const newToast = toastTemplate.cloneNode(true);
    newToast.querySelector('.toast-body').textContent = message;
    toastContainer.appendChild(newToast);
    const toast = new bootstrap.Toast(newToast);
    toast.show();
}
*/
  

/* document.addEventListener('DOMContentLoaded', function() {
    const todoForm = document.getElementById('todoItemForm');
    if (todoForm) {
        todoForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission
            const formData = new FormData(todoForm);
            fetch(todoForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showToast('Task saved successfully!', 10000);
                } else {
                    showToast('Failed to save task.', 10000);
                }
            })
            .catch(error => {
                showToast('An error occurred.', 10000);
            });
        });
    }
});
*/

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