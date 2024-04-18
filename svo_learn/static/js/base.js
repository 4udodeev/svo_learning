document.addEventListener("DOMContentLoaded", function() {
    var menu = document.querySelector('.menu');

    menu.addEventListener('click', function(event) {
        var target = event.target;
        var menuItem = target.closest('.menu-item');
        var submenu = menuItem.querySelector('.submenu');

        // Если клик произошел на кнопке пункта
        if (target.classList.contains('menu-text')) {
            // Снимаем активное состояние со всех пунктов меню, кроме текущего
            var menuItems = menu.querySelectorAll('.menu-item');
            menuItems.forEach(function(item) {
                if (item !== menuItem) {
                    item.classList.remove('active');
                }
            });

            // Применяем активное состояние к текущему пункту меню
            menuItem.classList.toggle('active');

            // Показываем или скрываем подпункты
            if (submenu) {
                submenu.classList.toggle('show');
            }
        }
    });
});
