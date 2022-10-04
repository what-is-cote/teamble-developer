class Model {
  constructor() {
    this.toDoList = [{ id: 0, value: "기본" }];
    this.isEditing = false;
  }

  /** @param {string} todo */
  addToDo(toDo) {
    this.toDoList.push(toDo);
  }

  updateToDo(newTodo) {
    this.toDoList = this.toDoList.map((toDo) => {
      if (toDo.id === newTodo.id) return newTodo;
      return toDo;
    });
  }
}

export default Model;
