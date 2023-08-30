document.addEventListener("DOMContentLoaded", function () {
    const incrementButtons = document.querySelectorAll(".increment");
    const decrementButtons = document.querySelectorAll(".decrement");
    const removeButtons = document.querySelectorAll(".remove");

    const orderid = localStorage.getItem("order_id");
    let data = {};
    if (orderid != null) {
        data = { order_id: orderid };
        console.log('data ' +JSON.stringify(data))
    }
    

    incrementButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            const orderItemId = event.target.getAttribute("data-orderitem");
            const url = `http://127.0.0.1:8000/api/add-to-cart/${orderItemId}`;

            fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                body: JSON.stringify(data),
            })
            .then(response => response.json())
            .then(data => {
                // Update the quantity display or any other relevant UI elements
                console.log(data);
                location.reload()
            })
            .catch(error => {
                console.error("Error:", error);
            });
        });
    });

    decrementButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            const orderItemId = event.target.getAttribute("data-orderitem");
            const url = `http://127.0.0.1:8000/api/decrement/${orderItemId}`;

            fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                body: JSON.stringify(data),
            })
            .then(response => response.json())
            .then(data => {
                // Update the quantity display or any other relevant UI elements
                console.log(data);
                location.reload()
            })
            .catch(error => {
                console.error("Error:", error);
            });
        });
    });

    removeButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            const orderItemId = event.target.getAttribute("data-orderitem");
            const url = `http://127.0.0.1:8000/api/remove-item/${orderItemId}`;

            fetch(url, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                body: JSON.stringify(data),
            })
            .then(response => response.json())
            .then(data => {
                // Remove the item's HTML element or update the UI accordingly
                console.log(data);
                location.reload()
            })
            .catch(error => {
                console.error("Error:", error);
            });
        });
    });
});
