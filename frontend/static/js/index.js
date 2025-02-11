// sidebar actions
// opening and closing the sidebar
let sideBar = document.querySelector(".navbar-content");
let dashboardContent = document.querySelector(".content");
let menuBtn = document.querySelector(".menu-btn i");

menuBtn.addEventListener("click", () => {
    menuBtn.classList.toggle("active");
    let isOpen = menuBtn.classList.contains("active");

    menuBtn.classList.toggle("fa-bars", !isOpen);
    menuBtn.classList.toggle("fa-times", isOpen);

    sideBar.style.display = isOpen ? "none" : "block";
    dashboardContent.style.left = isOpen ? "10px" : "var(--content-width)";
});

// making a ul.li navlink active
document.addEventListener("DOMContentLoaded", () => {
    const sidebarLinks = document.querySelectorAll(".sidebarlink");

    sidebarLinks.forEach(link => {
        link.addEventListener("click", () => {
            sidebarLinks.forEach((link) =>
                link.querySelector(".sidebarListItem").classList.remove("active")
            );

            link.querySelector(".sidebarListItem").classList.add("active");
        });
    });
});

// opening and closing the form sections
document.addEventListener("DOMContentLoaded", () => {
    let service = document.querySelector(".itemContainer");
    let form = document.querySelector(".additem");
    let addBtn = document.querySelector(".additemBtn");
    let closeBtn = document.querySelector(".closeFormBtn");

    addBtn.addEventListener("click", () => {
        service.style.display = "none";
        form.style.display = "block";
    });

    closeBtn.addEventListener("click", () => {
        form.style.display = "none";
        service.style.display = "block";
    });
});