// import Alpine from "https://cdn.skypack.dev/alpinejs@3.0.6";
// window.Alpine = Alpine

// Alpine.start()

// function tabs() {
//     return {
//         active: 1,
//         isActive(tab) {
//             return tab == this.active;
//         },
//     }
// }

// setActive(value) {
//     this.active = value;
// };
let table = new DataTable('#story', {
    // options
});

const flatpickr = require("flatpickr");
flatpickr("#id_released_at", {
    enableTime: true,
    dateFormat: "Y-m-d H:i",
    altInput: true,
    altFormat: "F j, Y H;i",
});