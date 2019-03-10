apt-get update;
apt-get install -y tor;
apt-get install python;
printf "e[1;93m[!] All requirements are installed! Run python3 multitools.py\e[0m\n"
printf "e[1;93m[!] But first, run tor or service tor start!\e[0m\n"
exit 1