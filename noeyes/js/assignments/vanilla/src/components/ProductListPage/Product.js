import Component from "../../core/Component.js";

class Product extends Component {
  template() {
    const { imageUrl, name, price } = this.$props;

    return `
    <img src=${imageUrl}>
    <div class="Product__info">
      <div>${name}</div>
      <div>${price.toLocaleString()}원~</div>
    </div>
    `;
  }
}

export default Product;
