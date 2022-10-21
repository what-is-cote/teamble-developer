import Component from "../../core/Component.js";
import { client } from "../../utils/client.js";
import { createEl, qs } from "../../utils/helper.js";

class ProductDetail extends Component {
  setup() {
    this.id = location.pathname.split("/").slice(-1);
    this.$state = {
      total: 0,
      selected: [],
      detail: {},
    };
    this.getProductDetail();
  }

  template() {
    if (JSON.stringify(this.$state.detail) === "{}")
      return `<div>loading...</div>`;

    const { total, order, detail } = this.$state;
    return `
          <img src="https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/assignment_image/cafe_coffee_cup.png">
          <div class="ProductDetail__info">
            <h2>커피잔</h2>
            <div class="ProductDetail__price">${detail.price.toLocaleString()}원~</div>
            <select>
            <option>선택하세요.</option>
            ${detail.productOptions
              .map((option) => {
                if (option.stock === 0)
                  return `<option disabled data-id=${option.id}>${option.name}(품절)</option>`;
                else
                  return `<option data-id=${option.id}>${option.name}(+${option.price})</option>`;
              })
              .join("")}
            </select>
            <div class="ProductDetail__selectedOptions">
              <h3>선택된 상품</h3>
              <ul>
                <li>
                  커피잔 100개 번들 10,000원 <div><input type="number" value="10">개</div>
                </li>
                <li>
                  커피잔 1000개 번들 15,000원 <div><input type="number" value="5">개</div>
                </li>
              </ul>
              <div class="ProductDetail__totalPrice">${total.toLocaleString()}원</div>
              <button class="OrderButton">주문하기</button>
            </div>
          </div>
        
    `;
  }

  async getProductDetail() {
    const data = await client(`/products/${this.id}`, { method: "GET" });
    this.setState({ detail: data });
  }
}

export default ProductDetail;
