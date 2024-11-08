# grep使用示例
# 1.查找文件中包含指定字符串的行
grep  "a"  log.txt

# 2.查找文件中不包含指定字符串的行
grep -v "a" log.txt

# 3.查找文件中包含指定字符串的行数
grep -c "a" log.txt

# 4.查找文件中包含指定字符串的行，并显示行号
grep -n "a" log.txt

# 5.查找文件中包含指定字符串的行，并显示匹配的字符串
grep -o "a" log.txt

# 6.查找当前文件夹中包含指定字符串的文件，排除指定文件
grep -rl --exclude="*.jpg" "a" .

# 7.查找当前文件夹中包含指定字符串的文件，只查找指定文件，返回文件名
grep -rl --include="*.txt" "a" . | wc -l

# 8.查找当前文件夹中包含指定字符串的文件，只查找指定文件，返回文件内容
grep -rl --exclude="*.jpg" "a" . | xargs cat | grep -v '^$' | wc -l









