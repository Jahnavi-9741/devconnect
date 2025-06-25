document.addEventListener("DOMContentLoaded", () => {
    const toggleBtn = document.getElementById("darkToggle");
    toggleBtn.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
    });
});
