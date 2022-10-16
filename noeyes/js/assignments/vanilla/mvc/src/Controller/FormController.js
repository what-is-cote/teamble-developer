import { on } from "../utils/helper.js";
import Controller from "./index.js";

class FormController extends Controller {
  constructor(model, view) {
    super(model, view);
  }

  setEvent() {
    on("keypress", "[type=text]", (e) => this.handleEnter(e));

    this.view
      .on("submit", (e) => e.preventDefault())
      .on("@submit", (e) => {
        this.addToDo(e.detail);
        e.target[0].value = "";
      });
  }

  addToDo({ value }) {
    this.model.addToDo({ id: this.model.toDoList.length + 1, value });
    this.render();
  }

  handleEnter({ key, target: { value } }) {
    if (key === "Enter") this.view.emit("@submit", { value });
  }

  render() {}
}

export default FormController;
