class Model {
  constructor() {
    this.toDoList = [{ id: 0, value: "기본", editing: false }];
  }

  /** @param {string} todo */
  addToDo(toDo) {
    this.toDoList.push(toDo);
  }

  updateToDo(newTodo) {
    this.toDoList = this.toDoList.map((toDo) => {
      if (toDo.id === newTodo.id) return { ...newTodo, editing: false };
      return toDo;
    });
  }

  toggleMode(id) {
    this.toDoList = this.toDoList.map((todo) =>
      todo.id === id
        ? { ...todo, editing: !todo.editing }
        : { ...todo, editing: false }
    );
  }

  deleteToDo(id) {
    this.toDoList = this.toDoList.filter((todo) => todo.id !== id);
  }
}

export default Model;
