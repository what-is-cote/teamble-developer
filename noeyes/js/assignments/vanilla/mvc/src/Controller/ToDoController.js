import Controller from "./index.js";

class ToDoController extends Controller {
  constructor(model, view) {
    super(model, view);

    this.render();
  }

  setEvent() {
    this.view
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
    this.view.render(this.model.toDoList);
  }
}

export default ToDoController;
