import numpy as np
str_mystery="481 18 308 13 652 391 63 62 353 111 805 251 36 544 600 799 283 880 \
 470 599 814 507 242 650 180 860 979 298 621 197 572 976 905 427 119 905\
  64 430 742 563 382 211 228 760 567 366 103 409 211 952   5 493 151 267\
 517 495 375  80 341  39 560  85 490  44  17 151  42 688 648 501 437 154\
  66  28 921 642 196 719 208 492 538 687 841 933 386 719 114 261 838 228\
 120 508 316 476 233 902 698 471 604 172 993 790 557 129 446  64 317 997\
 509 710 909 147 228 595 188 246 728 509 365 139 773 426 929 888 534 513\
 666  77 299 943 985 588 137  31 385 405 980 854 327 714 318 909 803 334\
 130 949 532 640 820 975 889 240 878 294 899 488 639 961 819 649 939 163\
 209 879 479 573 557  25 783 332 311 425 140 678 766 492 234 316 811 447\
 772 325 640 387 858 208 739 870 227 385  24 286  22 599 951 994 457  99\
 238 172 549 932 412 545 713  19 785 931 684 333 630 752 191 949 200 361\
 887 243 753 600 635 243 173 249 294 583 106 772 848 387 874 321 562  96\
 211 561 918 868 206 745 710 869 387 600 726 179 336 806 392 612"
str_mystery = str_mystery.split()
mystery = np.zeros(len(str_mystery))
for i in range(len(str_mystery)):
    mystery[i]=str_mystery[i]

print(np.std(mystery))