import { hide, qs } from "../utils/helper.js";

class Controller {
  _listener = [];

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
      .on("@update", ({ detail: { id } }) => {
        this.toggleMode(id);
      })
      .on("@delete", ({ detail: { id } }) => {
        this.deleteToDo(id);
      })
      .on("@submit", ({ detail }) => {
        this.updateToDo(detail);
      });
  }

  raiseListeners(listeners) {
    listeners.forEach((l) => l());
    this.render();
  }

  addToDo({ value }) {
    this.model.addToDo({ id: this.model.toDoList.length + 1, value });
    this.render();
  }

  updateToDo(detail) {
    this.model.updateToDo({ id: parseInt(detail.id), value: detail.value });
    this.render();
  }

  toggleMode(id) {
    this.model.toggleMode(parseInt(id));
    this.render();
  }

  deleteToDo(id) {
    this.model.deleteToDo(parseInt(id));
    this.render();
  }

  render() {
    this.toDoView.render(this.model.toDoList);
  }
}

export default Controller;
