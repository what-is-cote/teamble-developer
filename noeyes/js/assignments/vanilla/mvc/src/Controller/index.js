import Model from "../Model/index.js";
import { hide, qs } from "../utils/helper.js";
import FormView from "../View/FormView.js";

class Controller {
  constructor(model, view) {
    this.view = view;
    this.model = model;
    // this.form = new FoCon();
    this.render();
    this.setEvent();
  }

  render() {
    this.view.render(this.model);
  }
}

export default Controller;
