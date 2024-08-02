// static/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    const profile = document.querySelector('.profile');
    const dropdown = document.querySelector('.profile-dropdown');

    profile.addEventListener('mouseenter', function() {
        dropdown.style.display = 'block';
    });

    profile.addEventListener('mouseleave', function() {
        dropdown.style.display = 'none';
    });
});
