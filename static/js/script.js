const fetchWishlist = async () => {
  const res = await fetch("/wishlist/json")
  const data = await res.json()

  let table = `
      <tr>
        <th>Nama Barang</th>
        <th>Harga Barang</th>
        <th>Deskripsi</th>
      </tr>
  `

  data.forEach((item) => {
    fields = item.fields

    table += `
      <tr>
        <td>${fields.nama_barang}</td>
        <td>${fields.harga_barang}</td>
        <td>${fields.deskripsi}</td>
      </tr>
    `
  })

  document.getElementById("wishlist_table").innerHTML = table
}

document.getElementById("wishlist-form").onsubmit = async (event) => {
  event.preventDefault()

  let csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value

  let formData = new FormData(document.getElementById("wishlist-form"))
  let data = {}

  formData.forEach((value, key) => {
    data[key] = value
  })

  await fetch("/wishlist/ajax/submit", { 
    method: "POST",
    headers: {
      "X-CSRFTOKEN": csrftoken
    },
    body: JSON.stringify(data)
  })
}

if (window.location.pathname == "/wishlist/ajax") {
  fetchWishlist()
}

