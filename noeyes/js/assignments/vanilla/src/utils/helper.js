// @ts-check

/**
 *  @typedef {Object} Options
 *  @property {string} [id]
 *  @property {string} [class]
 *  @property {object} [attributes]
 */

/**
 *
 * @param {string} selector
 * @param {HTMLElement | Document} [target]
 * @returns
 */
export function qs(selector, target = document) {
  return target.querySelector(selector);
}

/**
 *
 * @param {string} tag
 * @param {Options} [options]
 * @returns
 */
export function createEl(tag, options = {}) {
  const $el = document.createElement(tag);

  if (options.id) $el.id = options.id;
  if (options.class) $el.className = options.class;
  if (options.attributes) {
    Object.entries(options.attributes).forEach(([key, value]) =>
      $el.setAttribute(key, value)
    );
  }

  return $el;
}
