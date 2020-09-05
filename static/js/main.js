const selected = document.getElementsByTagName('input')[0];
selected.addEventListener("change", () => {
  const browser = selected.value;

  /* Create an array with all elements having class = input */
  const allFields = [...document.getElementsByClassName("input")];
  /* Hide all fields */
  allFields.map(field => field.style.display = "none");

  /* Show the fields depending on browser selection */
  switch (browser.toLowerCase()) {
    case "chrome":
      /* Title, Organization & Description */
      document.getElementById("title").style.display = "block";
      document.getElementById("organization").style.display = "block";
      document.getElementById("description").style.display = "block";
      break;
    case "firefox":
      break;
    default:
      /* Any code that should run if no browser matches */
  }
});