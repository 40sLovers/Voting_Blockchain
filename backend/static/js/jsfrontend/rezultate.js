// Chart.js
var chart = document.getElementById('chart_voturi').getContext('2d');

// Luam date
let vot_itemi;
let dict_voturi = {};

async function luam_date()
{
    vot_itemi = await fetch("http://127.0.0.1:5000/getPoolResults?pool_id=123");
    vot_itemi = await vot_itemi.json();

    var key, val;

    for(i in vot_itemi)
    {
        key = Object.keys(vot_itemi[i])[0];
        val = Object.values(vot_itemi[i])[0];

        dict_voturi[key] = val;
    }
}
luam_date();

// Creare tabel
/*
    Aici sunt valori PLACEHOLDER
    Este doar o simulare pentru afisarea rezultatelor
    Datele trebuie luate din backend

    (Momentan datele sunt stocate intr-o lista de dictionare. Nu stiu cum vor fi memorate in final...)
*/


let votesChart = new Chart(chart, {
    type:'bar',
    data:{
        labels:[],
        datasets:[{
            label:'Voturi',
            data:[],

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

// Calcule pentru voturi
async function calcul_nr_total_voturi(dict_voturi)
{
    // Numarul total de voturi
    var nrTotalVoturi = 0;

    for(let i in dict_voturi)
        nrTotalVoturi += dict_voturi[i];

    document.getElementById("nrTotalVoturi").innerText = String(nrTotalVoturi);
}

async function calcul_castigatori(dict_voturi)
{
    var nrMaximVoturi = -1;
    var castigatori = "";

    for(let i in dict_voturi)
        if(dict_voturi[i] > nrMaximVoturi)
        nrMaximVoturi = dict_voturi[i];

    for(let i in dict_voturi)
        if(dict_voturi[i] == nrMaximVoturi)
        {
        console.log(i);
        if(castigatori.localeCompare("") != 0)
            castigatori = castigatori.concat(", ");

        castigatori = castigatori.concat(String(i));
        }

    document.getElementById("castigatori").innerText = String(castigatori);
}

// Updatarea tabelului
async function updatare_tabel()
{
    var l = Object.keys(dict_voturi).length;
    for(var i=0; i<l; i++)
    {
        votesChart["data"]["labels"][i] = Object.keys(dict_voturi)[i];
        votesChart["data"]["datasets"][0]["data"][i] = Object.values(dict_voturi)[i];
    }

    votesChart.update();
}

// Functie
async function javascript_chart()
{
    // Luam date
    luam_date();
    console.log(dict_voturi);
    // Sortare dictionar
        // TO-DO!!!

    updatare_tabel();

    // Calcularea voturilor;
    calcul_nr_total_voturi(dict_voturi);
    calcul_castigatori(dict_voturi);

    // Updatare tabel
}

javascript_chart();
setInterval(javascript_chart, 5000);