document.addEventListener("DOMContentLoaded", function () {
    console.log('escuchando cundi');

    fetch('/consume_images_cundinamarca2')
        .then(response => response.json())
        .then(data => {
            const dataObject = JSON.parse(data);
            console.log('esta es data final cundinamarca: ', dataObject);

            const container = document.getElementById("image-container");

            // Bucle para crear las 15 imágenes
            for (let i = 0; i < 27; i++) {
                const colDiv = document.createElement("div");
                colDiv.className = "col-4";  // Esto hará que haya hasta 3 imágenes por fila

                const figura = document.createElement("figure");

                const imagen = document.createElement("img");
                imagen.src = dataObject.data[i].image.source.url;
                imagen.alt = "Descripción de la imagen";
                imagen.className = "img-fluid rounded mx-auto d-block";

                const figcaption = document.createElement("figcaption");
                figcaption.textContent = "Por: " + dataObject.data[i].author.name;

                figura.appendChild(imagen);
                figura.appendChild(figcaption);

                colDiv.appendChild(figura);
                container.appendChild(colDiv);
            }

            // Ahora crea el gráfico con los datos obtenidos
            createChart(dataObject);
        });
});
