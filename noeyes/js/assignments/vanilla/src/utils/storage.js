export function getCart() {
  return JSON.parse(localStorage.getItem("products_cart"));
}

export function setCart(newProducts) {
  localStorage.setItem("products_cart", JSON.stringify(newProducts));
}
