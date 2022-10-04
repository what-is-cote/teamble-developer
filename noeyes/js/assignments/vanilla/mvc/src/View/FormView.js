import { qs, on } from "../utils/helper.js";
import View from "../View/index.js";

class FormView extends View {
  constructor() {
    super(qs("#form"));

    this.$input = qs("[type=text]", this.$element);
    this.$resetButton = qs("[type=button]", this.$element);

    this.setEvent();
  }

  setEvent() {
    on("keypress", "[type=text]", (e) => this.handleEnter(e));
    on("click", "[type=button]", () => console.log("object"));
  }

  handleEnter({ key, target: { value } }) {
    console.log(value);
    if (key === "Enter") this.emit("@submit", { value });
  }
}

export default FormView;
