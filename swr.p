wd = system("dirname ".ARG0)."\\"
df = wd."swr.txt"

set term qt size 2560,640

set grid ytics
set grid

set xrange [1925:2025]
set xtics 10

set y2range [0:10]
set y2tics 1

set key autotitle columnhead
plot df using 1:2 with lp lw 2, \
     df using 1:3 with lp lw 2, \
     df using 1:(10*$4-50) with lp lw 5
