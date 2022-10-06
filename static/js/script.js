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

if (window.location.pathname == "/wishlist/ajax") {
  fetchWishlist()
}

