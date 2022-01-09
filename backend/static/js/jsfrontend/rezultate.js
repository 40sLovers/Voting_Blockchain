// Chart.js
var chart = document.getElementById('chart_voturi').getContext('2d');

// Creare tabel
/*
    Aici sunt valori PLACEHOLDER
    Este doar o simulare pentru afisarea rezultatelor
    Datele trebuie luate din backend

    (Momentan datele sunt stocate intr-o lista de dictionare.)
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
        maintainAspectRatio: false,
        plugins: {
            title: {
                display: true,
                text: 'Rezultatele votului',
                font:{size:18},
                padding:{top:30, bottom:20},
                color:'#182552',
            },
            legend:{
                display:false
            }
        }
    }
})

// Luam date
let vot_itemi;
async function luam_date()
{
    const urlParams = new URLSearchParams(window.location.search);
    let cod = urlParams.get('cod');
    vot_itemi = await fetch(`${window.location.protocol}//${ window.location.host}/getPoolResults?pool_id=${cod}`);
    vot_itemi = await vot_itemi.json();
}
luam_date();

function comparare(first,second){
    console.log(first);
    console.log(second);
    console.log((Object.keys(first)[0] > Object.keys(second)[0]));
    if(Object.keys(first)[0] > Object.keys(second)[0])
        return true;
    return false;
}

function sort_nume()
{
    var l = vot_itemi.length;
    for(var i=0; i<l-1; i++)
    {
        for(var j=i+1; j<l; j++)
        {
            if(Object.keys(vot_itemi[i])[0] > Object.keys(vot_itemi[j])[0])
            {
                var aux=vot_itemi[i];
                vot_itemi[i] = vot_itemi[j];
                vot_itemi[j] = aux;
            }
        }
    }
}

function sort_valori()
{
    var l = vot_itemi.length;
    for(var i=0; i<l-1; i++)
    {
        for(var j=i+1; j<l; j++)
        {
            if(Object.values(vot_itemi[i])[0] > Object.values(vot_itemi[j])[0])
            {
                var aux=vot_itemi[i];
                vot_itemi[i] = vot_itemi[j];
                vot_itemi[j] = aux;
            }
        }
    }
}

function sortari()
{
    var checkBox_nume   = document.getElementById('sortAlfabetic');
    var checkBox_ordine = document.getElementById('sortOrdine');

    if(checkBox_nume.checked)
    {
        sort_nume();
        if(checkBox_ordine.checked)
            vot_itemi.reverse();
    }  
    else
    {
        sort_valori();
        if(checkBox_ordine.checked)
            vot_itemi.reverse();
    }

    updatare_tabel();
}

// Calcule pentru voturi
async function calcul_nr_total_voturi()
{
    var nrTotalVoturi = 
    vot_itemi.map((el)=> Object.values(el)[0])
    .reduce((prev,curr)=>prev+curr,0);
    document.getElementById("nrTotalVoturi").innerText = String(nrTotalVoturi);
}

async function calcul_castigatori()
{
    var nrMaximVoturi = -1;
    var castigatori = "";
    nrMaximVoturi = Math.max(...vot_itemi.map((el)=>Object.values(el)[0]))

    castigatori = 
    vot_itemi.filter((el)=> Object.values(el)[0] == nrMaximVoturi)
    .map((el)=>Object.keys(el)[0])
    document.getElementById("castigatori").innerText = String(castigatori);
}

// Updatarea tabelului
async function updatare_tabel()
{
    votesChart["data"]["labels"]= vot_itemi.map((el)=>Object.keys(el)[0]);
    votesChart["data"]["datasets"][0]["data"]=vot_itemi.map((el)=>Object.values(el)[0]);
    votesChart.update();
}

// Functie
async function javascript_chart()
{
    // Luam date
    await luam_date();

    // Sortare
    sortari();

    // Calcularea voturilor;
    calcul_nr_total_voturi();
    calcul_castigatori();

    // Updatare tabel
    updatare_tabel();
}

javascript_chart();
setInterval(javascript_chart, 5000);