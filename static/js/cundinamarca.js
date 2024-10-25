document.addEventListener("DOMContentLoaded", function () {
    console.log('escuchando cundi');

    fetch('/consume_images_Boyaca2')
        .then(response => response.json())
        .then(data => {
            const dataObject = JSON.parse(data);
            console.log('esta es dat final cundinamarca: ', dataObject);

            // Ahora crea el gráfico con los datos obtenidos
            createChart(dataObject);
        })
});

function createChart(dataObject) {
    console.log('Te escucho');
    
    console.log('Este es source ', dataObject.data[5].image.source.url);

    const masFotos = Object.values(dataObject.infoMasFotogra);
    const nombreFotogra = Object.keys(dataObject.infoMasFotogra);
    const nombreFotograFO = Object.keys(dataObject.infoMasFotos);
    const nombreLugar = Object.values(dataObject.infoMasFotos);
    console.log('mas fotos ', nombreLugar[0]);
    console.log('fotografo ', nombreFotograFO[0]);

    // Aquí puedes extraer los datos necesarios de dataObject
    const totalFotos = dataObject.totalFotos || 100;
    const infoMasFotos = dataObject.infoMasFotos || 60;
    const topFotografos = ['Fotos por pila', 'Fotografo con mas fotos: ' + nombreFotogra[0], 'lugar con mas fotos:' + nombreFotograFO[0]];
    const aportes = [dataObject.data.length, masFotos[0], nombreLugar[0]];
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar', // Tipo de gráfico
        data: {
            labels: topFotografos, // Etiquetas para el eje X
            datasets: [{
                label: 'Aportes de Fotógrafos',
                data: aportes, // Datos para el gráfico
                backgroundColor: [
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });


    // Crea un elemento figure
    var figura = document.createElement("figure");

    // Crea el elemento img
    var imagen = document.createElement("img");
    imagen.src = dataObject.data[5].image.source.url;
    
    imagen.alt = "Descripción de la imagen";
    imagen.className = "img-fluid rounded mx-auto d-block";

    var figcaption = document.createElement("figcaption");
    figcaption.textContent = "Por: " + dataObject.data[5].author.name;

    figura.appendChild(imagen);
    figura.appendChild(figcaption);



   

    // Crea el elemento img
    

    var figura = document.createElement("figure");

    // Crea el elemento img
    var imagen = document.createElement("img");
    imagen.src = dataObject.data[27].image.source.url;
    imagen.alt = "Descripción de la imagen";
    imagen.className = "img-fluid rounded mx-auto d-block";

    var figcaption = document.createElement("figcaption");
    figcaption.textContent = "Por: " + dataObject.data[27].author.name;

    figura.appendChild(imagen);
    figura.appendChild(figcaption);

    document.getElementById("myImage2").appendChild(figura);

    var figura = document.createElement("figure");

    // Crea el elemento img
    var imagen = document.createElement("img");
    imagen.src = dataObject.data[35].image.source.url;
    imagen.alt = "Descripción de la imagen";
    imagen.className = "img-fluid rounded mx-auto d-block";

    var figcaption = document.createElement("figcaption");
    figcaption.textContent = "Por: " + dataObject.data[35].author.name;

    figura.appendChild(imagen);
    figura.appendChild(figcaption);

    document.getElementById("myImage3").appendChild(figura);

    var figura = document.createElement("figure");

    // Crea el elemento img
    var imagen = document.createElement("img");
    imagen.src = dataObject.data[75].image.source.url;
    imagen.alt = "Descripción de la imagen";
    imagen.className = "img-fluid rounded mx-auto d-block";

    var figcaption = document.createElement("figcaption");
    figcaption.textContent = "Por: " + dataObject.data[75].author.name;

    figura.appendChild(imagen);
    figura.appendChild(figcaption);

    document.getElementById("myImage4").appendChild(figura);
}
