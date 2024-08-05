google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(drawChart);

let styleMode = localStorage.getItem('styleMode');
const styleToggle = document.querySelector('.theme-toggle');
const button = document.querySelector('#theme');

function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ['Minutes', 'Glycemia'],
    ['5', 6.5,],
    ['10', 7.3,],
    ['15', 7.7,],
    ['20', 7.9,],
    ['25', 8.3,],
    ['30', 9.3,],
    ['35', 9.3,],
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