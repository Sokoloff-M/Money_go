// Скрипты для справочников
$(document).ready(function() {
    // Сортировка таблиц
    $('.sortable').click(function() {
        let table = $(this).closest('table');
        let index = $(this).index();
        let rows = table.find('tbody tr').get();
        
        rows.sort(function(a, b) {
            let keyA = $(a).children('td').eq(index).text().toUpperCase();
            let keyB = $(b).children('td').eq(index).text().toUpperCase();
            
            if ($(this).hasClass('asc')) {
                return keyA.localeCompare(keyB);
            } else {
                return keyB.localeCompare(keyA);
            }
        });
        
        $.each(rows, function(index, row) {
            table.children('tbody').append(row);
        });
        
        $(this).toggleClass('asc desc');
    });
});