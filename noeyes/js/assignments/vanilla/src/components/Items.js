import Component from "../core/Component.js";
import { useState } from "../utils/hook.js";

export default class Items extends Component {
  setup() {
    [this.items, this.setItems] = useState(["item1", "item2"]);
  }
  template() {
    return `
      <ul class='test' data-is-hi='hihi'>
        ${this.items.map((item) => `<li>${item}</li>`).join("")}
      </ul>
      <button class='addBtn'>추가</button>
      <button class='deleteBtn'>삭제</button>
      
    `;
  }

  setEvent() {
    this.addEvent("click", ".addBtn", () => {
      // const { items } = this.$state;
      // this.setState({ items: [...items, `item${items.length + 1}`] });
      this.setItems([...this.items, `item${this.items.length + 1}`]);
    });
    this.addEvent("click", ".deleteBtn", ({ target }) => {
      const items = [...this.$state.items];
      items.splice(target.dataset.index, 1);
      this.setState({ items });
    });

    this.addEvent("click", ".box1", () => {
      console.log("clicked");
    });
  }
}
