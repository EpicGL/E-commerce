let cart_counter = document.querySelector('.cart-counter');
let cart_link = document.querySelector('.cart-link');


function ordercunt(){
    const orderid = localStorage.getItem("order_id")
    
    if (orderid != null){
        url = `http://127.0.0.1:8000/api/total-order-item/${orderid}`
        fetch(url)
        .then (res => res.json())
        .then(data =>{
            console.log('Ordercunt data : ' + data)
            if (data == 'no data'){
                return cart_counter.textContent = '';
            }

            if (data < 1){
                localStorage.removeItem('order_id')
                return cart_counter.textContent = '';
            }

            cart_counter.textContent = data;
            cart_link.setAttribute('href',`http://127.0.0.1:8000/cart/${orderid}`)
        })
    }
}

ordercunt()

// add item to cart
document.addEventListener("DOMContentLoaded", function () {
    const addButtons = document.querySelectorAll(".add-btn");

    addButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            const productId = event.target.getAttribute("data-product");
            const url = `http://127.0.0.1:8000/api/add-to-cart/${productId}`;

            console.log('url: ' + url)

            const orderid = localStorage.getItem("order_id");
            let data = {};
            if (orderid != null) {
                data = { order_id: orderid };
                console.log('data ' +JSON.stringify(data))
            }
            
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
                console.log(data)
                let orderid = data.order
                console.log('message:' + orderid)

                localStorage.setItem("order_id", JSON.stringify(orderid)) 
                console.log(localStorage.getItem("order_id"))
                ordercunt()
            })
            .catch(error => {
                console.error("Error:", error);
            });
        });
    });
});
