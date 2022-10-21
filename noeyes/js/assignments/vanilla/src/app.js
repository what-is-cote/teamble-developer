import Component from "./core/Component.js";
import { registerRouter } from "./utils/route.js";

export default class App extends Component {
  constructor() {
    const $app = document.querySelector(".App");
    super($app);

    const routerCallback = registerRouter(this.render.bind(this));

    window.addEventListener("ROUTE", ({ detail: { url } }) => {
      routerCallback(url);
    });

    window.addEventListener("popstate", () => {
      routerCallback(location.pathname);
    });
  }
}

new App();
