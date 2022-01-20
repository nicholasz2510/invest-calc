wd = system("dirname ".ARG0)."\\"
df = wd."cirr.txt"

set term qt size 2560,640

set grid ytics
set grid

set xrange [1925:2025]
set xtics 10

set key autotitle columnhead
plot df using 1:2 with lp lw 2
