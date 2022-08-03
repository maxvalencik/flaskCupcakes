const BASE_URL = "http://127.0.0.1:5000/api";


/** Create html */

function generateHTML(cupcake) {
  return `
    <div data-cupcake-id=${cupcake.id}>
      <li>
        ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
        <button class="delete-button">X</button>
      </li>
      <img class="Cupcake-img"
            src="${cupcake.image}"
            alt="(no image provided)">
    </div>
  `;
}


/** put initial cupcakes on page. */

async function showCupcakes() {
  const response = await axios.get(`${BASE_URL}/cupcakes`);
  for (let cupcake of response.data.cupcakes) {
    let newCupcake = generateHTML(cupcake);
    // let newCupcake = generateHTML(cupcake);
    document.getElementById("cupcakes-list").insertAdjacentHTML('beforeend',newCupcake);
  }
}


 /**handle clicking delete: delete cupcake*/ 

 //Using jQuery .on() function -- $("#") selects elements of ID ...
$("#cupcakes-list").on("click", ".delete-button", async function (evt) {
  evt.preventDefault();
  let $cupcake = $(evt.target).closest("div");
  let cupcakeId = $cupcake.attr("data-cupcake-id");

  await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
  $cupcake.remove();
});


showCupcakes();