import Component from "../core/Component.js";
import { useState } from "../utils/hook.js";

class Counter extends Component {
  setup() {
    [this.count, this.setCount] = useState(0);
  }

  template() {
    return `
      <span class='count'>${this.count}</span>
      <button class='increase'>+</button>
      <button class='decrease'>-</button>
    `;
  }

  setEvent() {
    this.addEvent("click", ".increase", (e) => {
      this.setCount(this.count + 1);
    }).addEvent("click", ".decrease", (e) => {
      this.setState({ count: this.$state.count - 1 });
    });
  }
}

export default Counter;
