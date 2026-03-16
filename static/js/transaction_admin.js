// Скрипт для админки Django
(function($) {
    $(document).ready(function() {
        // Динамическая загрузка категорий
        $('#id_type').change(function() {
            var typeId = $(this).val();
            if (typeId) {
                $.ajax({
                    url: '/api/get-categories/',
                    data: {type_id: typeId},
                    success: function(data) {
                        var categorySelect = $('#id_category');
                        categorySelect.empty();
                        categorySelect.append('<option value="">---------</option>');
                        $.each(data, function(key, value) {
                            categorySelect.append('<option value="' + value.id + '">' + value.name + '</option>');
                        });
                    }
                });
            }
        });
        
        // Динамическая загрузка подкатегорий
        $('#id_category').change(function() {
            var categoryId = $(this).val();
            if (categoryId) {
                $.ajax({
                    url: '/api/get-subcategories/',
                    data: {category_id: categoryId},
                    success: function(data) {
                        var subcategorySelect = $('#id_subcategory');
                        subcategorySelect.empty();
                        subcategorySelect.append('<option value="">---------</option>');
                        $.each(data, function(key, value) {
                            subcategorySelect.append('<option value="' + value.id + '">' + value.name + '</option>');
                        });
                    }
                });
            }
        });
    });
})(django.jQuery);