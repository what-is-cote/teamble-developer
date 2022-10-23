import Component from "../../core/Component.js";
import { client } from "../../utils/client.js";
import { getCart, setCart } from "../../utils/storage.js";
import { route } from "../../utils/route.js";

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

    const { total, selected, detail } = this.$state;
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
                ${selected
                  .map(
                    (option) =>
                      `<li data-id=${option.id}>
                      ${option.name} ${option.price}원 <div><input type="number" value=${option.quantity}>개</div>
                    </li>`
                  )
                  .join("")}
              </ul>
              <div class="ProductDetail__totalPrice">${total.toLocaleString()}원</div>
              <button class="OrderButton">주문하기</button>
            </div>
          </div>
        
    `;
  }

  setEvent() {
    this.addEvent("change", "select", (e) => {
      let found = false;
      const { selected, detail } = this.$state;
      const id = parseInt(e.target.selectedOptions[0].dataset.id);
      const [selectedOption] = detail.productOptions.filter(
        (option) => option.id === id
      );

      const newState = selected.map((option) => {
        if (option.id === selectedOption.id) {
          found = true;
          option.quantity < option.stock && (option.quantity += 1);
          return option;
        } else return option;
      });

      if (!found) newState.push({ ...selectedOption, quantity: 1 });

      this.setState({
        selected: [...newState],
        total: this.getTotal(newState),
      });
    })
      .addEvent("change", ".ProductDetail__selectedOptions", (e) => {
        const { selected, detail } = this.$state;
        const id = parseInt(e.target.closest("li").dataset.id);

        const newState = selected.map((option) =>
          option.id === id
            ? {
                ...option,
                ...(0 <= e.target.value && e.target.value <= option.stock
                  ? { quantity: parseInt(e.target.value) }
                  : {}),
              }
            : option
        );

        this.setState({
          selected: [...newState],
          total: this.getTotal(newState),
        });
      })
      .addEvent("click", ".OrderButton", () => {
        const { selected, detail } = this.$state;
        const cart = selected.map((option) => ({
          productId: detail.id,
          optionId: option.id,
          quantity: option.quantity,
        }));

        setCart([...(getCart() || []), ...cart]);
        route("/cart");
      });
  }

  getTotal(selectedOptions) {
    return selectedOptions.reduce((p, c) => (p += c.quantity * c.price), 0);
  }

  async getProductDetail() {
    const data = await client(`/products/${this.id}`, { method: "GET" });
    this.setState({ total: data.price, detail: data });
  }
}

export default ProductDetail;
