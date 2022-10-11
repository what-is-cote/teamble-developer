export function qs(selector, target = document) {
  return target.querySelector(selector);
}

export function qsAll(selector, target = document) {
  return target.querySelectorAll(selector);
}

export function on(event, selectorOrEl, callback) {
  if (typeof selectorOrEl === "string") {
    const $el = qs(selectorOrEl);
    $el.addEventListener(event, callback);
  } else {
    selectorOrEl.addEventListener(event, callback);
  }
}

export function delegate(event, parent, selector, callback) {
  const isTarget = (target) => {
    const children = [...qsAll(selector, parent)];
    return children.includes(target) || target.closest(selector);
  };

  parent.addEventListener(event, (e) => {
    isTarget(e.target) && callback(e);
  });
}

export function emit(event, selectorOrEl, payload, options) {
  const E = new CustomEvent(event, {
    cancelable: true,
    detail: payload,
    ...options,
  });

  if (typeof selectorOrEl === "string ") {
    const $el = qs(selectorOrEl);
    $el.dispatchEvent(E);
  } else {
    selectorOrEl.dispatchEvent(E);
  }
}

export function show(selectorOrEl, target) {
  if (typeof selectorOrEl === "string") {
    const $el = qs(selectorOrEl, target);

    $el.style.classList.add("show");
  }
}

export function hide(selectorOrEl, target) {
  if (typeof selectorOrEl === "string") {
    const $el = qs(".to-do-edit");
    console.log($el.style);

    $el.classList.add("hide");
    console.log($el.style);
  }
}
