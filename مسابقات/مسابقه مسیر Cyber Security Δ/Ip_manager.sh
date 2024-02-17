#!/bin/bash

isValid() {
    local ip="$1"
    if [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]] || [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$ ]]; then
        return 0
    else
        return 1
    fi
}

handle() {
    local cmd="$1"
    local path="$2"
    if [ ! -f "$path" ]; then
        echo "File does not exist or invalid IP"
        exit 1
    fi
    while IFS= read -r ip; do
        if isValid "$ip"; then
            iptables -D INPUT -s "$ip" -j ACCEPT 2>/dev/null
            iptables -D INPUT -s "$ip" -j DROP 2>/dev/null
            if [ "$cmd" == "block" ]; then
                iptables -A INPUT -s "$ip" -j DROP
            else
                iptables -A INPUT -s "$ip" -j ACCEPT
            fi
        else
            echo "Invalid IP address in file: $ip"
            exit 1
        fi
    done < "$path"
}

if [ $# -lt 2 ]; then
    echo "not enough arguments"
    exit 1
fi

c=$1
a=$2

if [ "$c" != "block" ] && [ "$c" != "unblock" ]; then
    echo "invalid command"
    exit 1
fi

if [ -f "$a" ]; then
    handle "$c" "$a"
elif isValid "$a"; then
    iptables -D INPUT -s "$a" -j ACCEPT 2>/dev/null
    iptables -D INPUT -s "$a" -j DROP 2>/dev/null
    if [ "$c" == "block" ]; then
        iptables -A INPUT -s "$a" -j DROP
    else
        iptables -A INPUT -s "$a" -j ACCEPT
    fi
else
    echo "File does not exist or invalid IP"
    exit 1
fi
