fetch('/consume_images').then(response => response.json())
  .then(data => {
    console.log(data);  // Ver los datos en la consola
    if (data) {
      console.log('entra');
      for (let index = 0; index < data.length; index++) {
        let myImages = data[index].url
        console.log(myImages);
        const div = document.createElement('div')
        div.className('images');
        const main = document.getElementById('main');
        main.appendChild(div);
        //Carga de Imagenes:
        div.innerHTML = `<img src="${{myImages}}" alt="">`
      }
    }


  })
  .catch(error => console.error('Error al obtener los datos:', error));