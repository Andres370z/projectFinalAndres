fetch('/consume_images').then(response => response.json())
  .then(data => {
    console.log(data);  // Ver los datos en la consola
  })
  .catch(error => console.error('Error al obtener los datos:', error));