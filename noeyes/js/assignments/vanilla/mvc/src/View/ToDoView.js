import { on, qs } from "../utils/helper.js";
import View from "../View/index.js";

class ToDoView extends View {
  constructor() {
    super(qs(".to-do-container"));

    this.template = new Template();
    this.$updateBtn = qs("update", this.$element);
    this.$deleteBtn = qs("delete", this.$element);
  }

  render(toDoList) {
    qs(".to-do-list", this.$element).innerHTML =
      this.template.getToDoList(toDoList);
  }
}

export default ToDoView;

class Template {
  constructor() {}

  getToDoText(value) {
    return `
      <span class="to-do-text">${value}</span>
    `;
  }

  getFlexButton() {
    return `
      <div class="flex-button ml-auto">
        <button class="shrink update">수정</button>
        <button class="shrink delete">삭제</button>
      </div>
    `;
  }

  getToDoList(toDoList) {
    return toDoList
      .map(
        (toDo) => `
        <li class="to-do " data-key='${toDo.id}'>
          ${this.getToDoText(toDo.value)}
          ${this.getFlexButton()}
        </li>
        <li class="to-do to-do-edit hide" data-key='${toDo.id}'>
          <input type='text' class="to-do" data-key='${toDo.id}'/>
          ${this.getFlexButton()}
        </li>
    `
      )
      .join("");
  }
}
