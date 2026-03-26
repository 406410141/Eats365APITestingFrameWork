#!/bin/bash


echo "🚀 正在執行 Pytest 測試..."
pytest --alluredir=allure-results || true


echo "📊 正在生成 Allure 報告..."
allure generate allure-results -o allure-report --clean


echo "🌐 報告已就緒！請在瀏覽器開啟 http://localhost:8070"
python3 -m http.server 8070 --directory allure-report