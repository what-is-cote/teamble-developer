import { on, qs } from "../utils/helper.js";
import View from "../View/index.js";

class ToDoView extends View {
  constructor() {
    super(qs(".to-do-container"));

    this.template = new Template();
    this.setEvent();
  }

  render(toDoList) {
    qs(".to-do-list", this.$element).innerHTML =
      this.template.getToDoList(toDoList);
  }

  setEvent() {
    this.delegate("click", ".update", this.handleClickUpdate.bind(this))
      .delegate("click", ".delete", this.handleClickDelete.bind(this))
      .delegate("submit", ".to-do-form", this.handleSubmit.bind(this));
  }

  handleSubmit(e) {
    e.preventDefault();

    this.emit("@submit", {
      id: e.target.closest(".to-do").dataset.id,
      value: e.target.children[0].value,
    });
  }

  handleClickDelete({ target }) {
    this.emit("@delete", { id: target.closest(".to-do").dataset.id });
  }

  handleClickUpdate({ target }) {
    this.emit("@update", { id: target.closest(".to-do").dataset.id });
    qs(".to-do-input").focus();
  }

  handleEnter({
    key,
    target: {
      value,
      dataset: { id },
    },
  }) {
    if (key === "Enter") this.emit("@submit", { value, id });
  }
}

export default ToDoView;

class Template {
  constructor() {}

  getToDoTextArea(toDo) {
    return `
      <span class="to-do-text">${toDo.value}</span>
      ${this.getFlexButton()}
    `;
  }

  getToDoForm(toDo) {
    return `
      <form class='to-do-form flex'>
        <input type='text' class="to-do-input" value=${toDo.value} data-id=${
      toDo.id
    }  />
        ${this.getConfirmButton()}
      </form>
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

  getConfirmButton() {
    return `
        <button class="shrink confirm" type='submit'>완료</button>
    `;
  }

  getToDoList(toDoList) {
    return toDoList
      .map(
        (toDo) => `
        <li class="to-do " data-id='${toDo.id}'>
          ${toDo.editing ? this.getToDoForm(toDo) : this.getToDoTextArea(toDo)}
        </li>
    `
      )
      .join("");
  }
}
