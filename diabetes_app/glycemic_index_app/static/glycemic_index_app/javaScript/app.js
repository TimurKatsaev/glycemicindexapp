google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(drawChart);

let styleMode = localStorage.getItem('styleMode');
const styleToggle = document.querySelector('.theme-toggle');
const button = document.querySelector('#theme');

const statItems = document.getElementsByClassName('main-item');

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Day', 'Glycemia'],
        ['1', 6.5,],
        ['2', 7.3,],
        ['3', 8.9,],
        ['4', 4.5,],
        ['5', 8.3,],
        ['6', 9.3,],
        ['7', 10.3,],
    ]);

  var options = getOptions(styleMode);

  var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

  chart.draw(data, options);
}

function getOptions(styleMode) {
  if (styleMode === 'dark') {
    return {
      title: 'Company Performance',
      titleTextStyle: {
        color: '#FFFFFF'
      },
      backgroundColor: '#2B2A2F',
      hAxis: {
        textStyle: {
          color: '#FFFFFF'
        },
        gridlines: {
          color: '#555555'
        }
      },
      vAxis: {
        textStyle: {
          color: '#FFFFFF'
        },
        gridlines: {
          color: '#555555'
        }
      },
      legend: {
        textStyle: {
          color: '#FFFFFF'
        }
      },
      colors: ['#ffab00', '#0f9d58', '#4285f4', '#db4437']
    };
  } else {
    return {
      title: 'Company Performance',
      titleTextStyle: {
        color: '#000000'
      },
      backgroundColor: '#FFFFFF',
      hAxis: {
        textStyle: {
          color: '#000000'
        },
        gridlines: {
          color: '#CCCCCC'
        }
      },
      vAxis: {
        textStyle: {
          color: '#000000'
        },
        gridlines: {
          color: '#CCCCCC'
        }
      },
      legend: {
        textStyle: {
          color: '#000000'
        }
      },
      colors: ['#3366CC', '#DC3912', '#FF9900', '#109618']
    };
  }
}

function itemClick(item){
  for (let i = 0; i < statItems.length; i++) {
    statItems[i].classList.remove('active');
  }
  item.classList.add('active');
}

const enableDarkStyle = () => {
  document.body.classList.add('darkstyle');
  button.classList.add('active')
  localStorage.setItem('styleMode', 'dark');
}

const disableDarkStyle = () => {
  document.body.classList.remove('darkstyle');
  button.classList.remove('active')
  localStorage.setItem('styleMode', null);
}

styleToggle.addEventListener('click', () => {
  styleMode = localStorage.getItem('styleMode');
  if (styleMode !== 'dark') {
    enableDarkStyle();
  } else {
    disableDarkStyle();
  }
});

if (styleMode === 'dark') {
  enableDarkStyle();
}