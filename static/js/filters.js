// Скрипты для фильтрации
$(document).ready(function() {
    // Автоматическая отправка формы при изменении select
    $('#status, #type, #category, #subcategory').change(function() {
        $(this).closest('form').submit();
    });
    
    // Валидация дат
    $('#date_from, #date_to').change(function() {
        let dateFrom = $('#date_from').val();
        let dateTo = $('#date_to').val();
        
        if (dateFrom && dateTo && dateFrom > dateTo) {
            alert('Дата "с" не может быть позже даты "по"');
            $(this).val('');
        }
    });
});