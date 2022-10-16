import Model from "./Model/index.js";
import FormView from "./View/FormView.js";
import ToDoView from "./View/ToDoView.js";
import FormController from "./Controller/FormController.js";
import ToDoController from "./Controller/ToDoController.js";

// const model = new Model();
// new Controller(model, {
//   formView: new FormView(),
//   toDoView: new ToDoView(),
// });

const exe = () => {
  const model = new Model();
  new FormController(model, new FormView());
  new ToDoController(model, new ToDoView());
};
exe();
