import Component from "../core/Component.js";

export default class Items extends Component {
  setup() {
    this.$state = { items: ["item1", "item2"] };
  }
  template() {
    const { items } = this.$state;
    return `
      <ul class='test'>
        ${items.map((item) => `<li>${item}</li>`).join("")}
      </ul>
      <button class='addBtn'>추가</button>
      <button class='deleteBtn'>삭제</button>
      <div class='box1' style='width: 100px; height: 100px; background: red;'>
      <div class='box2' style='width: 50px; height: 50px; background: blue;'> <div/>
      <div/>
    `;
  }

  setEvent() {
    this.addEvent("click", ".addBtn", () => {
      const { items } = this.$state;
      this.setState({ items: [...items, `item${items.length + 1}`] });
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
