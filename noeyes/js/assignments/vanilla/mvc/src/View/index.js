import { delegate, emit, hide, on } from "../utils/helper.js";

class View {
  constructor(element) {
    this.$element = element;
  }

  on(event, callback) {
    on(event, this.$element, callback);

    return this;
  }

  delegate(event, selector, callback) {
    delegate(event, this.$element, selector, callback);

    return this;
  }

  emit(event, payload) {
    emit(event, this.$element, payload);
  }

  show() {}

  hide() {
    hide();
  }
}

export default View;
