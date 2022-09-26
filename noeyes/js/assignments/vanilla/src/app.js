import Component from "./core/Component.js";
import Items from "./components/Items.js";
export default class App extends Component {
  constructor() {
    const $app = document.querySelector("#app");
    super($app);

    new Items($app);
  }
}

new App();
