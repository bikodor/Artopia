"use strict";

document.addEventListener('DOMContentLoaded', function() {
    // Получаем элемент по его id
    var item = document.getElementById('alarm')
    var itemCount = item.textContent;

    // Преобразуем текстовое содержимое в число
    var count = parseInt(itemCount, 10);
    // Проверяем, больше ли количество нуля
    if (count > 0) {
        // Если да, то меняем стиль другого элемента на "inline"
        item.style.display = 'inline';
    }
});


document.addEventListener('DOMContentLoaded', function() {
    // Проверяем, есть ли элементы с классом 'pack'
    var basket = document.querySelector('div.basket');
    var packs = document.querySelectorAll('.pack');


    if (packs.length === 0) {
        // Если элементов с классом 'pack' нет, удаляем кнопку "Заказать" и выводим сообщение
        var orderButton = document.querySelector('.submit-buy');
        if (orderButton) {
            orderButton.remove(); // Удаляем кнопку "Заказать"
        }

        // Создаем элемент для сообщения "Корзина пуста"
        var emptyMessage = document.createElement('h1');
        emptyMessage.textContent = 'Корзина пуста';
        basket.appendChild(emptyMessage); // Добавляем сообщение в контейнер
    }
});