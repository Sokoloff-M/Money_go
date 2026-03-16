// Основные функции для транзакций
$(document).ready(function() {
    // Автоматическое скрытие сообщений через 5 секунд
    setTimeout(function() {
        $('.alert').fadeOut('slow');
    }, 5000);
    
    // Подтверждение удаления
    $('.delete-confirm').click(function(e) {
        if (!confirm('Вы уверены, что хотите удалить эту запись?')) {
            e.preventDefault();
        }
    });
    
    // Форматирование суммы с разделителями
    function formatAmount(input) {
        let value = input.val().replace(/\D/g, '');
        if (value) {
            value = parseInt(value).toLocaleString('ru-RU');
            input.val(value);
        }
    }
    
    $('#id_amount').blur(function() {
        formatAmount($(this));
    });
});