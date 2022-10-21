import { client } from "../../utils/client.js";
import Product from "../ProductListPage/Product.js";
import Component from "../../core/Component.js";
import { createEl } from "../../utils/helper.js";
import { route } from "../../utils/route.js";

class ProductList extends Component {
  setup() {
    this.$state = { products: [] };
    this.getProducts();
  }

  template() {
    return `
    `;
  }

  setEvent() {
    this.addEvent("click", ".Product", (e) => {
      const id = e.target.closest("li").dataset.id;
      route(`/products/${id}`);
    });
  }

  mounted() {
    this.$state.products.forEach((product) => {
      new Product(
        createEl("li", {
          class: "Product",
          attributes: { "data-id": product.id },
        }),
        product
      ).appendTo(this.$target);
    });
  }

  async getProducts() {
    const data = await client("/products", { method: "GET" });
    this.setState({ products: data });
  }
}

export default ProductList;
