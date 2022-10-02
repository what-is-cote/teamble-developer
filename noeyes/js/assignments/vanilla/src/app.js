import Component from "./core/Component.js";
import Items from "./components/Items.js";

export default class App extends Component {
  constructor() {
    const $app = document.querySelector("#app");
    super($app);
  }

  template() {
    return `
      <div class='box1' style='width: 100px; height: 100px; background: red;'>
        <span>before component</span>
      </div>
    `;
  }

  mounted() {
    new Items(document.querySelector(".box1"));
  }

  setEvent() {
    this.addEvent("click", ".box1", () => this.setState({}));
  }
}

new App();
