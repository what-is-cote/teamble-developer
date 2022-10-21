import ProductList from "../components/ProductListPage/ProductList.js";
import Component from "../core/Component.js";
import { createEl } from "../utils/helper.js";

class ProductListPage extends Component {
  template() {
    return `
      <h1>상품목록</h1>
    `;
  }

  mounted() {
    new ProductList(createEl("ul")).appendTo(this.$target);
  }
}

export default ProductListPage;
