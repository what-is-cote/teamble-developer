import { qs, on } from "../utils/helper.js";
import View from "../View/index.js";

class FormView extends View {
  constructor() {
    super(qs("#form"));

    this.$input = qs("[type=text]", this.$element);
    this.$searchButton = qs("[type=button]", this.$element);
  }
}

export default FormView;
