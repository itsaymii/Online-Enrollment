// modal.js
// Handles opening/closing modals and blurring background
function openModal(modalId) {
    document.getElementById(modalId).style.display = 'block';
    document.body.classList.add('modal-blur');
}
function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
    document.body.classList.remove('modal-blur');
}
document.querySelectorAll('.modal .close').forEach(function(btn) {
    btn.onclick = function() {
        closeModal(btn.closest('.modal').id);
    };
});
window.onclick = function(event) {
    document.querySelectorAll('.modal').forEach(function(modal) {
        if (event.target == modal) {
            closeModal(modal.id);
        }
    });
};
