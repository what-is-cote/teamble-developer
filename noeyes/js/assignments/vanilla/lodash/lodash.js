Array.prototype.myReduce = function (callback, init) {
  let prev = init ? init : this[0];

  for (let i = init == null ? 1 : 0; i < this.length; i++) {
    prev = callback(prev, this[i], i, this);
  }

  return prev;
};

Array.prototype.myFilter = function (callback) {
  const arr = [];
  for (let i = 0; i < this.length; i++) {
    callback(this[i], i, this) && arr.push(this[i]);
  }

  return arr;
};

var testArray = [
  {
    description: "Random description.",
    testNumber: 123456789,
    testBoolean: true,
    testObject: {
      testString: "test string",
      testNumber: 12345,
    },
    testArray: [
      {
        myName: "test name",
        myNumber: 123245,
      },
    ],
  },
  {
    description: "Random description.",
    testNumber: 123456789,
    testBoolean: true,
    testObject: {
      testString: "test string",
      testNumber: 12345,
    },
    testArray: [
      {
        myName: "test name",
        myNumber: 123245,
      },
    ],
  },
];
var a = {
  test: [1],
  love: { id: 3, mylove: { name: "yj", age: 25 } },
  n: 11,
};
const deepCopy = function (obj) {
  const copiedObj = {};
  function recursiveCopy(data) {
    const local = {};
    if (Array.isArray(data)) return data.map((e) => recursiveCopy(e));
    else if (data && typeof data === "object") {
      for (let k in data) local[k] = recursiveCopy(data[k]);
      return local;
    } else return data;
  }

  for (let k in obj) {
    copiedObj[k] = recursiveCopy(obj[k]);
  }

  return copiedObj;
};

function renameKey(obj, old_key, new_key) {
  if (old_key !== new_key) {
    Object.defineProperty(
      obj,
      new_key,
      Object.getOwnPropertyDescriptor(obj, old_key)
    );
    delete obj[old_key];
  }
}

/**
 *
 * @param {string} tag
 * @param {Document | HTMLElement} target
 */
function qsAll(tag, target = document) {
  const result = [];

  const selectNode = (parent) => {
    Array.from(parent.children).forEach((node) => {
      if (node.tagName === tag.toUpperCase()) result.push(node);

      selectNode(node);
    });
  };

  selectNode(target);

  return result;
}

console.log(qsAll("button"));

class MyPromise1 {
  constructor(executor) {
    this.result;
    this.state = "pending";
    this.nextCallback = [];

    try {
      executor(this.resolve.bind(this), this.reject.bind(this));
    } catch (err) {
      this.reject(err);
    }
  }

  resolve(data) {
    this.update(data, "fulfilled");
  }
  reject(data) {
    this.update(data, "rejected");
  }

  update(data, state) {
    this.result = data;
    this.state = state;

    this.flush(data);
  }

  then(resolvedCallback, rejectedCallback = () => {}) {
    return new MyPromise1((resolve, reject) => {
      this.nextCallback.push((value) => {
        if (this.state === "fulfilled") return resolve(resolvedCallback(value));
        if (this.state === "rejected") return reject(rejectedCallback(value));
      });
    });
  }

  flush(data) {
    if (data instanceof MyPromise1 || data instanceof Promise) {
      if (data.state === "pending") {
        data.then(
          (value) => {
            this.state = "fulfilled";
            this.result = value;
            this.nextCallback.forEach((callback) => callback(value));
          },
          (value) => {
            this.state = "rejected";
            this.result = value;
            this.nextCallback.forEach((callback) => callback(value));
          }
        );
      } else {
        this.nextCallback.forEach((callback) => callback(data.result));
      }
    } else {
      this.nextCallback.forEach((callback) => callback(data));
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
        this.laterCalls.forEach((latercall) => latercall());
      });
    } else {
      this.value = value;
      this.state = state;

      this.laterCalls.forEach((latercall) => latercall());
    }
  }

  decidePromiseByMethod(method, callback) {
    const state = method === "then" ? "resolved" : "rejected";
    if (this.state === state)
      return new MyPromise2((resolve) => resolve(callback(this.value)));

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
    console.log("then");
    return this.decidePromiseByMethod("then", callback);
  }

  catch(callback) {
    return this.decidePromiseByMethod("catch", callback);
  }
};

(async () => {
  const data = await new MyPromise2((resolve, reject) => {
    setTimeout(() => {
      console.log("first");
      resolve("before");
    }, 2000);
  });

  console.log(data);
  console.log("after");
})();
