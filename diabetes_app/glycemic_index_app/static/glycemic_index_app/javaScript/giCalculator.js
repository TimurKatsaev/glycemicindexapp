const form = document.getElementById('add-form');

form.addEventListener('submit', function (event) {
    event.preventDefault(); // Предотвращаем стандартное действие отправки формы
    let giInputList = []

    const giInputs = document.getElementsByClassName("form-GI");

    Array.prototype.forEach.call(giInputs, el => {
        giInputList.push(el.value);
    })

    // Выполняем вычисления (например, складываем числа)
    const sum = giInputList.reduce((a, b) => parseInt(a) + parseInt(b), 0);
    const avg = (sum / giInputList.length) || 0;

    // Заполняем результат в отдельное поле
    document.getElementById('avg-gi').value = avg;
    document.getElementById('avg-rcg').value = avg / 1000; // На самом деле это должно определяться по БД пользователя
    document.getElementById('actual-gi').value = giInputList;
    document.getElementById('graph').value = giInputList;

    // После вычислений отправляем форму вручную
    form.submit(); // Отправляем форму
});