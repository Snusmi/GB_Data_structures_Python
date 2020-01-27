######################
######################

aglasis@LAPTOP-C0OP46FS:~$ cat username.sh
#!/bin/bash

for n in {1..3}
do
        echo $USER
done
aglasis@LAPTOP-C0OP46FS:~$ bash username.sh
aglasis
aglasis
aglasis
aglasis@LAPTOP-C0OP46FS:~$ cat numbers.sh

#!/bin/bash

y=0

while [ $y -lt 100 ]

do
 echo $y
 (( y+=2 ))
done
aglasis@LAPTOP-C0OP46FS:~$ bash numbers.sh
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
aglasis@LAPTOP-C0OP46FS:~$ cat backup.sh
#!/bin/bash
$(cp -f /home/aglasis/test.txt /home/aglasis/test.txt.bak)
aglasis@LAPTOP-C0OP46FS:~$ chmod +x backup.sh
aglasis@LAPTOP-C0OP46FS:~$ crontab -l
no crontab for aglasis
aglasis@LAPTOP-C0OP46FS:~$ crontab -e
no crontab for aglasis - using an empty one

Select an editor.  To change later, run 'select-editor'.
  1. /bin/nano        <---- easiest
  2. /usr/bin/vim.basic
  3. /usr/bin/mcedit
  4. /usr/bin/vim.tiny
  5. /bin/ed

Choose 1-5 [1]: 1
crontab: installing new crontab
aglasis@LAPTOP-C0OP46FS:~$ crontab -l
*/10 * * * * /home/aglasis/backup.sh
aglasis@LAPTOP-C0OP46FS:~$