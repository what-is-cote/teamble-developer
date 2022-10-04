import Model from "./Model/index.js";
import Controller from "./Controller/index.js";
import FormView from "./View/FormView.js";
import ToDoView from "./View/ToDoView.js";

const model = new Model();
new Controller(model, {
  formView: new FormView(),
  toDoView: new ToDoView(),
});
