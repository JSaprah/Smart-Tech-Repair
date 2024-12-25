// Get all phone elements
const phones = document.querySelectorAll('.phone');

// Add event listeners to filter buttons
document.getElementById('apple-btn').addEventListener('click', function() {
    filterPhones('Apple');
});

document.getElementById('samsung-btn').addEventListener('click', function() {
    filterPhones('Samsung');
});

document.getElementById('all-btn').addEventListener('click', function() {
    filterPhones('all');
});

// Function to filter phones by manufacturer
function filterPhones(manufacturer) {
    phones.forEach(function(phone) {
        const phoneManufacturer = phone.getAttribute('data-manufacturer');
        
        if (manufacturer === 'all' || phoneManufacturer === manufacturer) {
            phone.style.display = 'block';
        } else {
            phone.style.display = 'none';
        }
    });
}
