import debounceFrame from "./debounceFrame.js";

const store = {
  states: [],
  stateKey: 0,
  root: null,
};

const _render = debounceFrame(() => {
  store.stateKey = 0;
  store.root();
});

export function render(root) {
  store.root = root;
  _render();
}

export function useState(init) {
  if (store.states.length === store.stateKey) {
    store.states.push(init);
  }
  const { states, stateKey } = store;
  const state = states[stateKey];

  store.stateKey += 1;

  function setState(newState) {
    states[stateKey] = newState;
    _render();
  }

  return [state, setState];
}
