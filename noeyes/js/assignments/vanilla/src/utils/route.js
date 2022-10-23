import CartPage from "../pages/CartPage.js";
import ProductDetailPage from "../pages/ProductDetailPage.js";
import ProductListPage from "../pages/ProductListPage.js";
import { createEl } from "./helper.js";

export function registerRouter(render) {
  function router() {
    const $app = document.querySelector(".App");
    const { pathname } = location;

    render();

    if (pathname === "/") {
      new ProductListPage(
        createEl("div", { class: "ProductListPage" })
      ).appendTo($app);
    } else if (pathname.slice(1).split("/")[0] === "products") {
      new ProductDetailPage(
        createEl("div", { class: "ProductDetailPage" })
      ).appendTo($app);
    } else if (pathname === "/cart") {
      new CartPage(createEl("div", { class: "CartPage" })).appendTo($app);
    }
  }

  function routerCallback(url) {
    history.pushState(null, null, url);
    router(render);
  }

  router();

  return routerCallback;
}

export function route(url) {
  const E = new CustomEvent("ROUTE", {
    cancelable: true,
    detail: { url },
  });
  window.dispatchEvent(E);
}
