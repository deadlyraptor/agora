// toggle mobile menu
const burgerIcon = document.querySelector('.navbar-burger');
const navbarMenu = document.querySelector('.navbar-menu');

burgerIcon.addEventListener('click', () => {
    navbarMenu.classList.toggle('is-active');
});

// close notification
const deleteButton = document.querySelectorAll('.notification .delete').forEach($deleteButton => {
    const notification = $deleteButton.parentNode;
    $deleteButton.addEventListener('click', () => {
        notification.parentNode.removeChild(notification);
    });
});
