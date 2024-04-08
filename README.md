# qa_guru_python_8_22
Задание к двадцать второму уроку курса QA Guru

## Локальный запуск на эмулированном устройсте
pytest -s -v --context=local_emulator .

## Локальный запуск на реальном устройсте
pytest -s -v --context=local_real_device .

## Удаленный запуск на BrowserStack
pytest -s -v --context=bstack .

## Просмотр отчета allure
allure serve .\allure-results\