import ProductDetail from "../components/ProductDetailPage/ProductDetail.js";
import Component from "../core/Component.js";
import { qs } from "../utils/helper.js";

class ProductDetailPage extends Component {
  template() {
    return `
      <h1>커피잔 상품 정보</h1>
      <div class="ProductDetail" />
    `;
  }

  mounted() {
    new ProductDetail(qs(".ProductDetail", this.$target));
  }
}

export default ProductDetailPage;
