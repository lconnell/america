const days = [...document.querySelectorAll('details.day')];
const expand = document.getElementById('expand');
function syncExpand() {
  const allOpen = days.every(day => day.open);
  expand.innerHTML = allOpen ? 'Collapse all days <span aria-hidden="true">−</span>' : 'Expand all days <span aria-hidden="true">+</span>';
  expand.setAttribute('aria-label', allOpen ? 'Collapse all itinerary days' : 'Expand all itinerary days');
}
expand.addEventListener('click', () => {
  const next = !days.every(day => day.open);
  days.forEach(day => { day.open = next; });
  syncExpand();
});
days.forEach(day => day.addEventListener('toggle', syncExpand));
function revealLinkedDay() {
  const id = window.location.hash.slice(1);
  const day = days.find(day => day.id === id);
  if (day) day.open = true;
}
window.addEventListener('hashchange', revealLinkedDay);
revealLinkedDay();
let printState;
function preparePrint() {
  if (printState) return;
  const details = [...document.querySelectorAll('details')];
  printState = details.map(el => [el, el.open]);
  details.forEach(el => { el.open = true; });
}
window.addEventListener('beforeprint', preparePrint);
window.addEventListener('afterprint', () => {
  printState?.forEach(([el, open]) => { el.open = open; });
  printState = undefined;
});
document.getElementById('print').addEventListener('click', () => { preparePrint(); window.print(); });
syncExpand();
