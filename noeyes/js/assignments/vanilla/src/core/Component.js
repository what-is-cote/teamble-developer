import { createEl } from "../utils/helper.js";

export default class Component {
  $target;
  $state;

  constructor($target, $props = {}, option = {}) {
    this.$target = $target;
    this.$props = $props;
    this.setup();
    this.render(option);
    this.setEvent();
  }
  mounted() {}
  setup() {}
  template() {
    return "";
  }

  render() {
    this.$target.innerHTML = this.template();
    this.mounted();
  }

  setEvent() {}
  setState(newState) {
    this.$state = { ...this.$state, ...newState };
    this.render();
  }

  addEvent(eventType, selector, callback, target = this.$target) {
    const children = [...target.querySelectorAll(selector)];

    const isTarget = (target) =>
      children.includes(target) || target.closest(selector);

    target.addEventListener(eventType, (event) => {
      if (!isTarget(event.target)) return false;
      callback(event);
    });

    return this;
  }

  appendTo(parent) {
    parent.append(this.$target);
  }

  get root() {
    return this.$target;
  }
}
