// AJAX for Add Student Modal
// Assumes jQuery is available. If not, use vanilla JS fetch API.
document.addEventListener('DOMContentLoaded', function() {
    var addForm = document.querySelector('#addStudentModal form');
    if (addForm) {
        addForm.addEventListener('submit', function(e) {
            e.preventDefault();
            var formData = new FormData(addForm);
            var xhr = new XMLHttpRequest();
            xhr.open('POST', addForm.action, true);
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            xhr.onload = function() {
                if (xhr.status === 200) {
                    try {
                        var response = JSON.parse(xhr.responseText);
                        if (response.success && response.html) {
                            // Replace table body
                            var tbody = document.querySelector('table tbody');
                            if (tbody) {
                                tbody.outerHTML = response.html;
                            }
                            closeModal('addStudentModal');
                            addForm.reset();
                        } else if (response.errors) {
                            // Show form errors in modal
                            var errorDiv = document.getElementById('addStudentFormErrors');
                            if (!errorDiv) {
                                errorDiv = document.createElement('div');
                                errorDiv.id = 'addStudentFormErrors';
                                addForm.parentNode.insertBefore(errorDiv, addForm);
                            }
                            errorDiv.innerHTML = response.errors;
                        } else {
                            alert('Error adding student.');
                        }
                    } catch (err) {
                        alert('Error adding student.');
                    }
                } else {
                    alert('Error adding student.');
                }
            };
            xhr.send(formData);
        });
    }
});
