#!/bin/bash

mkdir -p valgrind_reports
mkdir -p bin_output

echo "[*] 开始批量 Valgrind 检测..."

# 遍历所有 .cpp 文件
for file in output_c_files/*.cpp; do
    name=$(basename "$file" .cpp)
    exe="bin_output/$name"
    report="valgrind_reports/$name.txt"

    echo -e "\n[*] 编译 $file ..."
    g++ "$file" -o "$exe" 2> "$report.compile.log"
    if [[ $? -ne 0 ]]; then
        echo "[-] ❌ 编译失败，跳过 $file（错误日志见 $report.compile.log）"
        continue
    fi

    echo "[*] 使用 Valgrind 检测 $exe ..."
    valgrind --leak-check=full --error-exitcode=1 "$exe" > "$report" 2>&1

    if grep -q "Invalid read\|Invalid write\|definitely lost" "$report"; then
        echo "[!] ⚠️ 潜在漏洞发现于 $file（见 $report）"
    else
        echo "[+] ✅ $file 未发现明显问题"
    fi
done

echo -e "\n[*] 检测完毕，所有报告保存在 valgrind_reports/"