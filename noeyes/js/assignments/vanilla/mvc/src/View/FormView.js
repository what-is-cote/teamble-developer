import { qs, on } from "../utils/helper.js";
import View from "../View/index.js";

class FormView extends View {
  constructor() {
    super(qs("#form"));

    this.$input = qs("[type=text]", this.$element);
    this.$searchButton = qs("[type=button]", this.$element);
    console.log(this.$searchButton);
    this.setEvent();
  }

  setEvent() {
    on("keypress", "[type=text]", (e) => this.handleEnter(e));
  }

  handleEnter({ key, target: { value } }) {
    if (key === "Enter") this.emit("@submit", { value });
  }
}

export default FormView;
