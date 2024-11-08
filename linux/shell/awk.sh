# 提取第一列，排序，统计出现次数，按次数从大到小排序
# sort 默认根据ASCII码值排序，-n 按数值排序从小到大，-r 逆序
awk '{print $1}' log.txt | uniq -c | sort -nr
# awk '{print $1}' log.txt：提取 log.txt 文件的第一列。
# sort：对提取的第一列根据ASCII码进行排序。
# uniq -c：统计每个元素出现的次数。
# sort -nr：按出现次数从大到小排序。

# 以逗号为分隔符，提取 log.txt 文件的第一列，统计每个元素出现的次数，按出现次数从大到小排序，取出现次数最多的元素。
awk -F ',' '{print $1}' log.txt | uniq -c | sort -nr | head -n 1

# wc -l log.txt：统计 log.txt 文件的行数。
wc -l log.txt


# 提取第一列数据并求和
awk -F ',' '{sum += $1} END {print sum}' a.csv

# 提取第一列数据并求平均值
awk -F ',' '{sum += $1} END {print sum/NR}' a.csv
# NR：表示行号，awk 内置变量，表示当前处理的行号。

# 提取第一列数据并求最大值
awk -F ','  'BEGIN {max = 0} {if ($1 > max) max = $1} END {print max}' a.csv

# 提取第一列数据并求最小值
awk -F ','  'BEGIN {min = 999999999} {if ($1 < min) min = $1} END {print min}' a.csv