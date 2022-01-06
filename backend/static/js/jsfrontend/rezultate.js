var chart = document.getElementById('chart_voturi').getContext('2d');

async function javascript_chart()
{
    // VECHI!!! Nu stiu daca mai e nevoie de asta.
    // exemplu pentru query parameters
    // ?vot_itemi=["Ion",%20"Maria"]&vot_numar=[325,412]


    // ----Afisarea tabelului----
    // Chart.js

    let vot_title = "Titlu vot";


    /*
        Aici sunt valori PLACEHOLDER
        Este doar o simulare pentru afisarea rezultatelor
        Datele trebuie luate din backend

        (Momentan datele sunt stocate intr-un dictionar. Nu stiu cum vor fi memorate in final...)
    */

    /*
    let vot_itemi =
        {
        "Ionel":34,
        "Dan":46,
        "Maria":42,
        "Ioana":44,
        "Johnny":35,
        "Jane":46
        }*/

    let vot_itemi;

    vot_itemi = await fetch("http://127.0.0.1:5000/getPoolResults?pool_id=123");
    vot_itemi = await vot_itemi.json();
    console.log(vot_itemi);

    // Sortare dictionar
        // TO-DO!!!


    // Chart.js

    let votesChart = new Chart(chart, {
        type:'bar',
        data:{
            labels:Object.keys(vot_itemi),
            datasets:[{
                label:'Voturi',
                data:Object.values(vot_itemi),

                backgroundColor: [
                    'rgba(89, 133, 255, 0.5)',
                    'rgba(255, 89, 133, 0.5)',
                ],
            }],
        },
        options: {
            plugins: {
                title: {
                    display: true,
                    text: 'Rezultatele votului',
                    font:{size:18},
                    padding:{top:30, bottom:20},
                    color:'#182552'
                },
                legend:{
                    display:false
                }
            }
        }
    })


    // ----Calcularea voturilor----

    // Numarul total de voturi
    var nrTotalVoturi = 0;

    for(let i in vot_itemi)
        nrTotalVoturi += vot_itemi[i];

    document.getElementById("nrTotalVoturi").innerText = String(nrTotalVoturi);


    // Castigator
    var nrMaximVoturi = -1;
    var castigatori = "";

    for(let i in vot_itemi)
        if(vot_itemi[i] > nrMaximVoturi)
        nrMaximVoturi = vot_itemi[i];

    for(let i in vot_itemi)
        if(vot_itemi[i] == nrMaximVoturi)
        {
        console.log(i);
        if(castigatori.localeCompare("") != 0)
            castigatori = castigatori.concat(", ");

        castigatori = castigatori.concat(String(i));
        }

    console.log(castigatori);

    document.getElementById("castigatori").innerText = String(castigatori);
}

javascript_chart();
setInterval(javascript_chart, 5000);