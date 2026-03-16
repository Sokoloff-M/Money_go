import os

# Корневая папка проекта (текущая)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Структура папок (ключ - папка, значение - список файлов в ней)
structure = {
    "config": ["__init__.py", "settings.py", "urls.py", "asgi.py", "wsgi.py"],
    "apps/transactions": ["__init__.py", "admin.py", "apps.py", "models.py", "views.py", "urls.py", "forms.py", "filters.py", "utils.py"],
    "apps/directories": ["__init__.py", "admin.py", "apps.py", "models.py", "views.py", "urls.py", "forms.py"],
    "static/css": ["style.css", "admin_custom.css"],
    "static/js": ["transactions.js", "filters.js", "directories.js"],
    "static/images": ["favicon.ico"],
    "templates/includes": ["header.html", "footer.html", "filters.html"],
    "templates/transactions": ["list.html", "create.html", "edit.html", "delete.html"],
    "templates/directories": ["status_list.html", "type_list.html", "category_list.html", "subcategory_list.html"],
    "templates/directories/forms": ["status_form.html", "type_form.html", "category_form.html", "subcategory_form.html"],
    "fixtures": ["initial_status.json", "initial_types.json", "initial_categories.json"],
    "tests": ["__init__.py", "test_models.py", "test_views.py", "test_forms.py"],
    "docs": ["api.md", "user_guide.md"],
    "media": [],
    "staticfiles": [],
}

# Корневые файлы
root_files = [
    "manage.py",
    "requirements.txt",
    "README.md",
    ".gitignore",
    ".env",
]

# Создаём папки и файлы
for folder, files in structure.items():
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if not os.path.exists(file_path):
            open(file_path, 'a').close()  # создаёт пустой файл
            print(f"Создан: {file_path}")

for file in root_files:
    file_path = os.path.join(base_dir, file)
    if not os.path.exists(file_path):
        open(file_path, 'a').close()
        print(f"Создан: {file_path}")

print("\n✅ Структура проекта успешно создана!")