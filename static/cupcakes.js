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


/** handle form for adding of new cupcakes 

$("#new-cupcake-form").on("submit", async function (evt) {
  evt.preventDefault();

  let flavor = $("#form-flavor").val();
  let rating = $("#form-rating").val();
  let size = $("#form-size").val();
  let image = $("#form-image").val();

  const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
    flavor,
    rating,
    size,
    image
  });

  let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
  getElementById("#cupcakes-list").append(newCupcake);
  getElementById("#new-cupcake-form").trigger("reset");
});*/


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