import Component from "./core/Component.js";
import Items from "./components/Items.js";
import Counter from "./components/Counter.js";
import { render } from "./utils/hook.js";

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
      <div class='counter'></div>
    `;
  }

  mounted() {
    new Items(document.querySelector(".box1"));
    new Counter(document.querySelector(".counter"));
  }

  setEvent() {}
}

const exe = () => new App();
render(exe);
