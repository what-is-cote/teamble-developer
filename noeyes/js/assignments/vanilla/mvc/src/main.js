import Model from "./Model/index.js";
import Controller from "./Controller/index.js";
import FormView from "./View/FormView.js";
import ToDoView from "./View/ToDoView.js";

const model = new Model();
new Controller(model, {
  formView: new FormView(),
  toDoView: new ToDoView(),
});

class MyPromise1 {
  constructor(executor) {
    this.state = "pending";
    this.callbackList = [];

    try {
      executor(this.resolve.bind(this), this.reject.bind(this));
    } catch (err) {}
  }

  resolve(data) {
    this.flush(data);
  }
  reject(data) {}
  then(callback) {
    this.callbackList.push(callback);

    return this;
  }

  async flush(data) {
    let value = data;

    for (let callback of this.callbackList) {
      value = await callback(value);
    }
  }
}

const MyPromise2 = class {
  constructor(executor) {
    this.state = "pending";
    this.laterCalls = [];
    this.decidePromiseByMethod.bind(this);
    this.applyChangedState.bind(this);

    try {
      executor(this.resolve.bind(this), this.reject.bind(this));
    } catch (error) {
      this.reject(error);
    }
  }

  applyChangedState(value, state) {
    if (!(this.state === "pending")) return;
    if (value instanceof MyPromise2) {
      value.then((innerPromiseValue) => {
        this.value = innerPromiseValue;
        this.status = state;

        for (let call of this.laterCalls) {
          async () => await call();
        }
        // this.laterCalls.forEach((latercall) => latercall());
      });
    } else {
      this.value = value;
      this.state = state;
      for (let call of this.laterCalls) {
        async () => await call();
      }
      // this.laterCalls.forEach((latercall) => latercall());
    }
  }

  decidePromiseByMethod(method, callback) {
    const state = method === "then" ? "resolved" : "rejected";
    if (this.state === state) {
      return new MyPromise2((resolve) => resolve(callback(this.value)));
    }

    if (this.state === "pending")
      return new MyPromise2((resolve) => {
        this.laterCalls.push(() => resolve(callback(this.value)));
      });
    return this;
  }

  resolve(value) {
    this.applyChangedState(value, "resolved");
  }

  reject(value) {
    this.applyChangedState(value, "rejected");
  }

  then(callback) {
    return this.decidePromiseByMethod("then", callback);
  }

  catch(callback) {
    return this.decidePromiseByMethod("catch", callback);
  }
};

(async () => {
  const data = await new MyPromise1((resolve, reject) => {
    setTimeout(() => {
      console.log("first");
      resolve("second");
    }, 2000);
  })
    .then(async (res) => {
      console.log("s", res);
      await new MyPromise1((resolve) => {
        setTimeout(() => {
          console.log("pro2");
          resolve("hihi");
        }, 3000);
      });

      return res;
    })
    .then((res) => {
      console.log("3", res);
    });

  console.log("data", data);
  // console.log("data2", data2 === data);
  console.log("end");
})();

// (async () => {
//   const data = await new MyPromise2((resolve, reject) => {
//     setTimeout(() => {
//       console.log("first");
//       resolve("second");
//     }, 2000);
//   }).then((r) => console.log("r", r));

//   console.log(data);
//   console.log("end");
// })();

class Test {
  constructor(callback) {
    callback(this.resolve.bind(this));
  }
  resolve() {
    this.exit();
  }
  then(resolve, reject) {
    this.exit = resolve;
    return this;
  }
}

// (async () => {
//   // setTimeout(() => {
//   //   console.log("timer");
//   // }, 0);
//   const k = await new Test((resolve) => {
//     setTimeout(() => {
//       console.log("hihi");
//       resolve();
//     }, 2000);
//   });

//   console.log("end");
// })();
