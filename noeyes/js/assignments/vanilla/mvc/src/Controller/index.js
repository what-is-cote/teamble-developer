import { hide, qs } from "../utils/helper.js";

class Controller {
  constructor(model, { formView, toDoView }) {
    this.model = model;
    this.formView = formView;
    this.toDoView = toDoView;

    this.render();
    this.setEvent();
  }

  setEvent() {
    this.formView
      .on("submit", (e) => e.preventDefault())
      .on("@submit", (e) => {
        this.addToDo(e.detail);
        e.target[0].value = "";
      });

    this.toDoView
      .delegate("click", ".update", this.toggleMode.bind(this))
      .delegate("click", ".delete", (e) => {
        console.log("삭제");
      });
  }
  addToDo({ value }) {
    this.model.addToDo({ id: this.model.toDoList.length + 1, value });
    this.toDoView.render(this.model.toDoList);
  }

  updateToDo(e) {}

  toggleMode() {
    this.model.isEditing = !this.model.isEditing;
    this.render();
  }

  render() {
    this.toDoView.render(this.model.toDoList);

    // this.toDoView.setEvent();
  }
}

export default Controller;
