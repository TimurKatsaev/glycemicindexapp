google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(drawChart);

const url = window.location.href;
const id = url[url.length-2]
let arr = []

function createNestedList(str) {
  // Разбиваем строку на верхний уровень по "|"
  let topLevelItems = str.split('|');
  let nestedList = topLevelItems.map(item => {
      // Разбиваем каждый элемент верхнего уровня по ","
      let subItems = item.split(',');
      // Очищаем пробелы
      return subItems.map(subItem => parseFloat(subItem.trim()));
  });
  return nestedList;
}

fetch('/api/notemodel/' + id + '/')
  .then(response => response.json())
  .then(data => {
    arr = createNestedList(data.graph)
  })
  .catch(error => {
    console.error('Error:', error);
  });

  
function drawChart() {
  arr.unshift(['Day', 'Glycemia'])
  var data = google.visualization.arrayToDataTable(arr);

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