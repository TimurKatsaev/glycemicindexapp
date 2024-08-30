const form = document.getElementById('add-form');

form.addEventListener('submit', function (event) {
    event.preventDefault(); // Предотвращаем стандартное действие отправки формы

    let giInputList = []
    const giInputs = document.getElementsByClassName("form-GI");
    const glycemia = document.getElementById("form-glycemia").value;
    const bread_units = document.getElementById("form-XE").value;
    const time_in = 10; // На самом деле это должно определяться по БД пользователя
    const bu_index = 2; // На самом деле это должно определяться по БД пользователя
    let graph = ''
    
    // Добавляем ГИ с инпутов в список
    Array.prototype.forEach.call(giInputs, el => {
        giInputList.push(el.value);
    })
    
    // Выполняем вычисления
    const sum = giInputList.reduce((a, b) => parseInt(a) + parseInt(b), 0);
    const avgGi = (sum / giInputList.length) || 0;
    const avgRsg = avgGi / 1000; // На самом деле это должно определяться по БД пользователя
    const absorption_time = (bread_units*bu_index*1000)/avgGi

    // Заполняем результат в отдельное поле
    document.getElementById('avg-gi').value = avgGi;
    document.getElementById('avg-rcg').value = avgRsg; // На самом деле это должно определяться по БД пользователя
    document.getElementById('actual-gi').value = giInputList;

    // Вычисляем график

    let minutes = time_in

    for (let i = 1; i <= time_in; i++) {
        graph += (`${i},${glycemia}|`)
    }

    for (let i = 1; i <= absorption_time; i++) {
        graph += (`${minutes+i},${parseFloat(glycemia)+parseFloat(avgRsg)*i}|`)
    }

    for (let i = 1; i <= 5; i++) {
        graph +=(`${minutes+parseInt(absorption_time)+i},${parseFloat(glycemia)+parseFloat(avgRsg)*absorption_time}|`);
        if (i == 5){
            graph +=(`${minutes+parseInt(absorption_time)+i},${parseFloat(glycemia)+parseFloat(avgRsg)*absorption_time}`);
        }
    }

    // Заполняем результат графика в отдельное поле
    document.getElementById('graph').value = graph;

    // После вычислений отправляем форму вручную
    form.submit(); // Отправляем форму
});