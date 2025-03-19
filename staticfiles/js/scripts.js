// filepath: c:\Users\Ali\Documents\VS_CODE projects\listo\static\js\scripts.js

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