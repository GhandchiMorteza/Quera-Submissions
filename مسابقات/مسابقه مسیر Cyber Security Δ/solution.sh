#!/bin/bash

mkdir /bootcamp
touch /bootcamp/bootcamp_data
chown user1:user1 /bootcamp/bootcamp_data
groupadd quera-bootcamp
usermod -G quera-bootcamp user1
usermod -G quera-bootcamp user2
chmod 660 /bootcamp/bootcamp_data
chgrp quera-bootcamp /bootcamp
chmod 0770 /bootcamp
find /bootcamp -maxdepth 1 -type d -not -name 'bootcamp' -exec rm -rf {} \;
find /bootcamp/bootcamp_data -type f -delete
groupdel quera-bootcamp